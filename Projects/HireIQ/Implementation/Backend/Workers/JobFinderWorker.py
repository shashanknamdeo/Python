import os
import re
import math
import sys
import time
import random
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# -----------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

print("BASE_DIR =", BASE_DIR)

# -----------------------------------------------

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from jobs.models import Job   # adjust app name if different

# -----------------------------------------------

# from core.Logger import get_logger

# logger = get_logger("__name__")

# -----------------------------------------------

# from Functions.CommonFunctions import getDriver
# from Functions.CommonFunctions import extract_naukri_job_id

# -----------------------------------------------


# def get_total_pages(driver, jobs_per_page=20):
#     """
#     Extract total job count and calculate total pages
#     """
#     logger.debug('Function Initialized')
#     # 
#     wait = WebDriverWait(driver, 15)
#     # 
#     count_elem = wait.until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "span.styles_count-string__DlPaZ")))
#     # 
#     text = count_elem.get_attribute("title")  # "1 - 20 of 88"
#     match = re.search(r"of\s+(\d+)", text)
#     # 
#     if not match:
#         logger.warning("Could not detect total job count, defaulting to 1 page")
#         return 1
#     # 
#     total_jobs = int(match.group(1))
#     total_pages = math.ceil(total_jobs / jobs_per_page)
#     # 
#     logger.info(f"Total jobs: {total_jobs}, Total pages: {total_pages}")
#     # 
#     return total_pages


# def openJobsPage(driver, page=1):
#     """
#     https://www.naukri.com/jobs-in-india?experience=0&jobAge=1&functionAreaIdGid=3&functionAreaIdGid=5&functionAreaIdGid=8
#     """
#     logger.debug("Function Initialized")
#     # 
#     experience  = 0
#     job_age     = 1
#     function_area_ids = [3, 5, 8]
#     # 
#     try:
#         base_url = "https://www.naukri.com/jobs-in-india"
#         fa_params = "&".join([f"functionAreaIdGid={i}" for i in function_area_ids])
#         # 
#         if page == 1:
#             url = f"{base_url}?experience={experience}&jobAge={job_age}&{fa_params}"
#         else:
#             url = f"{base_url}-{page}?experience={experience}&jobAge={job_age}&{fa_params}"
#         # 
#         driver.get(url)
#         # 
#         WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
#         # 
#         logger.info(f"Opened page {page} | Title: {driver.title}")
#     # 
#     except Exception as e:
#         logger.error(f"Error - openJobsPage | {e}", exc_info=True)
#         raise


# def sortJobs(driver):
#     """
#     Sort jobs by given criteria ('date' or 'relevance')
#     """
#     logger.debug("Function Initialized")
#     # 
#     criteria='date'     # Sort Criteria
#     # 
#     try:
#         wait = WebDriverWait(driver, 15)
#         sort_btn = wait.until(EC.element_to_be_clickable((By.ID, "filter-sort")))
#         sort_btn.click()
#         # 
#         if criteria == 'date':
#             date_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-id='filter-sort-f']")))
#             date_option.click()
#         # 
#         wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
#         logger.info(f"Jobs sorted by {criteria}")
#     except Exception as e:
#         logger.error(f"Error - sortJobs | {e}", exc_info=True)
#         raise


# def go_to_next_page(driver):
#     """
#     Clicks the 'Next' button to go to the next page.
#     Returns True if successful, False if no next page exists.
#     """
#     try:
#         next_btn = driver.find_element(
#             By.XPATH, "//a[contains(@class,'styles_btn-secondary__2AsIP') and contains(., 'Next')]"
#         )
#         next_btn.click()
#         time.sleep(random.uniform(3, 5))  # human-like pause
#         logger.info("Navigated to next page")
#         return True
#     except Exception:
#         logger.info("No Next button found or last page reached")
#         return False


# def extract_job_id_and_link(driver):
#     """
#     Extract job_id and job_link from Naukri job cards
#     Returns: list of dicts -> [{job_id, job_link}]
#     """
#     jobs_data = []
#     # 
#     job_cards = driver.find_elements(
#         By.XPATH, "//div[contains(@class,'srp-jobtuple-wrapper') and @data-job-id]"
#     )
#     # 
#     for card in job_cards:
#         try:
#             job_id = card.get_attribute("data-job-id")
#             # 
#             link_elem = card.find_element(By.XPATH, ".//a[contains(@class,'title')]")
#             job_link = link_elem.get_attribute("href")
#             # 
#             if job_id and job_link:
#                 jobs_data.append({"job_id": job_id, "job_link": job_link})
#         # 
#         except Exception as e:
#             logger.warning(f"Skipping job card due to error: {e}")
#     # 
#     logger.info(f"Extracted {len(jobs_data)} jobs")
#     return jobs_data


# def save_jobs_to_db(jobs_data):
#     """
#     Save scraped job_id and job_link into database.
#     Avoid duplicates using unique constraints.
#     """
#     logger.info('Function Initialized')
#     # 
#     saved = 0
#     skipped = 0
#     # 
#     for i, job in enumerate(jobs_data, start=1):
#         logger.info(f"Saving job {i}/{len(jobs_data)} | job_id={job['job_id']}")
#         # 
#         try:
#             obj, created = Job.objects.get_or_create(
#                 naukri_job_id=int(job["job_id"]),
#                 defaults={
#                     "job_url": job["job_link"],
#                     # "scrape_status": "pending",
#                     # "chatbot_status": "unknown",
#                     # "apply_status": "pending",
#                 }
#             )
#             # 
#             if created:
#                 saved += 1
#             else:
#                 skipped += 1
#         # 
#         except Exception as e:
#             logger.error(
#                 f"DB error for job_id={job['job_id']} | {e}",
#                 exc_info=True
#             )
#     # 
#     logger.info(f"Jobs saved: {saved}, skipped(existing): {skipped}")



# def jobFinderWorker():
#     """
#     """
#     logger.info('Function Initialized')
#     # 
#     driver = getDriver()
#     # 
#     try:
#         openJobsPage(driver)
#         sortJobs(driver)
#         time.sleep(5)
#         # 
#         jobs_data = extract_job_id_and_link(driver)
#         # 
#         if jobs_data:
#             save_jobs_to_db(jobs_data)
#     # 
#     except Exception as e:
#         logger.critical(f"JobFinderWorker failed | {e}", exc_info=True)
#     # 
#     finally:
#         driver.quit()


# def jobFinderWorker():
#     """
#     Crawl all jobs using 'Next' button with known total pages.
#     """
#     logger.info("JobFinderWorker Initialized")
#     # 
#     job_idle_sleep_minutes = 5
#     next_page_idle_seconds = 10
#     # 
#     idle_sleep_seconds = job_idle_sleep_minutes * 60
#     # 
#     driver = getDriver()
#     # 
#     try:
#         while True:
#             # 
#             # Open first page and sort
#             openJobsPage(driver, page=1)
#             sortJobs(driver)
#             time.sleep(3)
#             # 
#             # Get total pages from first page
#             total_pages = get_total_pages(driver)
#             logger.info(f"Total pages detected: {total_pages}")
#             # 
#             # Loop through pages
#             for page in range(1, total_pages + 1):
#                 print()
#                 time.sleep(next_page_idle_seconds)
#                 # 
#                 logger.info(f"Scraping page {page}/{total_pages}")
#                 jobs_data = extract_job_id_and_link(driver)
#                 if jobs_data:
#                     save_jobs_to_db(jobs_data)
#                 else:
#                     logger.info("No jobs found on this page")
#                 # 
#                 # Go to next page if not the last one
#                 if page < total_pages:
#                     success = go_to_next_page(driver)
#                     if not success:
#                         logger.warning("Cannot navigate to next page, stopping crawl")
#                         break
#                 # 
#             logger.info(f"No pending jobs. Sleeping for {job_idle_sleep_minutes} minutes...")
#             time.sleep(idle_sleep_seconds)
#     # 
#     except Exception as e:
#         logger.critical(f"JobFinderWorker failed | {e}", exc_info=True)
#     finally:
#         driver.quit()
#         logger.info("WebDriver closed | JobFinderWorker completed")


def jobFinderWorker():
    """
    """
    for i in range(1, 21):
        print(f'This is job {i}')
        time.sleep(2)
        # return True


if __name__ == "__main__":
    jobFinderWorker()


# pick jobs from database
# Job.objects.filter(scrape_status="pending")

# -----------------------------------------------

# when scraping job details:
# job.scrape_status = "done"
# job.save(update_fields=["scrape_status"])

# If error:
# job.scrape_status = "error"
# job.last_error = str(e)
# job.save(update_fields=["scrape_status", "last_error"])