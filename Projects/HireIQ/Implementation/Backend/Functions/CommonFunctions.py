

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

from core.Logger import get_logger
logger = get_logger("__name__")

# -------------------------------------------------------------------------------------------------


def getCredentials(profile_number=2):
    """
    Load Naukri credentials from env file
    """
    logger.debug("Function Initialized")
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
    logger.info("Naukri Credentials Extracted successfully")
    return email, password


# -------------------------------------------------------------------------------------------------


def getDriver():
    """
    Initialize Chrome WebDriver
    """
    logger.debug("Function Initialized")
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


def autoLogin(driver, email, password):
    """
    Login to Naukri
    """
    logger.debug("Function Initialized")
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
        return True
    # 
    except Exception as e:
        logger.error(f"Error - autoLogin | {e}", exc_info=True)
        sys.exit(1)


# -------------------------------------------------------------------------------------------------


def isCaptchaPresent(driver):
    """
    Detect CAPTCHA page
    """
    return "captcha" in driver.page_source.lower()


# -------------------------------------------------------------------------------------------------


def getApplyType(driver):
    """
    Detect apply button type on job page
    """
    logger.debug("Function Initialized")
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


def clickApplyButton(driver):
    """
    Click apply button if allowed
    """
    logger.debug("Function Initialized")
    # 
    try:
        btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "apply-button"))
        )
        # 
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", btn
        )
        time.sleep(random.uniform(4, 9))
        # 
        btn.click()
        # 
        logger.info("Applied Clicked")
        return True
    # 
    except Exception as e:
        logger.error(f"Error - processJobLinks | {e}", exc_info=True)
        sys.exit(1)


# -------------------------------------------------------------------------------------------------

import re

def extract_naukri_job_id(url: str) -> int:
    match = re.search(r"-([0-9]{12})\?", url)
    return int(match.group(1)) if match else None
