

import os
import sys
import time
import random
import requests

from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException


# -------------------------------------------------------------------------------------------------

from Core.Logger import get_logger

logger = get_logger("hireiq.naukri")

# -------------------------------------------------------------------------------------------------


def getCredentials(profile_number=2, verbose=False):
    """
    Load Naukri credentials from env file
    """
    logger.info("Initialize Function - getCredentials") if verbose else None
    # 
    secrets_path = os.getenv("SECRETS_FILE")
    if not secrets_path:
        logger.critical("SECRETS_FILE environment variable is not set.")
        raise SystemExit("SECRETS_FILE environment variable is not set.")
    # 
    load_dotenv(dotenv_path=secrets_path, override=True)
    # 
    email = os.getenv("NAUKRI_EMAIL_" + str(profile_number))
    password = os.getenv("NAUKRI_PASSWORD_" + str(profile_number))
    # 
    if not email or not password:
        logger.critical("Naukri credentials not found in env file.")
        raise SystemExit("Naukri credentials not found in env file.")
    # 
    logger.info("Credentials loaded successfully") if verbose else None
    return email, password





# -------------------------------------------------------------------------------------------------


def getDriver(verbose=False):
    """
    Initialize Chrome WebDriver
    """
    logger.info("Initialize Function - getDriver") if verbose else None
    # 
    try:
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        # 
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
        # 
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        # 
        logger.info("Chrome WebDriver initialized")
        return driver
    # 
    except Exception as e:
        logger.error(f"Error - getDriver | {e}", exc_info=True)
        sys.exit(1)


# -------------------------------------------------------------------------------------------------


def autoLogin(driver, email, password, verbose=False):
    """
    Login to Naukri
    """
    logger.info("Initialize Function - autoLogin") if verbose else None
    # 
    try:
        driver.get("https://www.naukri.com/nlogin/login")
        logger.debug("Login page opened")
        # 
        wait = WebDriverWait(driver, 15)
        wait.until(EC.presence_of_element_located((By.ID, "usernameField")))
        # 
        email_input = driver.find_element(By.ID, "usernameField")
        password_input = driver.find_element(By.ID, "passwordField")
        # 
        email_input.clear()
        for ch in email:
            email_input.send_keys(ch)
            time.sleep(0.1)
        # 
        password_input.clear()
        for ch in password:
            password_input.send_keys(ch)
            time.sleep(0.1)
        # 
        driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
        logger.debug("Login button clicked")
        # 
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "nI-gNb-drawer"))
        )
        # 
        logger.info("Login successful")
        # 
        if isCaptchaPresent(driver):
            logger.warning("CAPTCHA detected after login")
            driver.quit()
            raise SystemExit("Stopping bot due to CAPTCHA")
    # 
    except Exception as e:
        logger.error(f"Error - autoLogin | {e}", exc_info=True)
        sys.exit(1)


# -------------------------------------------------------------------------------------------------


def openJobsPage(driver, verbose=False):
    """
    Open job listing page
    """
    logger.info("Initialize Function - openJobsPage") if verbose else None
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
        logger.info(f"Jobs page opened | Title: {driver.title}")
    # 
    except Exception as e:
        logger.error(f"Error - openJobsPage | {e}", exc_info=True)
        sys.exit(1)



# -------------------------------------------------------------------------------------------------


def sortJobs(driver, verbose=False):
    """
    Sort jobs by Date
    """
    logger.info("Initialize Function - sortJobs") if verbose else None
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


def getJobLinks(driver, verbose=False):
    """
    Collect job URLs from listing page
    """
    logger.info("Initialize Function - getJobLinks") if verbose else None
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


def safeText(driver, xpath):
    """
    Safely extract text
    """
    try:
        return driver.find_element(By.XPATH, xpath).text.strip()
    except NoSuchElementException:
        return None


# -------------------------------------------------------------------------------------------------


def isCaptchaPresent(driver):
    """
    Detect CAPTCHA page
    """
    return "captcha" in driver.page_source.lower()


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


def scrapeJobDetail(driver, url, verbose=False):
    """
    Scrape individual job details
    """
    logger.info("Initialize Function - scrapeJobDetail") if verbose else None
    logger.debug(f"Scraping job URL: {url}")
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


def get_apply_type(driver, verbose=False):
    """
    Detect apply button type on job page
    """
    logger.info("Initialize Function - get_apply_type") if verbose else None
    # 
    mapping = {
        "already-applied": "APPLIED",
        "login-apply-button": "LOGIN_REQUIRED",
        "company-site-button": "APPLY_ON_COMPANY_SITE",
        "walkin-button": "WALKIN_INTERESTED",
        "apply-button": "APPLY"
    }
    # 
    for element_id, status in mapping.items():
        try:
            driver.find_element(By.ID, element_id)
            return status
        except NoSuchElementException:
            continue
    # 
    return "UNKNOWN"


# -------------------------------------------------------------------------------------------------


def isChatbotPresent(driver, verbose=False):
    """
    Detect Naukri application chatbot popup
    """
    logger.info("Initialize Function - isChatbotPresent") if verbose else None
    # 
    try:
        chatbot = driver.find_element(By.CLASS_NAME, "_chatBotContainer")
        return chatbot.is_displayed()
    except:
        return False


# -------------------------------------------------------------------------------------------------


def click_apply_button(driver, verbose=False):
    """
    Click apply button if allowed
    """
    logger.info("Initialize Function - click_apply_button") if verbose else None
    # 
    if isCaptchaPresent(driver):
        logger.warning("CAPTCHA detected before apply")
        if not getUserInput():
            return False
    # 
    apply_type = get_apply_type(driver)
    logger.info(f"Apply type detected: {apply_type}")
    # 
    if apply_type in ["APPLIED", "LOGIN_REQUIRED", "UNKNOWN"]:
        logger.info("Skipping apply")
        return False
    # 
    try:
        if apply_type == "APPLY":
            btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "apply-button"))
            )
        elif apply_type in ["APPLY_ON_COMPANY_SITE", "WALKIN_INTERESTED"]:
            logger.info("Manual apply required. Skipping.")
            return False
        else:
            return False
        # 
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", btn
        )
        time.sleep(random.uniform(4, 9))
        # 
        btn.click()
        time.sleep(4)
        # 
        if isChatbotPresent(driver):
            logger.warning("Chatbot detected — skipping this job")
            if not getUserInput():
                return False
        # 
        logger.info("Applied successfully without chatbot")
        return True
    # 
    except Exception as e:
        logger.error(f"Failed to click apply | {e}", exc_info=True)
        return False



# -------------------------------------------------------------------------------------------------


def getUserInput(verbose=False):
    """
    """
    logger.info("Initialize Function - getUserInput") if verbose else None
    # 
    while True:
        choice = input("Press C to continue or Q to quit: ").strip().lower()
        # 
        if choice == "c":
            print("Continuing the process...")
            return True
        # 
        elif choice == "q":
            print("Quitting the program. Goodbye!")
            return False
        # 
        else:
            print("Invalid input. Please press C or Q.")


# -------------------------------------------------------------------------------------------------


# import re

# def parseJobDescription(driver):
#     """
#     Parse job description section and convert to structured JSON
#     """
#     data = {
#         "overview": {},
#         "description_summary": None,
#         "responsibilities": [],
#         "eligibility": [],
#         "education": {},
#         "skills": [],
#         "raw_text": None
#     }
#     # 
#     # 1️⃣ Extract RAW text safely
#     try:
#         jd_container = driver.find_element(
#             By.CLASS_NAME, "styles_JDC__dang-inner-html__h0K4t"
#         )
#         raw_text = jd_container.text
#     except:
#         return data
#     # 
#     data["raw_text"] = raw_text
#     # 
#     lines = [l.strip() for l in raw_text.split("\n") if l.strip()]
#     # 
#     # 2️⃣ OVERVIEW extraction
#     for line in lines:
#         if "location" in line.lower():
#             data["overview"]["location"] = line.split(":", 1)[-1].strip()
#         # 
#         if "duration" in line.lower():
#             data["overview"]["duration"] = line.split(":", 1)[-1].strip()
#         # 
#         if "stipend" in line.lower() or "salary" in line.lower():
#             data["overview"]["stipend"] = line.split(":", 1)[-1].strip()
#         # 
#         if "vacancies" in line.lower():
#             nums = re.findall(r"\d+", line)
#             if nums:
#                 data["overview"]["vacancies"] = int(nums[0])
#         # 
#         if "intern" in line.lower() or "developer" in line.lower():
#             if "overview_title" not in data["overview"]:
#                 data["overview"]["title"] = line
#     # 
#     # 3️⃣ Responsibilities
#     capture = False
#     for line in lines:
#         if "responsibilit" in line.lower():
#             capture = True
#             continue
#         if capture:
#             if line.lower().startswith(("eligibility", "required", "skills")):
#                 capture = False
#             else:
#                 data["responsibilities"].append(line)
#     # 
#     # 4️⃣ Eligibility
#     capture = False
#     for line in lines:
#         if "eligibility" in line.lower():
#             capture = True
#             continue
#         if capture:
#             if line.lower().startswith(("required", "skills", "benefits")):
#                 capture = False
#             else:
#                 data["eligibility"].append(line)
#     # 
#     # 5️⃣ Description summary (first meaningful paragraph)
#     for line in lines:
#         if len(line) > 120:
#             data["description_summary"] = line
#             break
#     # 
#     # 6️⃣ Education (from structured section)
#     try:
#         edu_blocks = driver.find_elements(
#             By.XPATH, "//div[contains(@class,'styles_education')]//span"
#         )
#         if edu_blocks:
#             data["education"]["ug"] = edu_blocks[0].text
#             if len(edu_blocks) > 1:
#                 data["education"]["pg"] = edu_blocks[1].text
#     except:
#         pass
#     # 
#     # 7️⃣ Skills (most reliable)
#     try:
#         skill_elements = driver.find_elements(
#             By.XPATH, "//div[contains(@class,'styles_key-skill')]//span"
#         )
#         skills = list(set([s.text.strip() for s in skill_elements if s.text.strip()]))
#         data["skills"] = skills
#     except:
#         pass
#     # 
#     return data


# _________________________________________________________________________________________________


# import time

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException


# # -------------------------------------------------------------------------------------------------


# def getDriver(verbose=False):
#     """
#     """
#     print("Initialize Function - getDriver") if verbose == True else None
#     # 
#     options = Options()
#     options.add_argument("--start-maximized")
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     # 
#     driver = webdriver.Chrome(
#         service=Service(ChromeDriverManager().install()),
#         options=options
#     )
#     return driver


# # -----------------------------------------------


# def autoLogin(driver, email, password, verbose=False):
#     """
#     """
#     print("Initialize Function - autoLogin") if verbose == True else None
#     # 
#     driver.get("https://www.naukri.com/nlogin/login")
#     # 
#     WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.ID, "usernameField"))
#     )
#     # 
#     # email = "email@gmail.com"
#     # password = "passward@123"
#     # 
#     email_input = driver.find_element(By.ID, "usernameField")
#     password_input = driver.find_element(By.ID, "passwordField")
#     # 
#     email_input.clear()
#     for ch in email:
#         email_input.send_keys(ch)
#         time.sleep(0.05)
#     # 
#     password_input.clear()
#     for ch in password:
#         password_input.send_keys(ch)
#         time.sleep(0.05)
#     # 
#     login_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
#     login_btn.click()
#     # 
#     time.sleep(5)
#     print("TITLE AFTER LOGIN:", driver.title)
#     # 
#     if "Dashboard" in driver.title or "Home" in driver.title:
#         print("✅ Login successful")
#     else:
#         print("⚠️ Login status unclear — check manually")


# # -----------------------------------------------


# def openJobsPage(driver, verbose=False):
#     """
#     """
#     print("Initialize Function - openJobsPage") if verbose == True else None
#     # 
#     url = (
#         "https://www.naukri.com/jobs-in-india"
#         "?experience=0"
#         "&jobAge=1"
#         "&functionAreaIdGid=3"
#         "&functionAreaIdGid=5"
#         "&functionAreaIdGid=8"
#     )
#     # 
#     driver.get(url)
#     time.sleep(5)
#     print("PAGE TITLE:", driver.title)


# # -----------------------------------------------


# def sortJobs(driver, verbose=False):
#     """
#     """
#     print("Initialize Function - sortJobs") if verbose == True else None
#     # 
#     wait = WebDriverWait(driver, 15)
#     # 
#     # Click sort dropdown
#     sort_btn = wait.until(
#         EC.element_to_be_clickable((By.ID, "filter-sort"))
#     )
#     sort_btn.click()
#     time.sleep(1)
#     # 
#     # Click Date option
#     date_option = wait.until(
#         EC.element_to_be_clickable(
#             (By.XPATH, "//a[@data-id='filter-sort-f']")
#         )
#     )
#     date_option.click()
#     # 
#     time.sleep(5)


# # -----------------------------------------------


# def getJobLinks(driver, verbose=False):
#     """
#     """
#     print("Initialize Function - getJobLinks") if verbose == True else None
#     # 
#     jobs = driver.find_elements(
#         By.XPATH, "//a[contains(@class,'title')]"
#     )
#     # 
#     links = []
#     for job in jobs:
#         link = job.get_attribute("href")
#         if link:
#             links.append(link)
#     # 
#     print("JOBS FOUND:", len(links))
#     return links


# # -----------------------------------------------


# def safeText(driver, xpath, verbose=False):
#     """
#     """
#     print("Initialize Function - safeText") if verbose == True else None
#     # 
#     try:
#         return driver.find_element(By.XPATH, xpath).text.strip()
#     except NoSuchElementException:
#         return None


# # -----------------------------------------------


# def getExperience(driver, verbose=False):
#     """
#     """
#     print("Initialize Function - getExperience") if verbose == True else None
#     # 
#     return safeText(
#         driver, "//div[contains(@class,'exp__')]//span"
#     )


# def getSalary(driver, verbose=False):
#     """
#     """
#     print("Initialize Function - getSalary") if verbose == True else None
#     # 
#     return safeText(
#         driver, "//div[contains(@class,'salary__')]//span"
#     )


# def getLocation(driver, verbose=False):
#     """
#     """
#     print("Initialize Function - getLocation") if verbose == True else None
#     # 
#     try:
#         locations = driver.find_elements(
#             By.XPATH, "//div[contains(@class,'loc_')]//a"
#         )
#         return ", ".join([loc.text for loc in locations])
#     except:
#         return None


# def getCompany(driver, verbose=False):
#     """
#     """
#     print("Initialize Function - getCompany") if verbose == True else None
#     # 
#     return safeText(
#         driver,
#         "//div[contains(@class,'jd-header-comp-name')]//a[1]"
#     )


# # -----------------------------------------------


# def scrapeJobDetail(driver, url, verbose=False):
#     """
#     """
#     print("Initialize Function - scrapeJobDetail") if verbose == True else None
#     # 
#     driver.get(url)
#     time.sleep(4)
#     # 
#     job = {
#         "url": url,
#         "title": None,
#         "company": None,
#         "experience": None,
#         "salary": None,
#         "location": None,
#         "description": None,
#     }
#     # 
#     try:
#         job["title"] = driver.find_element(By.TAG_NAME, "h1").text
#     except:
#         pass
#     # 
#     job["company"] = getCompany(driver=driver, verbose=verbose)
#     job["experience"] = getExperience(driver=driver, verbose=verbose)
#     job["salary"] = getSalary(driver=driver, verbose=verbose)
#     job["location"] = getLocation(driver=driver, verbose=verbose)
#     # 
#     try:
#         job["description"] = driver.find_element(
#             By.XPATH,
#             "//section[contains(@class,'job-desc')]"
#         ).text
#     except:
#         pass
#     # 
#     return job

# import os
# from dotenv import load_dotenv

# from NaukriFunctions import *

# # -----------------------------------------------

# DRIVER = None

# # -----------------------------------------------


# def getCredentials(verbose=False):
#     """
#     """
#     print("Initialize Function - getCredentials") if verbose == True else None
#     # get path from environment variable (Windows)
#     secrets_path = os.getenv("SECRETS_FILE")
#     if not secrets_path:
#         raise SystemExit("SECRETS_FILE environment variable is not set.")
#     # 
#     # load the file into the process environment
#     load_dotenv(dotenv_path=secrets_path, override=False)
#     # 
#     # now access secrets via os.getenv
#     email = os.getenv("NAUKRI_EMAIL")
#     password = os.getenv("NAUKRI_password")
#     print(email, password)
#     return email, password


# # -----------------------------------------------


# def get_apply_type(driver):
#     """
#     """
#     try:
#         driver.find_element(By.ID, "already-applied")
#         return "APPLIED"
#     except NoSuchElementException:
#         print('NoSuchElementException - APPLIED')
#         pass
#     # 
#     try:
#         driver.find_element(By.ID, "login-apply-button")
#         return "LOGIN_REQUIRED"
#     except NoSuchElementException:
#         print('NoSuchElementException - LOGIN_REQUIRED')
#         pass
#     # 
#     try:
#         driver.find_element(By.ID, "company-site-button")
#         return "APPLY_ON_COMPANY_SITE"
#     except NoSuchElementException:
#         print('NoSuchElementException - APPLY_ON_COMPANY_SITE')
#         pass
#     # 
#     try:
#         driver.find_element(By.ID, "walkin-button")
#         return "WALKIN_INTERESTED"
#     except NoSuchElementException:
#         print('NoSuchElementException - WALKIN_INTERESTED')
#         pass
#     # 
#     try:
#         driver.find_element(By.ID, "apply-button")
#         return "APPLY"
#     except NoSuchElementException:
#         print('NoSuchElementException - APPLY')
#         pass
#     # 
#     raise ValueError("No element found name - (already-applied, login-apply-button, company-site-button, walkin-button, apply-button)")


# # -----------------------------------------------


# import time

# def click_apply_button(driver):
#     """
#     """
#     apply_type = get_apply_type(driver)
#     print("APPLY TYPE:", apply_type)
#     # 
#     if apply_type in ["APPLIED", None]:
#         print("Already applied")
#         return False
#     # 
#     if apply_type == "LOGIN_REQUIRED":
#         print("⚠ Login required. Skipping.")
#         return False
#     # 
#     try:
#         if apply_type == "APPLY":
#             btn = driver.find_element(By.ID, "apply-button")
#         # 
#         elif apply_type == "APPLY_ON_COMPANY_SITE":
#             print("Can not click apply_type -> APPLY_ON_COMPANY_SITE")
#             # btn = driver.find_element(By.ID, "company-site-button")
#             return False
#         # 
#         elif apply_type == "WALKIN_INTERESTED":
#             print("Can not click apply_type -> WALKIN_INTERESTED")
#             # btn = driver.find_element(By.ID, "walkin-button")
#             return False
#         # 
#         else:
#             raise ValueError("No element found name - (already-applied, login-apply-button, company-site-button, walkin-button, apply-button)")
#         # 
#         driver.execute_script("arguments[0].scrollIntoView({block:'center'});", btn)
#         time.sleep(1)
#         btn.click()
#         time.sleep(5)
#         # 
#         print("✅ Clicked apply button")
#         # 
#         return True
#     # 
#     except Exception as e:
#         print("❌ Failed to click apply:", e)
#         return False
