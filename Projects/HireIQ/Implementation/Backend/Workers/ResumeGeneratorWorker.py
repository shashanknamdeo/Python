import os
import sys
import json
import pdfkit
import pyperclip

from jinja2 import Environment, FileSystemLoader


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

print("BASE_DIR =", BASE_DIR)

from GenAI import gen_ai_client

# -------------------------------------------------------------------------------------------------

def read_multiline_input(end_word="END"):
    print(f"\n\nEnter your prompt (type '{end_word}' on a new line to finish):")
    lines = []
    # 
    while True:
        line = input()
        if line.strip() == end_word:
            break
        lines.append(line)
    # 
    return "\n".join(lines)


def generateResumeJSON(prompt):
    try:
        client = gen_ai_client()
        jd = read_multiline_input()
        request_prompt = prompt + jd
        print(request_prompt)
        response = client.generate(request_prompt)
        print(response)
        # client.close()
        return response
    # 
    except Exception as e:
        print('Exception - generateResumeJSON', e)


def extract_message(response: str) -> dict:
    parsed = json.loads(response)          # outer JSON
    message_str = parsed["message"]        # string
    resume_dict = json.loads(message_str)  # inner JSON
    return resume_dict


# Load resume JSON
# with open("ResumeOutput.json", "r", encoding="utf-8") as f:
#     resume_data = json.load(f)

# Load HTML template

def generateResumePDF(resume_json):
    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=True
    )
    template = env.get_template("ResumeTemplate.html")

    # Render HTML
    rendered_html = template.render(**resume_json)

    # Save HTML (debug-friendly)
    with open("resume_rendered.html", "w", encoding="utf-8") as f:
        f.write(rendered_html)

    # PDF configuration
    options = {
        "encoding": "UTF-8",
        "page-size": "A4",
        "margin-top": "10mm",
        "margin-bottom": "10mm",
        "margin-left": "10mm",
        "margin-right": "10mm",
    }

    # Generate PDF
    pdfkit.from_file(
        "resume_rendered.html",
        "Resume.pdf",
        options=options
    )

    print("✅ Resume PDF generated successfully")





# def main():
#     """
#     """
#     response = generateResumeJSON(prompt)
#     resume_json = extract_message(response)
#     generateResumePDF(resume_json)

def main(prompt):
    """
    """
    while True:
        print('\n\n\n\n\n\n\n----------------------------------------------------------------------------------------------------')
        jd = read_multiline_input()
        temp_prompt = prompt + jd
        print(temp_prompt)
        pyperclip.copy(temp_prompt)
        # 
        resume_json = read_multiline_input()
        print(type(resume_json))
        print(resume_json)
        resume_json = json.loads(resume_json)
        print(type(resume_json))
        generateResumePDF(resume_json)








prompt = """
tweak my resume to create a new resume json based on JD 

Output:
    Only output Json
    No other text than JSON
    Response in such a format so that i can copy the response in just one click
Output Format :
{"profile_summary": "","skills": {"Skill_Types (First alphabet capital)" : ["Skill_1", "Skill_2"]},"experience": {"role": "Software Engineer – Project Experience","type": "Independent & Academic Projects","location": "Bhopal, India","duration": "2022 – Present","projects": [{"name": "HireIQ – AI-Driven Job Application Automation Platform","technologies": [],"highlights": []},{"name": "IntelliTrade – Automated Trading & Analytics System","technologies": [],"highlights": []},{"name": "NeuroLearn – AI-Based Personalized Learning Platform","technologies": [],"highlights": []},]}}


this is my resume JSON

{"profile_summary": "Entry-level Software Engineer and AI/ML undergraduate with hands-on experience in Python, Django, and AWS. Skilled in building scalable backendsystems, REST APIs, automation pipelines, and cloud-native applications for EdTech and FinTech use cases. Experienced with PostgreSQL, REST API design, authenticationworkflows, and deploying production systems on AWS.","skills": {"development": ["Python","Django","RESTful APIs","API Integration","Backend Architecture","Automation","Selenium"],"cloud_devops": ["AWS EC2","AWS RDS","AWS S3","AWS IAM","AWS Elastic Beanstalk","AWS CloudWatch","Docker","Cloud Deployment","Environment Configuration","Scalable Systems"],"databases": ["PostgreSQL","MongoDB","SQL","Data Modeling","Query Optimization"],"ai_ml_analytics": ["AI/ML Concepts","Generative AI (Gemini)","Data Analysis","Algorithmic Logic"],"tools_practices": ["Git","GitHub","Linux","Logging","Error Handling","Unit Testing","CI/CD Basics","Fault Tolerance","Agile Methodologies"]},"experience": {"role": "Software Engineer – Project Experience","type": "Independent & Academic Projects","location": "Bhopal, India","duration": "2022 – Present","projects": [{"name": "HireIQ – AI-Driven Job Application Automation Platform","technologies": ["Python","Django","Selenium","Generative AI (Gemini)","PostgreSQL","AWS RDS","AWS Elastic Beanstalk"],"highlights": ["Built an end-to-end job automation pipeline for discovery, analysis, and application, reducing manual effort by 70–80%.","Implemented a Python–Django multi-worker architecture for scraping, resume matching, and apply-flow detection with GenAI-based JD scoring.","Designed secure RESTful APIs with authentication, authorization, logging, retries, and fault-tolerant database-driven workflows.","Deployed on AWS with PostgreSQL-backed persistence, enabling scalable, restart-safe processing and operational stability."]},{"name": "IntelliTrade – Automated Trading & Analytics System","technologies": ["Python","Django","AI/ML","Data Analysis","Kotak Securities API","Zerodha API","AWS"],"highlights": ["Developed an AI-powered algorithmic trading platform supporting multi-asset trading including equities and derivatives.","Integrated Kotak Securities API for automated trade execution and Zerodha API for real-time market data ingestion.","Built RESTful backend services in Django to process live data streams, strategy execution, trade logging, and performance monitoring.","Deployed on AWS to support scalable, low-latency operations and secure trade data storage."]},{"name": "NeuroLearn – AI-Based Personalized Learning Platform","technologies": ["Generative AI (Gemini)","Django","React Native","AWS","PostgreSQL"],"highlights": ["Architected an AI-driven learning platform delivering personalized study plans using learner goals, pace, and performance data.","Applied AI/ML to dynamically adapt learning paths, improving learning efficiency, content relevance, and engagement.","Built a scalable Django and PostgreSQL backend deployed on AWS with validation, API security, and database optimization.","Designed RESTful APIs with authentication, authorization, logging, retries, and a React Native app for seamless access."]}]},


and this is the JD 

---------------------------------------------------------------------------------------------------


"""


main(prompt)
