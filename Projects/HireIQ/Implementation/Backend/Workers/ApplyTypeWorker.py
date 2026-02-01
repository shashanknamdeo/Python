
import os
import sys
import time
import random

from queue import Empty

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# -------------------------------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

print("BASE_DIR =", BASE_DIR)

# -------------------------------------------------------------------------------------------------

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from jobs.models import Job
from django.db import transaction

# -------------------------------------------------------------------------------------------------

from core.Logger import get_logger
logger = get_logger("__name__")

# -------------------------------------------------------------------------------------------------

from Functions.CommonFunctions import getDriver
from Functions.CommonFunctions import autoLogin
from Functions.CommonFunctions import getCredentials
from Functions.CommonFunctions import clickApplyButton
from Functions.CommonFunctions import getApplyType

# -------------------------------------------------------------------------------------------------

def fetch_job_for_chatbot():
    """
    Fetch exactly ONE job that:
    - is scraped
    - chatbot not checked yet
    - lock-safe for multiple workers
    # 
    Returns:
        Job instance or None
    """
    with transaction.atomic():
        job = (
            Job.objects
            .select_for_update(skip_locked=True)
            .filter(
                scrape_status="done",
                resume_match=True,
                job_status="unknown"
            )
            .first()
        )
        # 
        if not job:
            return None
        # 
        job.chatbot_status = "processing"
        job.save(update_fields=["job_status"])
        # 
        return job


# -------------------------------------------------------------------------------------------------


def checkChatbot(driver):
    """
    Detect Naukri application chatbot popup
    """
    logger.debug("Function Initialized")
    # 
    try:
        chatbot = driver.find_element(By.CLASS_NAME, "_chatBotContainer")
        response = chatbot.is_displayed()
        logger.info("Chatbot Present")
        return True
    # 
    except NoSuchElementException:
        logger.info("Chatbot not found on page")
        return False


# -------------------------------------------------------------------------------------------------


def checkApplyButton(driver, job_link):
    """
    Returns:
    - "SAFE"
    - "CHATBOT"
    - "COMPANY_SITE"
    - "WALKIN"
    """
    logger.debug("Function Initialized")
    # 
    try:
        driver.get(job_link)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(5)
        # 
        apply_type = getApplyType(driver=driver)
        logger.info(f"Apply Type : {apply_type}")
        # 
        if apply_type == "APPLY":
            clickApplyButton(driver=driver)
            time.sleep(2)
            # 
            if checkChatbot(driver):
                return "CHATBOT"
            else:
                return "SAFE"
        # 
        if apply_type == "APPLY_ON_COMPANY_SITE":
            return "COMPANY_SITE"
        # 
        if apply_type == "WALKIN_INTERESTED":
            return "WALKIN"
        # 
        if apply_type == 'APPLIED':
            logger.warning('Apply Type : APPLIED')
            return 'APPLIED'
        # 
        if apply_type == "UNKNOWN" or apply_type == "LOGIN_REQUIRED" :
            logger.error(f'Error    |    Apply Type : {apply_type}')
            return 'ERROR'
        # 
        raise Exception(f"Error    |    Apply Type    |    getApplyType() - returns : {apply_type}")
    # 
    except Exception as e:
        logger.error(f"Error - checkApplyButton | {e}", exc_info=True)
        sys.exit(1)



# -------------------------------------------------------------------------------------------------


def save_chatbot_result(job, result, error=None):
    """
    Save chatbot detection result
    # 
    result values:
    - "SAFE"
    - "CHATBOT"
    - "COMPANY_SITE"
    - "WALKIN"
    - "FAILED"
    """
    if result == "SAFE":
        job.job_status = "APPLY"
    # 
    elif result in ("CHATBOT", "COMPANY_SITE", "WALKIN"):
        job.job_status = result
    # 
    else:
        job.job_status = "failed"
    # 
    if error:
        job.last_error = error
    # 
    job.save(
        update_fields=[
            "job_status",
            "last_error",
            "updated_at"
        ]
    )


def applyTypeWorker():
    """
    """
    logger.info("Chatbot worker started")
    # 
    job_idle_sleep_minutes = 5
    check_gap_seconds = 60
    # 
    idle_sleep_seconds = job_idle_sleep_minutes * 60
    # 
    driver = getDriver()
    # 
    email, password = getCredentials(profile_number=2)
    autoLogin(driver=driver, email=email, password=password)
    # 
    while True:
        job = None
        try:
            # 
            job = fetch_job_for_chatbot()
            # 
            if not job:
                logger.info(f'No pending jobs. Sleeping for {job_idle_sleep_minutes} minutes... ')
                time.sleep(idle_sleep_seconds)
                continue
            # 
            print()
            logger.info(f"Processing job    |    ID : {job.naukri_job_id}    |    Link : {job.job_url}")
            # 
            result = checkApplyButton(driver, job.job_url)
            # 
            save_chatbot_result(job, result)
            # 
            logger.info(f"Chatbot checked | JobID={job.naukri_job_id} | Result={result}")
            time.sleep(check_gap_seconds)
        # 
        except Exception as e:
            logger.error("Chatbot worker error", exc_info=True)
            # 
            if job:
                save_chatbot_result(job=job, result="FAILED", error=str(e))
            # 
            time.sleep(check_gap_seconds)


if __name__ == "__main__":
    applyTypeWorker()


# def checkApplyButton(driver, job_link, apply_job_queue):
#     """
#     """
#     logger.debug("Function Initialized")
#     # 
#     try:
#         driver.get(job_link)
#         WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
#         time.sleep(5)
#         # 
#         apply_type = getApplyType(driver=driver)
#         logger.info(f'Apply Type : {apply_type}')
#         # 
#         response = None
#         if apply_type == 'APPLY':
#             clickApplyButton(driver=driver)
#             time.sleep(2)
#             response = checkChatbot(driver=driver)
#             if response == False:
#                 apply_job_queue.put(job_link)
#                 logger.info('Job Link appended to APPLY_JOB_QUEUE')
#                 return True
#         # 
#         if response == True or apply_type == 'APPLY_ON_COMPANY_SITE':
#             logger.warning(f"Manual Apply Required    | Job link : {job_link}")
#             return True
#         # 
#         elif apply_type == 'WALKIN_INTERESTED':
#             logger.info('Walkin Job Apply')
#             return True
#         # 
#         else:
#             logger.error(f'Unexpected Error    |    Job Link : {job_link}')
#             raise Exception
#     # 
#     except Exception as e:
#         logger.error(f"Error - checkApplyButton | {e}", exc_info=True)
#         sys.exit(1)



# def processQueueItemWithRetry(driver, job_link, apply_job_queue):
#     """
#     Process ONE queue item with:
#     - continuous retries
#     - retry gap between attempts
#     - job gap before starting a new link
#     """
#     logger.debug('Function Initialized')
#     # 
#     last_job_time     = None
#     job_gap_seconds   = 10     # 1 minute between different job links
#     retry_gap_seconds = 10    # 2 minutes between retries (same job)
#     max_retries = 3
#     attempt = 1
#     # 
#     # Enforce gap between job links
#     if last_job_time is not None:
#         elapsed = time.time() - last_job_time
#         if elapsed < job_gap_seconds:
#             sleep_time = job_gap_seconds - elapsed
#             logger.info(f"Waiting {sleep_time:.0f}s before processing next job")
#             time.sleep(sleep_time)
#     # 
#     while attempt <= max_retries:
#         # 
#         response = checkApplyButton(driver=driver, job_link=job_link, apply_job_queue=apply_job_queue)
#         # 
#         if response:
#             logger.info(f"Job processed successfully    |    {job_link}")
#             return True
#         # 
#         if attempt < max_retries:
#             logger.warning(f"Apply failed    |    Retrying after {retry_gap_seconds}s    |    Attempt {attempt}/{max_retries}")
#             time.sleep(retry_gap_seconds)
#         # 
#         attempt += 1
#     # 
#     logger.error(f"Permanent failure after {max_retries} attempts | {job_link}")
#     return False




# def applyLinkCheckerWorker(relevant_job_queue, apply_job_queue):
#     """
#     Pulls jobs from relevant queue and pushes safe jobs to apply queue
#     """
#     logger.debug("Initialized ApplyLinkCheckerWorker")
#     # 
#     queue_check_seconds = 10   # how often workers check queue
#     # 
#     driver = getDriver()
#     # 
#     email, password = getCredentials(profile_number=2)
#     logger.info("User credentials fetched")
#     time.sleep(random.uniform(4, 8))
#     # 
#     autoLogin(driver=driver, email=email, password=password)
#     # 
#     while True:
#         try:
#             job_link = relevant_job_queue.get(timeout=queue_check_seconds)
#             # 
#             response = processQueueItemWithRetry( driver=driver, job_link=job_link, apply_job_queue=apply_job_queue)
#             # 
#             if response:
#                 apply_job_queue.put(job_link)
#             # 
#             relevant_job_queue.task_done()
#         # 
#         except Empty:
#             logger.info("Relevant job queue empty")
#             continue
#         # 
#         except Exception as e:
#             logger.error(f"ApplyLinkCheckerWorker Error | {e}", exc_info=True)
#             time.sleep(10)

# # store and use with CHATBOT_PRESENT and APPLY_ON_COMPANT_SITE apply

# # -------------------------------------------------------------------------------------------------