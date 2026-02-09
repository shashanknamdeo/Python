import time
import random
import pyperclip

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Functions.CommonFunctions import getDriver


class gen_ai_client:
    def __init__(self, typing_delay=0.08):
        self.typing_delay = typing_delay
        self.driver = getDriver()
        self.wait = WebDriverWait(self.driver, 30)

        self._open_gemini()
        self._initialize_behavior()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _open_gemini(self):
        self.driver.get("https://www.google.com/search?sourceid=chrome&udm=50&aep=42")
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ITIRGe"))
        )

    def _get_active_textarea(self):
        textareas = self.driver.find_elements(By.CSS_SELECTOR, "textarea.ITIRGe")
        for ta in reversed(textareas):
            if ta.is_displayed():
                return ta
        raise Exception("No visible textarea found")

    def _get_send_button(self):
        buttons = self.driver.find_elements(By.CSS_SELECTOR, "button[aria-label='Send']")
        for btn in buttons:
            if btn.is_displayed() and btn.is_enabled():
                return btn
        raise Exception("Send button not found")

    def _initialize_behavior(self):
        """
        One-time instruction to Gemini
        """
        textarea = self._get_active_textarea()
        textarea.click()

        self.prompt = """
        Instruction :
            I want you to act as a "Single-Block Response Engine. From now on, you must follow these absolute constraints for every reply: 
                1. You Must Response the Upcomming Request in such a format so that i can COPY THE RESPONSE IN JUST ONE CLICK.
                2. Wrap your entire response (including all text, explanations, and code) inside a single copyable block.
                3. Do not include any text, greetings, or sign-offs outside of that one code block.
                4. Ensure there is only one copyable block per response.
                5. If the response is long, keep it all within that same single block.
                6. You must give a copyable block per request.
                7. You have to give a written respose
            Output:
                Only output Json
                No other text than JSON
                Response in such a format so that i can copy the response in just one click
            Strict Output format : {"status": "success","message": "Full response text"}
        Request : 
        """
        self._type_multiline(textarea, self.prompt)
        time.sleep(1)
        self._get_send_button().click()
        time.sleep(1)
        # 
        self.last_copy_buttons_len = 1


    def _type_multiline(self, textarea, text):
        for line in text.split("\n"):
            textarea.send_keys(line)
            textarea.send_keys(Keys.SHIFT, Keys.ENTER)
            time.sleep(self.typing_delay)

    def _copy_last_response(self, retries=5, wait_time=0.8):
        pyperclip.copy("")  # 🔹 clear clipboard first

        for _ in range(retries):
            copy_buttons = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//button[@aria-label='Copy code text to clipboard.']")
                )
            )
            # 
            # print(len(copy_buttons))
            if len(copy_buttons) > self.last_copy_buttons_len:
                print("Response :")
                copy_button = copy_buttons[-1]
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    copy_button
                )
                copy_button.click()

                time.sleep(wait_time)

                data = pyperclip.paste()
                if data.strip():      # ✅ clipboard updated
                    self.last_copy_buttons_len = len(copy_buttons)
                    return data
            # 
            else:
                print("Waiting ....")
                time.sleep(2)
        # 
        raise Exception("Failed to copy Gemini response")


    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def generate(self, prompt: str) -> str:
        """
        Send prompt to Gemini and return copied response
        """
        textarea = self._get_active_textarea()
        textarea.click()
        time.sleep(0.3)

        self._type_multiline(textarea, self.prompt + prompt)

        time.sleep(2)
        self._get_send_button().click()

        time.sleep(5)  # wait for response render
        return self._copy_last_response()

    def close(self):
        self.driver.quit()
