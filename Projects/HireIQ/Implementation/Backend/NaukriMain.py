

import time
import random

from NaukriFunctions import *


# -----------------------------------------------

DRIVER = None

# -----------------------------------------------


def main(verbose=False):
    """
    Main execution flow
    """
    print("Initialize Function - main") if verbose else None
    # 
    driver = getDriver(verbose=verbose)
    DRIVER = driver
    # 
    email, password = getCredentials(profile_number=2, verbose=verbose)
    autoLogin(driver=driver, email=email, password=password, verbose=verbose)
    time.sleep(random.uniform(4, 8))
    # 
    openJobsPage(driver=driver, verbose=verbose)
    time.sleep(random.uniform(1, 3))
    # 
    sortJobs(driver=driver, verbose=verbose)
    time.sleep(random.uniform(1, 3))
    # 
    input("\nPress ENTER to see jobs")
    # 
    job_links = getJobLinks(driver=driver, verbose=verbose)
    # 
    if not job_links:
        print("No jobs found")
        driver.quit()
        return
    # 
    for link in job_links:
        job_data = scrapeJobDetail(driver=driver, url=link, verbose=verbose)
        # 
        print("\nSCRAPED JOB DATA:")
        for k, v in job_data.items():
            print(f"{k}: {v}")
        # 
        input("\nPress ENTER to check apply type")
        print(get_apply_type(driver))
        # 
        input("\nPress ENTER to attempt apply")
        # 
        applied = click_apply_button(driver)
        if applied is False:
            if isChatbotPresent(driver):
                print("➡️ Moving to next job")
                continue
            # 
            elif isCaptchaPresent(driver):
                print("🚨 CAPTCHA detected during job loop. Stopping.")
                break
        # 
        input("\nPress ENTER to open next job")
        # 
        time.sleep(random.uniform(8, 15))  # human reading time
    # 
    driver.quit()


# -----------------------------------------------


if __name__ == "__main__":
    main(verbose=True)


# _________________________________________________________________________________________________


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
#         job_data = scrapeJobDetail(driver=driver, url=link, verbose=verbose)
#         print("\nSCRAPED JOB DATA:") if verbose == True else None
#         for k, v in job_data.items():
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
