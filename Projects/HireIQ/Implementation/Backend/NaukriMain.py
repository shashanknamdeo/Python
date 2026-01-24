
import sys
import time
import threading

from queue import Queue

from Functions.CommonFunctions import getDriver
# from Functions.Driver1Functions import relevantJobWorker
# from Functions.Driver2Functions import applyLinkCheckerWorker
# from Functions.Driver3Functions import applyJobWorker
from Workers.JobFinderWorker import jobFinderWorker

# -----------------------------------------------

from core.Logger import get_logger
logger = get_logger("hireiq.naukri.main")

# -----------------------------------------------

RELEVANT_JOB_QUEUE  = Queue(maxsize=200)
APPLY_JOB_QUEUE     = Queue(maxsize=50)

# -----------------------------------------------


# def main():
#     logger.debug("Function Initialized")
#     # 
#     try:
#         threads = []
#         # 
#         # Thread-1: Fetch relevant jobs (anonymous)
#         t1 = threading.Thread( target=relevantJobWorker, args=(RELEVANT_JOB_QUEUE), name="RelevantJobThread", daemon=True )
#         threads.append(t1)
#         # 
#         # Thread-2: Check apply + chatbot (secondary ID)
#         t2 = threading.Thread( target=apply_link_checker_worker, args=(RELEVANT_JOB_QUEUE, APPLY_JOB_QUEUE), name="ApplyCheckerThread", daemon=True )
#         threads.append(t2)
#         # 
#         # Thread-3: Apply jobs (primary ID)
#         t3 = threading.Thread( target=apply_job_worker, arg=(APPLY_JOB_QUEUE), name="ApplyJobThread", daemon=True )
#         threads.append(t3)
#         # 
#         for t in threads:
#             t.start()
#         # 
#         # Keep main thread alive
#         while True:
#             time.sleep(1)
#         # 
#     except KeyboardInterrupt:
#         logger.warning("Shutting down system...")
#         sys.exit(0)
#     # 
#     except Exception as e:
#         logger.error(f"Fatal Error | {e}", exc_info=True)
#         sys.exit(1)

def main():
    logger.debug("Function Initialized")
    # RELEVANT_JOB_QUEUE.put('https://www.naukri.com/job-listings-gtm-operations-associate-valorega-talentedge-greater-noida-0-to-5-years-261225027985?src=cluster&sid=17691567362867212_1&xp=1&px=1&nignbevent_src=jobsearchDeskGNB')
    # RELEVANT_JOB_QUEUE.put('https://www.naukri.com/job-listings-sr-mis-executive-amcc-new-delhi-3-to-5-years-130126914636?src=simjobsjd_bottom')
    # relevantJobWorker(relevant_job_queue=RELEVANT_JOB_QUEUE)
    # input('Press Enter to check Chatbot')
    # applyLinkCheckerWorker(relevant_job_queue=RELEVANT_JOB_QUEUE, apply_job_queue=APPLY_JOB_QUEUE)
    # input('Press Enter to Apply')
    # APPLY_JOB_QUEUE.put('https://www.naukri.com/job-listings-cloud-engineer-alactic-inc-gurugram-0-to-2-years-230126025875')
    # applyJobWorker(apply_job_queue=APPLY_JOB_QUEUE)
    jobFinderWorker()

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
