
import sys
import time
import random

from queue import Empty

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Functions.CommonFunctions import getDriver
from Functions.CommonFunctions import autoLogin
from Functions.CommonFunctions import getCredentials
from Functions.CommonFunctions import clickApplyButton
from Functions.CommonFunctions import getApplyType

# -------------------------------------------------------------------------------------------------

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# -------------------------------------------------------------------------------------------------

from core.Logger import get_logger
logger = get_logger("__name__")

# -------------------------------------------------------------------------------------------------


def applyJob(driver, job_link):
    """
    """
    logger.debug("Function Initialized")
    # 
    try:
        driver.get(job_link)
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(5)
        # 
        apply_type =  getApplyType(driver) 
        if apply_type == 'APPLY':
            # 
            clickApplyButton(driver)
            time.sleep(5)
            # 
            driver.get(job_link)
            # 
            if getApplyType(driver) ==  'APPLIED':
                return True
            else:
                logger.warning(f'Apply Status not change to APPLIED    |    Job Link : {job_link}')
                return False
        else:
            logger.error(f'Job Apply Button is not APPLY    |    Button Type : {apply_type}    |    Job Link : {job_link}')
            sys.exit(1)
    # 
    except Exception as e:
        logger.error(f"Error - processJobLinks | {e}", exc_info=True)
        sys.exit(1)


# -------------------------------------------------------------------------------------------------


MAX_RETRIES         = 3
APPLY_GAP_SECONDS   = 20   # 2 minutes
QUEUE_CHECK_SECONDS = 10  # 1 minute


def applyJobWorker(apply_job_queue):
    """
    - Check queue every 1 minute
    - Apply 1 job every 2 minutes
    - Retry each failed job up to 3 continuous times
    - Do NOT put failed job back in queue
    """
    logger.debug("Initialized Function")
    # 
    driver = getDriver()
    email, password = getCredentials(profile_number=1)
    logger.info("User credentials fetched")
    time.sleep(random.uniform(4, 8))
    # 
    autoLogin(driver=driver, email=email, password=password)
    # 
    last_apply_time = 0
    # 
    while True:
        try:
            # Wait for a job (check queue every 1 min)
            try:
                job_link = apply_job_queue.get(timeout=QUEUE_CHECK_SECONDS)
            except Empty:
                logger.info("Apply queue empty, waiting...")
                continue
            # 
            # Attempt this job up to MAX_RETRIES times consecutively
            attempt = 0
            while attempt < MAX_RETRIES:
                # Enforce 2-minute gap between applies
                elapsed = time.time() - last_apply_time
                if elapsed < APPLY_GAP_SECONDS:
                    sleep_time = APPLY_GAP_SECONDS - elapsed
                    logger.info(f"Waiting {sleep_time:.0f}s before next apply")
                    time.sleep(sleep_time)
                # 
                # Try applying
                response = applyJob(driver=driver, job_link=job_link)
                # 
                if response:
                    logger.info(f"Applied successfully: {job_link}")
                    last_apply_time = time.time()
                    break  # exit retry loop
                # 
                else:
                    attempt += 1
                    if attempt < MAX_RETRIES:
                        logger.warning(f"Apply failed    |    Retrying : {attempt}/{MAX_RETRIES}    |    Job Link : {job_link}")
                        # wait 2 minutes before next retry
                        time.sleep(APPLY_GAP_SECONDS)
                    else:
                        logger.error(f"Apply permanently failed after {MAX_RETRIES} attempts    |    Job Link : {job_link}")
            # 
            # Mark the job done in queue after all attempts
            apply_job_queue.task_done()
        # 
        except Exception as e:
            logger.error(f"Apply Job Worker Fatal Error | {e}", exc_info=True)
            time.sleep(30)


# -------------------------------------------------------------------------------------------------

# if __name__ == '__main__':
#     try:
#         from queue import Queue
#         apply_job_queue = Queue
#         apply_job_worker(apply_job_queue)
#     except SystemExit:
#         pass
