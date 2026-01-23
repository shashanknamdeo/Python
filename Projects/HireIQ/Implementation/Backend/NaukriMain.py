
import sys
import time
import random

from Functions.Driver1Functions import getRelevantJobLinks
from Functions.CommonFunctions import getDriver

# -----------------------------------------------

from Core.Logger import get_logger
logger = get_logger("hireiq.naukri.main")

# -----------------------------------------------

DRIVER_1 = None

# -----------------------------------------------


def main():
    """
    """
    logger.debug("Initialize Function - main")
    # 
    try:
        driver_1 = getDriver()
        DRIVER_1 = driver_1
        logger.info("driver_1 Initialized")
        getRelevantJobLinks(driver=driver_1)
    # 
    except Exception as e:
        logger.error(f"Error - main | {e}", exc_info=True)
        sys.exit(1)

# -----------------------------------------------


if __name__ == "__main__":
    try:
        main()
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
