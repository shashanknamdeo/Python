import time
import random
import os
import django
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Functions.CommonFunctions import extract_naukri_job_id

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hireiq.settings")
# django.setup()

# from jobs.models import Job

from Functions.CommonFunctions import getDriver
from core.Logger import get_logger

logger = get_logger("__name__")



def openJobsPage(driver):
    """
    Open job listing page with dynamic parameters.
    """
    logger.debug("Function Initialized")
    # 
    experience  = 0             # job experience
    job_age     = 1             # job post duration
    function_area_ids = [3,5,8] # Category of job
    # 
    try:
        base_url = "https://www.naukri.com/jobs-in-india"
        # 
        # Combine multiple functionAreaIdGid values
        fa_params = "&".join([f"functionAreaIdGid={i}" for i in function_area_ids])
        # 
        url = f"{base_url}?experience={experience}&jobAge={job_age}&{fa_params}"
        # 
        driver.get(url)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        # 
        logger.info(f"Jobs page opened | Title: {driver.title}")
    # 
    except Exception as e:
        logger.error(f"Error - openJobsPage | {e}", exc_info=True)
        # Instead of sys.exit, maybe retry or raise exception
        raise



def sortJobs(driver):
    """
    Sort jobs by given criteria ('date' or 'relevance')
    """
    logger.debug("Function Initialized")
    # 
    criteria='date'     # Sort Criteria
    # 
    try:
        wait = WebDriverWait(driver, 15)
        sort_btn = wait.until(EC.element_to_be_clickable((By.ID, "filter-sort")))
        sort_btn.click()
        # 
        if criteria == 'date':
            date_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-id='filter-sort-f']")))
            date_option.click()
        # 
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        logger.info(f"Jobs sorted by {criteria}")
    except Exception as e:
        logger.error(f"Error - sortJobs | {e}", exc_info=True)
        raise



def getJobLinks(driver):
    jobs = driver.find_elements(By.XPATH, "//a[contains(@class,'title')]")
    links = [job.get_attribute("href") for job in jobs if job.get_attribute("href")]
    logger.info(f"Job links found: {len(links)}")
    return links


def saveJobLinksToDB(job_links):
    for link in job_links:
        job_id = extract_naukri_job_id(link)
        if job_id:
            Job.objects.update_or_create(
                naukri_job_id=job_id,
                defaults={
                    "job_url": link,
                    "scrape_status": "pending"
                }
            )
            logger.info(f"Job saved | {job_id}")





def extract_job_id_and_link(driver):
    """
    Extract job_id and job_link from Naukri job cards
    Returns: list of dicts -> [{job_id, job_link}]
    """
    jobs_data = []
    # 
    job_cards = driver.find_elements(
        By.XPATH, "//div[contains(@class,'srp-jobtuple-wrapper') and @data-job-id]"
    )
    # 
    for card in job_cards:
        try:
            job_id = card.get_attribute("data-job-id")
            # 
            link_elem = card.find_element(By.XPATH, ".//a[contains(@class,'title')]")
            job_link = link_elem.get_attribute("href")
            # 
            if job_id and job_link:
                jobs_data.append({"job_id": job_id, "job_link": job_link})
        # 
        except Exception as e:
            logger.warning(f"Skipping job card due to error: {e}")
    # 
    logger.info(f"Extracted {len(jobs_data)} jobs")
    return jobs_data


def jobFinderWorker():
    driver =getDriver()
    openJobsPage(driver)
    sortJobs(driver)
    time.sleep(5)
    jobs_data = extract_job_id_and_link(driver)
    print(jobs_data)
    # driver = getDriver()
    # while True:
    #     try:
    #         openJobsPage(driver)
    #         links = getJobLinks(driver)
    #         saveJobLinksToDB(links)
    #         logger.info("All links processed | Sleeping before next page")
    #         time.sleep(random.uniform(10, 20))
    #     except Exception as e:
    #         logger.error(f"Job Finder Error | {e}", exc_info=True)
    #         time.sleep(5)