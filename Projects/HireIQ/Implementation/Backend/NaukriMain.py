
import time
import random

from NaukriFunctions import *
from CompareResumeAndJobDescription import *

# -----------------------------------------------

from Core.Logger import get_logger
logger = get_logger("hireiq.naukri.main")

# -----------------------------------------------

DRIVER = None

# -----------------------------------------------


def main(verbose=False):
    """
    Main execution flow
    """
    logger.info("Initialize Function - main") if verbose else None
    # 
    driver = getDriver(verbose=verbose)
    logger.info("WebDriver initialized")
    DRIVER = driver
    # 
    api_key = fetchGeminiAccessKey(verbose=verbose)
    logger.info(f"Gemini API key fetched    | API Key : {api_key[-5:]}")
    # 
    email, password = getCredentials(profile_number=2, verbose=verbose)
    logger.info("User credentials fetched")
    # autoLogin(driver=driver, email=email, password=password, verbose=verbose)
    time.sleep(random.uniform(4, 8))
    # 
    openJobsPage(driver=driver, verbose=verbose)
    logger.info("Jobs page opened")
    time.sleep(random.uniform(1, 3))
    # 
    sortJobs(driver=driver, verbose=verbose)
    logger.info("Jobs sorted")
    time.sleep(random.uniform(1, 3))
    # 
    input("\nPress ENTER to see jobs")
    logger.info("User requested to view job listings")
    # 
    job_links = getJobLinks(driver=driver, verbose=verbose)
    logger.info(f"Job links fetched | Count: {len(job_links) if job_links else 0}")
    # 
    if not job_links:
        logger.warning("No jobs found")
        driver.quit()
        logger.info("WebDriver closed")
        return
    # 
    for link in job_links:
        logger.info(f"Processing job link: {link}")
        job_data_dict = scrapeJobDetail(driver=driver, url=link, verbose=verbose)
        logger.info("Job details scraped successfully")
        # 
        # for k, v in job_data_dict.items():
        #     print(f"{k}: {v}")
        # 
        logger.info("Comparing Resume and Job ......................................")
        comparison_result = generateGeminiResponse(api_key=api_key, job_description=str(job_data_dict), verbose=verbose)
        logger.info(f"Comparison result received: {comparison_result}")
        if comparison_result == 'True':
            logger.info("Similar")
        # 
        input("\nPress ENTER to open next job")
        logger.info("Moving to next job")
        # 
        driver.back()
        logger.debug("Navigated back to job list")
        sortJobs(driver=driver, verbose=verbose)
        logger.debug("Jobs re-sorted after navigation")
        # 
        time.sleep(random.uniform(8, 15))  # human reading time
    # 
    driver.quit()
    logger.info("WebDriver closed | Main execution completed")


# -----------------------------------------------


if __name__ == "__main__":
    try:
        main(verbose=True)
    except SystemExit:
        pass


# applied = click_apply_button(driver)
#         if applied is False:
#             if isChatbotPresent(driver):
#                 print("➡️ Moving to next job")
#                 continue
#             # 
#             elif isCaptchaPresent(driver):
#                 print("🚨 CAPTCHA detected during job loop. Stopping.")
#                 break
        


# _________________________________________________________________________________________________

# Key skill HTML (star for essential skills)
# <div class="styles_key-skill__GIPn_">
# <div class="styles_heading__veHpg">Key Skills</div>
# <div class="styles_legend__DVbef">Skills highlighted with ‘<i class="ni-icon-jd-save"></i>‘ are preferred keyskills</div>
# <div><a href="https://www.naukri.com/php-jobs" target="_blank" class="styles_chip__7YCfG styles_clickable__dUW8S">
# <i class="ni-icon-jd-save"></i><span>PHP</span></a><a href="https://www.naukri.com/laravel-jobs" target="_blank" class="styles_chip__7YCfG styles_clickable__dUW8S">
# <i class="ni-icon-jd-save"></i><span>Laravel</span></a></div>
# <div><a href="https://www.naukri.com/css-jobs" target="_blank" class="styles_chip__7YCfG styles_clickable__dUW8S"><span>CSS</span></a>
# <a href="https://www.naukri.com/html-jobs" target="_blank" class="styles_chip__7YCfG styles_clickable__dUW8S"><span>HTML</span></a></div></div>


# <div id="_3i3hoibi1Footer" class="footerWrapper">
#     <div class="footerInputBoxWrapper">
#         <div id="_3i3hoibi1InputBox" class="chatbot_SendMessageContainer">
#             <div class="chatbot_InputContainer">
#                 <div class="textAreaWrapper">
#                 <div id="userInput__3i3hoibi1InputBox" class="textArea" contenteditable="true" data-placeholder="For example: 7 lakhs"></div>
#                 <span class="chatBot chatBot-add-round add-icon d-none p-events-none" id="add-icon__3i3hoibi1InputBox"></span>
#                 </div>
#             </div>
#         </div>
#     </div>
# </div>

# <div id="_3i3hoibi1Footer" class="footerWrapper">
#     <div class="footerInputBoxWrapper">
#         <div id="_3i3hoibi1InputBox" class="chatbot_SendMessageContainer">
#             <div class="chatbot_InputContainer">
#                 <div class="textAreaWrapper">
#                 <div id="userInput__3i3hoibi1InputBox" class="textArea" contenteditable="true" data-placeholder="Type message here..."></div>
#                 <span class="chatBot chatBot-add-round add-icon d-none p-events-none" id="add-icon__3i3hoibi1InputBox"></span>
#                 </div>
#             </div>
#         </div>
#     </div>
# </div>


# _________________________________________________________________________________________________


# def main(verbose=False):
#     """
#     """
#     print("Initialize Function - main") if verbose == True else None
#     # 
#     driver = getDriver(verbose=verbose)
#     # 
#     email, password = getCredentials(verbose=verbose)
#     autoLogin(driver=driver, email=email, password=password, verbose=verbose)
#     # 
#     openJobsPage(driver=driver, verbose=verbose)
#     # 
#     sortJobs(driver=driver, verbose=verbose)
#     # 
#     job_links = getJobLinks(driver=driver, verbose=verbose)
#     print(job_links) if verbose == True else None
#     # 
#     if not job_links:
#         print("No jobs found")
#         return
#     # 
#     # Scrape first job (for testing)
#     for link in job_links:
#         job_data_dict = scrapeJobDetail(driver=driver, url=link, verbose=verbose)
#         print("\nSCRAPED JOB DATA:") if verbose == True else None
#         for k, v in job_data_dict.items():
#             print(f"{k}: {v}") if verbose == True else None
#         # 
#         DRIVER = driver
#         input("\nPress ENTER to get_apply_type")
#         print(get_apply_type(driver))
#         # 
#         input("\nPress ENTER to click_apply_button")
#         click_apply_button(driver)
#         # 
#         input("\nPress ENTER to oprn new job")
#     # 
#     driver.quit()


# if __name__ == "__main__":
#     main(verbose=True)
