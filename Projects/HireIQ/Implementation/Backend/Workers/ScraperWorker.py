
import sys
import time
import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from CompareResumeAndJobDescription import compareJob
from CompareResumeAndJobDescription import fetchGeminiAccessKey

from Functions.CommonFunctions import getDriver

# -------------------------------------------------------------------------------------------------

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# -------------------------------------------------------------------------------------------------

from core.Logger import get_logger
logger = get_logger("__name__")

# -------------------------------------------------------------------------------------------------

def openJobsPage(driver):
    """
    Open job listing page
    """
    logger.debug("Function Initialized")
    # 
    try:
        url = (
            "https://www.naukri.com/jobs-in-india"
            "?experience=0"
            "&jobAge=1"
            "&functionAreaIdGid=3"
            "&functionAreaIdGid=5"
            "&functionAreaIdGid=8"
        )
        # 
        driver.get(url)
        # 
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        # 
        logger.info(f"Jobs page opened    |    Title : {driver.title}")
    # 
    except Exception as e:
        logger.error(f"Error - openJobsPage | {e}", exc_info=True)
        sys.exit(1)


# -------------------------------------------------------------------------------------------------


def sortJobs(driver):
    """
    Sort jobs by Date
    """
    logger.debug("Function Initialized")
    # 
    wait = WebDriverWait(driver, 15)
    # 
    sort_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "filter-sort"))
    )
    sort_btn.click()
    time.sleep(random.uniform(1,3))
    # 
    date_option = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@data-id='filter-sort-f']")
        )
    )
    date_option.click()
    # 
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))


# -------------------------------------------------------------------------------------------------


def getJobLinks(driver):
    """
    Collect job URLs from listing page
    """
    logger.debug("Function Initialized")
    # 
    jobs = driver.find_elements(By.XPATH, "//a[contains(@class,'title')]")
    # 
    links = []
    for job in jobs:
        link = job.get_attribute("href")
        if link:
            links.append(link)
    # 
    logger.info(f"Jobs found: {len(links)}")
    return links


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
    except NoSuchElementException:
        return None


# -------------------------------------------------------------------------------------------------


def scrapeJobDetail(driver, url):
    """
    Scrape individual job details
    """
    logger.debug("Function Initialized")
    # 
    driver.get(url)
    # 
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    # 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3)")
    time.sleep(2)
    # 
    job_data_dict = {
        "url": url,
        "title": None,
        "company": None,
        "experience": None,
        "salary": None,
        "location": None,
        "description": None,
    }
    # 
    try:
        job_data_dict["title"] = driver.find_element(By.TAG_NAME, "h1").text
    except:
        logger.warning("Job title not found")
    # 
    job_data_dict["company"] = getCompany(driver)
    job_data_dict["experience"] = getExperience(driver)
    job_data_dict["salary"] = getSalary(driver)
    job_data_dict["location"] = getLocation(driver)
    # 
    try:
        job_data_dict["description"] = driver.find_element(
            By.XPATH, "//section[contains(@class,'job-desc')]"
        ).text
    except:
        logger.warning("Job description not found")
    # 
    logger.info("Job scraped successfully")
    return job_data_dict



# -------------------------------------------------------------------------------------------------


def processJobLinks(driver, job_links, api_key, relevant_job_queue):
    """
    Scrap and Compare job links
    """
    logger.debug("Function Initialized")
    # 
    try:
        for link in job_links:
            print()
            logger.info(f"Processing job link : {link}")
            job_data_dict = scrapeJobDetail(driver=driver, url=link)
            logger.info("Job details scraped successfully")
            # 
            # for k, v in job_data_dict.items():
            #     print(f"{k}: {v}")
            # 
            logger.info("Comparing Resume and Job ......................................")
            comparison_result = compareJob(api_key=api_key, job_description=str(job_data_dict))
            if comparison_result == 'True':
                logger.info("Similar")
                relevant_job_queue.put(link)
            # 
            # input("\nPress ENTER to open next job")
            print()
            logger.info("Moving to next job")
            # 
            # driver.back()
            # logger.info("Navigated back to job list")
            # sortJobs(driver=driver)
            # logger.info("Jobs re-sorted after navigation")
            # 
            time.sleep(random.uniform(8, 15))  # human reading time
        # 
        logger.info("All Jobs processed")
        return driver
    # 
    except Exception as e:
        logger.error(f"Error - processJobLinks | {e}", exc_info=True)
        sys.exit(1)


# -------------------------------------------------------------------------------------------------


def getRelevantJobLinks(driver, relevant_job_queue):
    """
    Driver 1 Task
    """
    logger.debug("Function Initialized")
    # 
    try:
        api_key = fetchGeminiAccessKey()
        logger.info(f"Gemini API key fetched    |    API Key : {api_key[-4:]}")
        # 
        openJobsPage(driver=driver)
        logger.info("Jobs page opened")
        time.sleep(random.uniform(1, 3))
        # 
        sortJobs(driver=driver)
        logger.info("Jobs sorted")
        time.sleep(random.uniform(1, 3))
        # 
        job_links = getJobLinks(driver=driver)
        logger.info(f"Job links fetched    |    Count : {len(job_links) if job_links else 0}")
        # 
        if not job_links:
            logger.critical("NO JOBS FOUND    |    Closing WebDriver")
            driver.quit()
            return
        # 
        processJobLinks(driver=driver, job_links=job_links, api_key=api_key, relevant_job_queue=relevant_job_queue)
        driver.quit()
        logger.info("WebDriver closed | Main execution completed")
    # 
    except Exception as e:
        logger.error(f"Error - getRelevantJobLinks | {e}", exc_info=True)
        sys.exit(1)


# -------------------------------------------------------------------------------------------------


def relevantJobWorker(relevant_job_queue):
    """
    fix issue - only i get job of page no 1
    """
    logger.debug("Function Initialized")
    # 
    driver = getDriver()
    # 
    while True:
        try:
            getRelevantJobLinks(driver=driver, relevant_job_queue=relevant_job_queue)
            time.sleep(15)
        except Exception as e:
            logger.error(f"Relevant Job Worker Error | {e}", exc_info=True)
            time.sleep(5)


# fix issue - only i get job of page no 1
