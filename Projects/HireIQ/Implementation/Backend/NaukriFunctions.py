
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# -------------------------------------------------------------------------------------------------


def getDriver(verbose=False):
    """
    """
    print("Initialize Function - getDriver") if verbose == True else None
    # 
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    # 
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver


# -----------------------------------------------


def autoLogin(driver, verbose=False):
    """
    """
    print("Initialize Function - autoLogin") if verbose == True else None
    # 
    driver.get("https://www.naukri.com/nlogin/login")
    # 
    WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "usernameField"))
    )
    # 
    email = "email@gmail.com"
    password = "passward@123"
    # 
    email_input = driver.find_element(By.ID, "usernameField")
    password_input = driver.find_element(By.ID, "passwordField")
    # 
    email_input.clear()
    for ch in email:
        email_input.send_keys(ch)
        time.sleep(0.05)
    # 
    password_input.clear()
    for ch in password:
        password_input.send_keys(ch)
        time.sleep(0.05)
    # 
    login_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
    login_btn.click()
    # 
    time.sleep(5)
    print("TITLE AFTER LOGIN:", driver.title)
    # 
    if "Dashboard" in driver.title or "Home" in driver.title:
        print("✅ Login successful")
    else:
        print("⚠️ Login status unclear — check manually")


# -----------------------------------------------


def openJobsPage(driver, verbose=False):
    """
    """
    print("Initialize Function - openJobsPage") if verbose == True else None
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
    time.sleep(5)
    print("PAGE TITLE:", driver.title)


# -----------------------------------------------


def sortJobs(driver, verbose=False):
    """
    """
    print("Initialize Function - sortJobs") if verbose == True else None
    # 
    wait = WebDriverWait(driver, 15)
    # 
    # Click sort dropdown
    sort_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "filter-sort"))
    )
    sort_btn.click()
    time.sleep(1)
    # 
    # Click Date option
    date_option = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@data-id='filter-sort-f']")
        )
    )
    date_option.click()
    # 
    time.sleep(5)


# -----------------------------------------------


def getJobLinks(driver, verbose=False):
    """
    """
    print("Initialize Function - getJobLinks") if verbose == True else None
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


# -----------------------------------------------


def safeText(driver, xpath, verbose=False):
    """
    """
    print("Initialize Function - safeText") if verbose == True else None
    # 
    try:
        return driver.find_element(By.XPATH, xpath).text.strip()
    except NoSuchElementException:
        return None


# -----------------------------------------------


def getExperience(driver, verbose=False):
    """
    """
    print("Initialize Function - getExperience") if verbose == True else None
    # 
    return safeText(
        driver, "//div[contains(@class,'exp__')]//span"
    )


def getSalary(driver, verbose=False):
    """
    """
    print("Initialize Function - getSalary") if verbose == True else None
    # 
    return safeText(
        driver, "//div[contains(@class,'salary__')]//span"
    )


def getLocation(driver, verbose=False):
    """
    """
    print("Initialize Function - getLocation") if verbose == True else None
    # 
    try:
        locations = driver.find_elements(
            By.XPATH, "//div[contains(@class,'loc_')]//a"
        )
        return ", ".join([loc.text for loc in locations])
    except:
        return None


def getCompany(driver, verbose=False):
    """
    """
    print("Initialize Function - getCompany") if verbose == True else None
    # 
    return safeText(
        driver,
        "//div[contains(@class,'jd-header-comp-name')]//a[1]"
    )


# -----------------------------------------------


def scrapeJobDetail(driver, url, verbose=False):
    """
    """
    print("Initialize Function - scrapeJobDetail") if verbose == True else None
    # 
    driver.get(url)
    time.sleep(4)
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
    job["company"] = getCompany(driver=driver, verbose=verbose)
    job["experience"] = getExperience(driver=driver, verbose=verbose)
    job["salary"] = getSalary(driver=driver, verbose=verbose)
    job["location"] = getLocation(driver=driver, verbose=verbose)
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

