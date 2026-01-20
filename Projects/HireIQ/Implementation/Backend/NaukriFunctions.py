

import os
import time
import random

from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# -------------------------------------------------------------------------------------------------


def getCredentials(profile_number=2, verbose=False):
    """
    Load Naukri credentials from env file
    """
    print("Initialize Function - getCredentials") if verbose else None
    # 
    secrets_path = os.getenv("SECRETS_FILE")
    if not secrets_path:
        raise SystemExit("SECRETS_FILE environment variable is not set.")
    # 
    load_dotenv(dotenv_path=secrets_path, override=True)
    # 
    email = os.getenv("NAUKRI_EMAIL_" + str(profile_number))
    password = os.getenv("NAUKRI_PASSWORD_" + str(profile_number))
    # 
    if not email or not password:
        raise SystemExit("Naukri credentials not found in env file.")
    # 
    return email, password




# -------------------------------------------------------------------------------------------------


def getDriver(verbose=False):
    """
    Initialize Chrome WebDriver
    """
    print("Initialize Function - getDriver") if verbose else None
    # 
    options = Options()
    # 
    # Window behavior
    options.add_argument("--start-maximized")
    # 
    # 🔒 Anti-bot flags
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    # 
    # 🧠 Real browser user-agent
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
    # 
    # 
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver


# -------------------------------------------------------------------------------------------------


def autoLogin(driver, email, password, verbose=False):
    """
    Login to Naukri
    """
    print("Initialize Function - autoLogin") if verbose else None
    # 
    driver.get("https://www.naukri.com/nlogin/login")
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
        time.sleep(0.05)   # human typing
    # 
    password_input.clear()
    for ch in password:
        password_input.send_keys(ch)
        time.sleep(0.05)   # human typing
    # 
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    # 
    # wait for dashboard/home load
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    # 
    print("TITLE AFTER LOGIN:", driver.title)
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "nI-gNb-drawer"))
        )
        print("✅ Login successful")
    except:
        print("❌ Login failed or CAPTCHA triggered")
    # 
    if isCaptchaPresent(driver):
        print("🚨 CAPTCHA detected after login")
        driver.quit()
        raise SystemExit("Stopping bot due to CAPTCHA")




# -------------------------------------------------------------------------------------------------


def openJobsPage(driver, verbose=False):
    """
    Open job listing page
    """
    print("Initialize Function - openJobsPage") if verbose else None
    # 
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
    print("PAGE TITLE:", driver.title)


# -------------------------------------------------------------------------------------------------


def sortJobs(driver, verbose=False):
    """
    Sort jobs by Date
    """
    print("Initialize Function - sortJobs") if verbose else None
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
    print("Initialize Function - getJobLinks") if verbose else None
    # 
    jobs = driver.find_elements(
        By.XPATH, "//a[contains(@class,'title')]"
    )
    # 
    links = []
    for job in jobs:
        link = job.get_attribute("href")
        if link:
            links.append(link)
    # 
    print("JOBS FOUND:", len(links))
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
    print("Initialize Function - scrapeJobDetail") if verbose else None
    # 
    driver.get(url)
    # 
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    # 
    # scroll to ensure lazy-loaded content
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3)")
    time.sleep(2)
    # 
    job = {
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
        job["title"] = driver.find_element(By.TAG_NAME, "h1").text
    except:
        pass
    # 
    job["company"] = getCompany(driver)
    job["experience"] = getExperience(driver)
    job["salary"] = getSalary(driver)
    job["location"] = getLocation(driver)
    # 
    try:
        job["description"] = driver.find_element(
            By.XPATH,
            "//section[contains(@class,'job-desc')]"
        ).text
    except:
        pass
    # 
    return job


# -------------------------------------------------------------------------------------------------


def get_apply_type(driver):
    """
    Detect apply button type on job page
    """
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


def isChatbotPresent(driver):
    """
    Detect Naukri application chatbot popup
    """
    try:
        chatbot = driver.find_element(By.CLASS_NAME, "_chatBotContainer")
        return chatbot.is_displayed()
    except:
        return False


# -------------------------------------------------------------------------------------------------


def click_apply_button(driver):
    """
    Click apply button if allowed
    """
    if isCaptchaPresent(driver):
        print("🚨 CAPTCHA detected before apply")
        if not askUserInput() :
            return False
    # 
    apply_type = get_apply_type(driver)
    print("APPLY TYPE:", apply_type)
    # 
    if apply_type in ["APPLIED", "LOGIN_REQUIRED", "UNKNOWN"]:
        print("Skipping apply")
        return False
    # 
    try:
        if apply_type == "APPLY":
            btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "apply-button"))
            )
        # 
        elif apply_type in ["APPLY_ON_COMPANY_SITE", "WALKIN_INTERESTED"]:
            print("Manual apply required. Skipping.")
            return False
        # 
        else:
            return False
        # 
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", btn
        )
        time.sleep(random.uniform(4, 9))
        # 
        btn.click()
        time.sleep(4)  # allow chatbot to load
        # 
        # Check for chatbot
        if isChatbotPresent(driver):
            print("🤖 Chatbot detected — skipping this job")
            if not askUserInput():
                return False
        # 
        print("✅ Applied without chatbot")
        return True
    # 
    except Exception as e:
        print("❌ Failed to click apply:", e)
        return False


# -------------------------------------------------------------------------------------------------


def askUserInput():
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
