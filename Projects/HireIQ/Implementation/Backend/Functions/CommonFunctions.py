

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
    except Exception as e:
        logger.error(f"Error - autoLogin | {e}", exc_info=True)
        sys.exit(1)


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





# -------------------------------------------------------------------------------------------------











# -------------------------------------------------------------------------------------------------


def getUserInput():
    """
    """
    logger.info("Function Initialized")
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
