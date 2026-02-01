
import os
import sys
import time
import random

from google import genai

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# -------------------------------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

print("BASE_DIR =", BASE_DIR)

# -------------------------------------------------------------------------------------------------

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.db import transaction, close_old_connections
from jobs.models import Job

# -------------------------------------------------------------------------------------------------

from core.Logger import get_logger
logger = get_logger("__name__")

# -------------------------------------------------------------------------------------------------

from Functions.CommonFunctions import getDriver
from Functions.CompareResumeAndJobDescription import compareJob
from Functions.CompareResumeAndJobDescription import fetchGeminiAccessKey

# -------------------------------------------------------------------------------------------------


def fetch_job_for_scraping(job_pick_order="new_to_old"):
    """
    Fetch ONE job safely from DB based on order.
    job_pick_order = "new_to_old" / "old_to_new"
    """
    logger.debug('Function Initialized')

    # 🔹 CHANGE: Ensure fresh DB connection
    close_old_connections()

    order_by_field = "-created_at" if job_pick_order == "new_to_old" else "created_at"

    with transaction.atomic():
        job = (
            Job.objects
            .select_for_update(skip_locked=True)
            .filter(scrape_status="pending")
            .order_by(order_by_field)
            .first()
        )

        if job:
            job.scrape_status = "processing"
            job.save(update_fields=["scrape_status"])

        return job


# -------------------------------------------------------------------------------------------------


def getExperience(driver):
    return safeText(driver, "//div[contains(@class,'exp__')]//span")


def getSalary(driver):
    return safeText(driver, "//div[contains(@class,'salary__')]//span")


def getLocation(driver):
    try:
        locations = driver.find_elements(
            By.XPATH, "//div[contains(@class,'loc_')]//a"
        )
        return ", ".join([loc.text for loc in locations])
    except:
        return None


def getCompany(driver):
    return safeText(
        driver,
        "//div[contains(@class,'jd-header-comp-name')]//a[1]"
    )


# -------------------------------------------------------------------------------------------------


def safeText(driver, xpath):
    """
    Safely extract text
    """
    try:
        return driver.find_element(By.XPATH, xpath).text.strip()
    except:
        return None


# -------------------------------------------------------------------------------------------------


def scrapeJobDetail(driver, url):
    """
    Scrape individual job details
    """
    logger.debug("Function Initialized")

    driver.get(url)

    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3)")
    time.sleep(2)

    job_data_dict = {
        "url": url,
        "title": None,
        "company": None,
        "experience": None,
        "salary": None,
        "location": None,
        "description": None,
    }

    try:
        job_data_dict["title"] = driver.find_element(By.TAG_NAME, "h1").text
    except:
        logger.warning("Job title not found")

    job_data_dict["company"] = getCompany(driver)
    job_data_dict["experience"] = getExperience(driver)
    job_data_dict["salary"] = getSalary(driver)
    job_data_dict["location"] = getLocation(driver)

    try:
        job_data_dict["description"] = driver.find_element(
            By.XPATH, "//section[contains(@class,'job-desc')]"
        ).text
    except:
        logger.warning("Job description not found")

    logger.info("Job scraped successfully")
    return job_data_dict


# -------------------------------------------------------------------------------------------------


def save_scrape_result(job, resume_match, error=None):
    """
    Update job after scraping & comparison
    """
    logger.debug('Function Initialized')

    # 🔹 CHANGE: Ensure fresh DB connection
    close_old_connections()

    job.resume_match = resume_match
    job.scrape_status = "done"
    job.last_error = error
    job.save(
        update_fields=[
            "resume_match",
            "scrape_status",
            "last_error",
            "updated_at",
        ]
    )


# -------------------------------------------------------------------------------------------------


def mark_job_failed(job, error):
    """
    """
    logger.debug('Function Initialized')

    # 🔹 CHANGE: Ensure fresh DB connection
    close_old_connections()

    job.scrape_status = "failed"
    job.last_error = str(error)
    job.save(update_fields=["scrape_status", "last_error", "updated_at"])


# -------------------------------------------------------------------------------------------------


def scraper_worker():
    logger.debug("Scraper worker started")

    job_idle_sleep_minutes = 5
    scrap_gap_seconds = 60

    idle_sleep_seconds = job_idle_sleep_minutes * 60

    driver = getDriver()
    api_key = fetchGeminiAccessKey()
    client = genai.Client(api_key=api_key)

    while True:
        job = None

        try:
            job = fetch_job_for_scraping()

            if not job:
                logger.info(
                    f"No pending jobs. Sleeping for {job_idle_sleep_minutes} minutes..."
                )
                time.sleep(idle_sleep_seconds)
                continue

            logger.info(
                f"Processing job | ID : {job.naukri_job_id} | Link : {job.job_url}"
            )

            job_data = scrapeJobDetail(driver=driver, url=job.job_url)

            logger.info("Comparing resume...")
            comparison_result = compareJob(
                client=client,
                job_description=str(job_data)
            )

            resume_match = comparison_result == "True"

            save_scrape_result(job=job, resume_match=resume_match)

            logger.info(
                f"Job completed | ID={job.naukri_job_id} | resume_match={resume_match}"
            )

            time.sleep(scrap_gap_seconds)

        except Exception as e:
            logger.error(f"Scraper error | {e}", exc_info=True)

            if job:
                mark_job_failed(job, e)

            time.sleep(10)


# -------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    scraper_worker()
