

import os
import time

from dotenv import load_dotenv

from google import genai
from google.genai.errors import ServerError

from PromptFunction import *

# --------------------------------------------------------------------------

from Core.Logger import get_logger
logger = get_logger("hireiq.compare.resume.and.job.description")

# --------------------------------------------------------------------------

def fetchGeminiAccessKey(verbose=False):
    """
    """
    logger.info("Initialize Function - fetchGeminiAccessKey") if verbose else None
    # get path from environment variable (Windows)
    secrets_path = os.getenv("SECRETS_FILE")
    if not secrets_path:
        raise SystemExit("SECRETS_FILE environment variable is not set.")
    # 
    # load the file into the process environment
    load_dotenv(dotenv_path=secrets_path, override=False)
    # 
    # now access secrets via os.getenv
    api_key = os.getenv("GOSSIPY_API_KEY")
    # print('api_key : ', api_key)
    return api_key

# --------------------------------------------------------------------------

def generateGeminiResponse(api_key, job_description, verbose=False):
    """
    """
    logger.info("Initialize Function - generateGeminiResponse") if verbose else None
    # 
    max_retries = 5
    retry_delay = 30
    # 
    # 1. Create client with API key
    client = genai.Client(api_key=api_key)
    # 
    # 2. Use supported model
    model = "models/gemini-2.5-flash"
    # 
    # 3. Simple prompt
    prompt = generatePrompt(job_description=job_description, verbose=verbose)
    # print(prompt)
    # 
    for attempt in range(1, max_retries + 1):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )
            # print('response : ', response)
            return response.text
        # 
        except ServerError as e:
            logger.info(f"Attempt {attempt} failed    |    Exception - 503 (Model is overloaded)    |    Retrying in 30 seconds.....")
            time.sleep(retry_delay)
    # 
    logger.info("All retries failed.")


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
    generateGeminiResponse(api_key=api_key, job_description=job_description)