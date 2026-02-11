
import os
import sys
# import time
# import random

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

# # -------------------------------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

print("BASE_DIR =", BASE_DIR)

# # -------------------------------------------------------------------------------------------------

# import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
# django.setup()

# from django.db import transaction, close_old_connections
# from jobs.models import Job

# # -------------------------------------------------------------------------------------------------

# from core.Logger import get_logger
# logger = get_logger("__name__")

# # -------------------------------------------------------------------------------------------------

# from Functions.CommonFunctions import getDriver

# # -------------------------------------------------------------------------------------------------

# import time
# import random
# import pyperclip
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import StaleElementReferenceException

# def human_typing(element, text, delay=0.08):
#     for ch in text:
#         element.send_keys(ch)
#         time.sleep(delay + random.uniform(0.01, 0.04))


# def get_active_textarea(driver):
#     """
#     Returns the last visible textarea.ITIRGe
#     (Google keeps old ones hidden in DOM)
#     """
#     textareas = driver.find_elements(By.CSS_SELECTOR, "textarea.ITIRGe")

#     for ta in reversed(textareas):
#         if ta.is_displayed():
#             return ta

#     raise Exception("No visible textarea found")


# def get_send_button(driver):
#     """
#     Always click the real BUTTON, not SVG div
#     """
#     buttons = driver.find_elements(By.CSS_SELECTOR, "button[aria-label='Send']")

#     for btn in buttons:
#         if btn.is_displayed() and btn.is_enabled():
#             return btn

#     raise Exception("Send button not found")


def read_multiline_input(end_word="END"):
    print(f"Enter your prompt (type '{end_word}' on a new line to finish):")
    lines = []
    # 
    while True:
        line = input()
        if line.strip() == end_word:
            break
        lines.append(line)
    # 
    return "\n".join(lines)


# def ask_question_on_search(driver, typing_delay=0.08):
#     driver.get("https://www.google.com/search?sourceid=chrome&udm=50&aep=42")
#     # 
#     wait = WebDriverWait(driver, 30)
#     # 
#     # wait for first textarea to exist
#     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ITIRGe")))
#     # 
#     try :
#         textarea = get_active_textarea(driver)
#         textarea.click()
#         # 
#         textarea.send_keys('I want that You Must Response the Upcomming Request in such a format so that i can COPY THE RESPONSE IN JUST ONE CLICK')
#         time.sleep(0.5)
#         send_btn = get_send_button(driver)
#         send_btn.click()
#     except Exception as e:
#         print(e)
#     # 
#     while True:
#         question = read_multiline_input()
#         if not question:
#             continue
#         # 
#         try:
#             # 🔹 Always re-locate fresh textarea
#             textarea = get_active_textarea(driver)
#             textarea.click()
#             time.sleep(0.3)
#             # 
#             for line in question.split("\n"):
#                 textarea.send_keys(line)
#                 textarea.send_keys(Keys.SHIFT, Keys.ENTER)
#                 # time.sleep(typing_delay)
#             # 
#             time.sleep(2)
#             # 
#             send_btn = get_send_button(driver)
#             send_btn.click()
#             # 
#             time.sleep(5)
#             # 
#             copy_buttons = wait.until(
#                 EC.presence_of_all_elements_located(
#                     (By.XPATH, "//button[@aria-label='Copy code text to clipboard.']")
#                 )
#             )
#             # 
#             copy_button = copy_buttons[-1]
#             # 
#             driver.execute_script(
#                 "arguments[0].scrollIntoView({block: 'center'});",
#                 copy_button
#             )
#             # 
#             copy_button.click()
#             # 
#             response = pyperclip.paste()
#             # 
#             return response
#         # 
#         except Exception as e:
#             print(e)



# if __name__ == '__main__':
#     ai_client = getDriver()
#     try:
#         ask_question_on_search(driver=driver, typing_delay=0.1)
#     except Exception as e:
#         print(e)
#     input('Press Enter to End')

# """
# I can definitely do that for you! 
# I will structure the data according to the JSON Resume standard, 
# which is the most widely supported format for generating PDFs through tools like the 
# JSON Resume CLI or Reactive Resume.
# """


from GenAI import gen_ai_client

client = gen_ai_client()

while True:
    try:
        question = read_multiline_input()
        print(question)
        response = client.generate(question)
        print(response)
    except Exception as e:
        print(Exception)

client.close()