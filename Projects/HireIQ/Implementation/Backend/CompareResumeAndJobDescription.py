

import os
import time

from dotenv import load_dotenv

from google import genai
from google.genai.errors import ServerError

from PromptFunction import *

# --------------------------------------------------------------------------

from Core.Logger import get_logger
logger = get_logger("__name__")

# --------------------------------------------------------------------------

def fetchGeminiAccessKey():
    """
    """
    logger.debug("Function Initialized")
    # 
    try:
        # Get path from environment variable (Windows)
        secrets_path = os.getenv("SECRETS_FILE")
        if not secrets_path:
            raise SystemExit("SECRETS_FILE environment variable is not set.")
        # 
        # Load the file into the process environment
        load_dotenv(dotenv_path=secrets_path, override=False)
        # 
        # Access secrets via os.getenv
        api_key = os.getenv("Gemini_GenAI_API_Key")
        # print('api_key : ', api_key)
        return api_key
    # 
    except Exception as e:
        logger.error(f"Error - fetchGeminiAccessKey | {e}", exc_info=True)
        sys.exit(1)


# --------------------------------------------------------------------------


def generateGeminiResponse(api_key, prompt):
    """
    """
    try:
        logger.debug("Function Initialized")
        # 
        max_retries = 5
        retry_delay = 30
        # 
        # Create client with API key
        client = genai.Client(api_key=api_key)
        # 
        # Use supported model
        model = "models/gemini-2.5-flash"
        # 
        for attempt in range(1, max_retries + 1):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )
                logger.info(f"Gemini Response Generated    |    Response : {response.text}")
                return response.text
            # 
            except ServerError as e:
                logger.info(f"Attempt {attempt} failed    |    Exception - 503 (Model is overloaded)    |    Retrying in 30 seconds.....")
                time.sleep(retry_delay)
        # 
        logger.info("All retries failed.")
    # 
    except Exception as e:
        logger.error(f"Error - generateGeminiResponse | {e}", exc_info=True)
        sys.exit(1)


def compareJob(api_key, job_description):
    """
    """
    logger.debug("Function Initialized")
    # 
    try:
        prompt = generatePrompt(job_description=job_description)
        # 
        response = generateGeminiResponse(api_key=api_key, prompt=prompt)
        # 
        return response
    # 
    except Exception as e:
        logger.error(f"Error - compareJob | {e}", exc_info=True)
        sys.exit(1)


# --------------------------------------------------------------------------

job_description = """
{'url': 'https://www.naukri.com/job-listings-ai-associate-tenjumps-softech-bengaluru-0-to-1-years-210126022862', 'title': 'AI Associate', 'company': 'Tenjumps Softech', 'experience': '0 - 1 years', 'salary': 'Not Disclosed', 'location': 'Bengaluru', 'description': 'Job description\nJob Title: AI Associate (Fresher)\nExperience: 0 Years (Fresh Graduates Only)\nEducation: B.Tech / M.Tech / MS (Any specialisation)\nBackground: Strong academic exposure from IITs or equivalent institutes preferred\n\nJob Description\nWe are looking for fresh graduates who are eager to build a career in Artificial Intelligence. This role is designed for candidates with no prior experience in AI or the industry. Selected candidates will undergo structured training and work under mentorship to learn AI concepts and support AI-driven projects.\n\nKey Responsibilities\nLearn AI, Machine Learning, and Data concepts through internal training programs\nAssist senior team members in data preparation and basic analysis. Support testing and validation of AI models\nDocument learnings, processes, and observations\nParticipate in team discussions and knowledge-sharing sessions.\n\nMandatory Requirements\nStrong logical thinking and problem-solving ability\nBasic understanding of programming concepts (any language)\nGood grasp of mathematics at the graduation level\nWillingness to learn new technologies and tools\nGood communication skills\n\n\nRole: Data Science & Machine Learning - Other\nIndustry Type: Courier / Logistics (Logistics Tech)\nDepartment: Data Science & Analytics\nEmployment Type: Full Time, Permanent\nRole Category: Data Science & Machine Learning\nEducation\nUG: Any Graduate\nKey Skills\nSkills highlighted with ‘‘ are preferred keyskills\nArtificial Intelligence\nMachine LearningPython'}
"""

# --------------------------------------------------------------------------

if __name__ == "__main__":
    api_key = fetchGeminiAccessKey()
    print(api_key)
    # 
    print(job_description)
    compareJob(api_key=api_key, job_description=job_description)