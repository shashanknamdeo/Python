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

{
  "profile_summary": "Entry-level Software Engineer and AI/ML undergraduate with hands-on experience in Python, Django, AWS, and Prompt Engineering for AI-driven applications. Skilled in building scalable backend systems, REST APIs, automation pipelines, and cloud-native solutions for EdTech, FinTech, and AI/ML projects. Experienced with PostgreSQL, REST API design, authentication workflows, and deploying production systems on AWS.",
  "skills": {
    "Development": ["Python", "Django", "RESTful APIs", "API Integration", "Backend Architecture", "Automation", "Selenium", "React Native"],
    "Cloud_DevOps": ["AWS EC2", "AWS RDS", "AWS S3", "AWS IAM", "AWS Elastic Beanstalk", "AWS CloudWatch", "Docker", "Cloud Deployment", "Environment Configuration", "Scalable Systems"],
    "Databases": ["PostgreSQL", "MongoDB", "SQL", "Data Modeling", "Query Optimization"],
    "AI_ML_Analytics": ["AI/ML Concepts", "Generative AI (Gemini)", "Prompt Engineering", "AI-driven automation", "Data Analysis", "Algorithmic Logic"],
    "Tools_Practices": ["Git", "GitHub", "Linux", "Logging", "Error Handling", "Unit Testing", "CI/CD Basics", "Fault Tolerance", "Agile Methodologies"]
  },
  "experience": {
    "role": "Software Engineer – Project Experience",
    "type": "Independent & Academic Projects",
    "location": "Bhopal, India",
    "duration": "2022 – Present",
    "projects": [
      {
        "name": "HireIQ – AI-Driven Job Application Automation Platform",
        "technologies": ["Python", "Django", "Selenium", "Generative AI (Gemini)", "Prompt Engineering", "PostgreSQL", "AWS RDS", "AWS Elastic Beanstalk"],
        "highlights": [
          "Built an end-to-end job automation pipeline for discovery, analysis, and application, reducing manual effort by 70–80%.",
          "Implemented a Python–Django multi-worker architecture for scraping, resume matching, and apply-flow detection with Generative AI using Prompt Engineering techniques for JD scoring.",
          "Designed secure RESTful APIs with authentication, authorization, logging, retries, and fault-tolerant, database-driven workflows.",
          "Deployed on AWS with PostgreSQL-backed persistence, enabling scalable, restart-safe processing and operational stability."
        ]
      },
      {
        "name": "IntelliTrade – Automated Trading & Analytics System",
        "technologies": ["Python", "Django", "AI/ML", "Data Analysis", "Kotak Securities API", "Zerodha API", "AWS"],
        "highlights": [
          "Developed an AI-powered algorithmic trading platform supporting multi-asset trading including equities and derivatives.",
          "Integrated Kotak Securities API for automated trade execution and Zerodha API for real-time market data ingestion.",
          "Built RESTful backend services in Django to process live data streams, strategy execution, trade logging, and performance monitoring.",
          "Deployed on AWS to support scalable, low-latency operations and secure trade data storage."
        ]
      },
      {
        "name": "NeuroLearn – AI-Based Personalized Learning Platform",
        "technologies": ["Generative AI (Gemini)", "Django", "React Native", "Prompt Engineering", "AWS", "PostgreSQL"],
        "highlights": [
          "Architected an AI-driven learning platform delivering personalized study plans using learner goals, pace, and performance data.",
          "Applied AI/ML to dynamically adapt learning paths, improving learning efficiency, content relevance, and engagement.",
          "Built a scalable Django and PostgreSQL backend deployed on AWS with validation, API security, and database optimization.",
          "Designed RESTful APIs with authentication, authorization, logging, retries, and a React Native app for seamless access."
        ]
      }
    ]
  },
  "education": [
    {
      "degree": "Bachelor of Technology – Artificial Intelligence & Machine Learning",
      "institution": "Jai Narain College of Technology, Bhopal",
      "duration": "2022 – 2026"
    }
  ],
  "certifications": [
    {"name": "AWS Certified Cloud Practitioner", "date": "August 2025", "issuer": "Amazon Web Services"},
    {"name": "Prompt Engineering Knowledge Universe", "date": "Feb 2026", "issuer": "Tayana Academy"},
    {"name": "Wipro TalentNext – .NET Full Stack Developer Certification", "date": "October 2025", "issuer": "Wipro Limited"}
  ]
}

and this is the JD 

---------------------------------------------------------------------------------------------------


"""


main(prompt)


# Use the RTCIFA Prompt Engineering framework to generate a **New_Resume_JSON** by intelligently tweaking my existing resume JSON based on the JD provided. Follow these guidelines:

# 1. **Role Alignment:** Highlight skills, projects, and experience that match the JD’s required skills, emphasizing **AI, Python, and .NET** wherever applicable.
# 2. **Profile Summary Enhancement:** Tailor the summary to reflect alignment with the position (Developer Intern / Fresher), including keywords like **AI, Python, .NET, Angular, and full-stack development**.
# 3. **Skills Mapping:** Prioritize JD-relevant skills in the JSON, keep other strong technical skills but categorize them appropriately under **Development, Cloud_DevOps, Databases, AI_ML_Analytics, Tools_Practices**.
# 4. **Experience Tweaks:** Update project highlights and technologies to emphasize **Python, AI, .NET familiarity**, and cloud deployment skills while retaining achievements.
# 5. **Certifications & Education:** Keep all existing certifications, highlighting those relevant to **AI, Python, .NET, or cloud technologies**.
# 6. **JSON Output:**  
#    - Only output JSON.  
#    - Follow the same structure as the input JSON.  
#    - Ensure **ATS-friendly formatting** with clear tech keywords.  
#    - All fields are preserved but adjusted for JD relevance.  