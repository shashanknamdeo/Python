
# import os
# os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# model_name = "google/flan-t5-base"

# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# resume_text = """
# SHASHANK KUMAR NAMDEO
# shashanknamdeo28@gmail.com | +91 9981325976
# linkedin.com/in/shashanknamdeo28 | github.com/shashanknamdeo
# Bhopal, India

# PROFILE SUMMARY
# Entry-level Software Engineer and AI/ML undergraduate with hands-on experience in Python, Django, and AWS. Skilled in
# building scalable backend systems, REST APIs, automation pipelines, and cloud-native applications for EdTech and FinTech
# use cases. Experienced with PostgreSQL, REST API design, authentication workflows, and deploying production systems on
# AWS.

# SKILLS & COMPETENCIES
# ● Development - Python, Django, RESTful APIs, API Integration, Backend Architecture, Automation, Selenium
# ● Cloud & DevOps - AWS (EC2, RDS, S3, IAM, Elastic Beanstalk, CloudWatch), Docker, Cloud Deployment,
# Environment Configuration, Scalable Systems
# ● Databases & Data Handling - PostgreSQL, MongoDB, SQL, Data Modeling, Query Optimization
# ● AI / ML & Analytics - AI/ML Concepts, Generative AI (Gemini), Data Analysis, Algorithmic Logic
# ● Tools & Engineering Practices - Git, GitHub, Linux, Logging, Error Handling, Unit Testing, CI/CD Basics, Fault
# Tolerance, Agile Methodologies

# EXPERIENCE
# Software Engineer – Project Experience | Independent & Academic Projects | Bhopal, India | During B.Tech (2022 – Present)

# HireIQ – AI-Driven Job Application Automation Platform
# Python, Django, Selenium, Generative AI (Gemini), PostgreSQL, AWS (RDS, Elastic Beanstalk)
# ● Built an end-to-end job automation pipeline for discovery, analysis, and application, reducing manual effort by 70–80%.
# ● Implemented a Python–Django multi-worker architecture for scraping, resume matching, and apply-flow detection with
# GenAI-based JD scoring.
# ● Designed secure RESTful APIs with authentication, authorization, logging, retries, and fault-tolerant, database-driven
# workflows.
# ● Deployed on AWS with PostgreSQL-backed persistence, enabling scalable, restart-safe processing and operational stability.

# IntelliTrade – Automated Trading & Analytics System
# Python, Django, AI/ML, Data Analysis, Kotak Securities API, Zerodha API, AWS
# ● Developed an AI-powered algorithmic trading platform supporting multi-asset trading including equities and derivatives.
# ● Integrated Kotak Securities API for automated trade execution and Zerodha API for real-time market data ingestion.
# ● Built RESTful backend services in Django to process live data streams, strategy execution, trade logging, and performance
# monitoring.
# ● Deployed on AWS to support scalable, low-latency operations and secure trade data storage.

# NeuroLearn – AI-Based Personalized Learning Platform
# Generative AI (Gemini), Django, React Native, AWS, PostgreSQL
# ● Architected an AI-driven learning platform delivering personalized study plans using learner goals, pace, and performance data.
# ● Applied AI/ML to dynamically adapt learning paths, improving learning efficiency, content relevance, and engagement.
# ● Built a scalable Django and PostgreSQL backend deployed on AWS with validation, API security, and database optimization.
# ● Designed RESTful APIs with authentication, authorization, logging, retries, and a React Native app for seamless access.

# EDUCATION
# Bachelor of Technology – Artificial Intelligence & Machine Learning
# Jai Narain College of Technology, Bhopal
# 2022 – 2026

# CERTIFICATIONS
# ● AWS Certified Cloud Practitioner (August 2025) – Amazon Web Services
# ● Wipro TalentNext – .NET Full Stack Developer Certification (October 2025)– Wipro Limited
# """

# job_description = """
# We are seeking an enthusiastic and detail-oriented Python Trainee to join our development team. This role is ideal for fresh graduates or early professionals who are passionate about programming and eager to build a strong career in Python development through hands-on experience and guided mentorship.

# Key Responsibilities

# Support the development and maintenance of Python-based applications

# Write clean, maintainable, and efficient code under supervision

# Assist in debugging, testing, and resolving application issues

# Collaborate with team members to understand project requirements

# Learn and implement best practices in coding and software development

# Participate in internal training sessions and code reviews

# Requirements
# Basic knowledge of Python programming

# Understanding of object-oriented programming concepts

# Familiarity with databases and basic SQL is an advantage

# Exposure to frameworks such as Django or Flask is a plus

# Good analytical and problem-solving skills

# Strong willingness to learn and adapt
# """

# prompt = f"""
# You are an ATS-friendly resume optimizer.

# TASK:
# 1. Rewrite the resume to match the job description
# 2. Keep facts truthful
# 3. Use strong action verbs
# 4. Output ONLY valid JSON

# JSON FORMAT:
# {{
#   "name": "",
#   "summary": "",
#   "skills": [],
#   "experience": [],
#   "projects": [],
#   "keywords_matched": []
# }}

# RESUME:
# {resume_text}

# JOB DESCRIPTION:
# {job_description}
# """

# inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

# outputs = model.generate(
#     **inputs,
#     max_length=512,
#     do_sample=True,      # allow stochastic generation
#     top_k=50,
#     top_p=0.95,
# )

# print(f'Output : \n \n {outputs}')

# result = tokenizer.decode(outputs[0], skip_special_tokens=True)

# print(f'Result : \n \n {result}')
# print(type(result))

# import json

# try:
#     parsed = json.loads(result)
#     print(parsed)
# except json.JSONDecodeError:
#     print("Invalid JSON output. Here's what the model returned:")
#     print(result)



# import os
# import json
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# # Silence HF warnings
# os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# # ---------------------------
# # 1️⃣ Load tokenizer and model
# # ---------------------------
# model_name = "google/flan-t5-base"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# # Force CPU
# device = "cpu"
# model.to(device)

# # ---------------------------
# # 2️⃣ Resume and JD
# # ---------------------------

# # ---------------------------
# # 3️⃣ Split resume into sections
# # ---------------------------
# sections = {
#     "summary": "",
#     "skills": "",
#     "experience": "",
#     "projects": "",
# }

# # Simple split based on your resume headings
# def extract_section(text, heading):
#     import re
#     pattern = rf"{heading}([\s\S]*?)(?=(?:\n[A-Z ]+\n)|$)"
#     match = re.search(pattern, text)
#     if match:
#         return match.group(1).strip()
#     return ""

# sections["summary"] = extract_section(resume_text, "PROFILE SUMMARY")
# sections["skills"] = extract_section(resume_text, "SKILLS & COMPETENCIES")
# sections["experience"] = extract_section(resume_text, "EXPERIENCE")
# sections["projects"] = extract_section(resume_text, "PROJECTS")  # Optional if exists

# # ---------------------------
# # 4️⃣ Function to generate JSON for one section
# # ---------------------------
# def generate_json(section_name, section_text, jd_text):
#     prompt = f"""
# You are an ATS-friendly resume optimizer.

# TASK:
# 1. Rewrite this section of the resume to match the job description.
# 2. Keep facts truthful.
# 3. Use strong action verbs.
# 4. Output ONLY valid JSON for this section.

# JSON FORMAT:
# {{
#   "{section_name}": [],
#   "keywords_matched": []
# }}

# RESUME SECTION:
# {section_text}

# JOB DESCRIPTION:
# {jd_text}
# """
#     inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024).to(device)
    
#     outputs = model.generate(
#         **inputs,
#         max_length=256,
#         do_sample=True,
#         top_k=50,
#         top_p=0.95
#     )
    
#     result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
#     try:
#         parsed = json.loads(result)
#         return parsed
#     except json.JSONDecodeError:
#         print(f"Warning: Invalid JSON output for section '{section_name}'. Using raw text.")
#         return {section_name: [section_text.strip()], "keywords_matched": []}

# # ---------------------------
# # 5️⃣ Generate JSON per section
# # ---------------------------
# final_json = {"name": "Shashank Kumar Namdeo"}  # Name fixed
# for section, text in sections.items():
#     if text:
#         section_json = generate_json(section, text, job_description)
#         final_json.update(section_json)

# # ---------------------------
# # 6️⃣ Output final JSON
# # ---------------------------
# print(json.dumps(final_json, indent=2))

# ---------------------------------------------------------------------------------------------------

import os
import json
import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Silence HF warnings
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# ---------------------------
# 1️⃣ Load tokenizer and model
# ---------------------------
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Force CPU
device = "cpu"
model.to(device)

# ---------------------------
# 2️⃣ Resume and JD
# ---------------------------

resume_text = """
SHASHANK KUMAR NAMDEO
shashanknamdeo28@gmail.com | +91 9981325976
linkedin.com/in/shashanknamdeo28 | github.com/shashanknamdeo
Bhopal, India

PROFILE SUMMARY
Entry-level Software Engineer and AI/ML undergraduate with hands-on experience in Python, Django, and AWS. Skilled in
building scalable backend systems, REST APIs, automation pipelines, and cloud-native applications for EdTech and FinTech
use cases. Experienced with PostgreSQL, REST API design, authentication workflows, and deploying production systems on
AWS.

SKILLS & COMPETENCIES
● Development - Python, Django, RESTful APIs, API Integration, Backend Architecture, Automation, Selenium
● Cloud & DevOps - AWS (EC2, RDS, S3, IAM, Elastic Beanstalk, CloudWatch), Docker, Cloud Deployment,
Environment Configuration, Scalable Systems
● Databases & Data Handling - PostgreSQL, MongoDB, SQL, Data Modeling, Query Optimization
● AI / ML & Analytics - AI/ML Concepts, Generative AI (Gemini), Data Analysis, Algorithmic Logic
● Tools & Engineering Practices - Git, GitHub, Linux, Logging, Error Handling, Unit Testing, CI/CD Basics, Fault
Tolerance, Agile Methodologies

EXPERIENCE
Software Engineer – Project Experience | Independent & Academic Projects | Bhopal, India | During B.Tech (2022 – Present)

HireIQ – AI-Driven Job Application Automation Platform
Python, Django, Selenium, Generative AI (Gemini), PostgreSQL, AWS (RDS, Elastic Beanstalk)
● Built an end-to-end job automation pipeline for discovery, analysis, and application, reducing manual effort by 70–80%.
● Implemented a Python–Django multi-worker architecture for scraping, resume matching, and apply-flow detection with
GenAI-based JD scoring.
● Designed secure RESTful APIs with authentication, authorization, logging, retries, and fault-tolerant, database-driven
workflows.
● Deployed on AWS with PostgreSQL-backed persistence, enabling scalable, restart-safe processing and operational stability.

IntelliTrade – Automated Trading & Analytics System
Python, Django, AI/ML, Data Analysis, Kotak Securities API, Zerodha API, AWS
● Developed an AI-powered algorithmic trading platform supporting multi-asset trading including equities and derivatives.
● Integrated Kotak Securities API for automated trade execution and Zerodha API for real-time market data ingestion.
● Built RESTful backend services in Django to process live data streams, strategy execution, trade logging, and performance
monitoring.
● Deployed on AWS to support scalable, low-latency operations and secure trade data storage.

NeuroLearn – AI-Based Personalized Learning Platform
Generative AI (Gemini), Django, React Native, AWS, PostgreSQL
● Architected an AI-driven learning platform delivering personalized study plans using learner goals, pace, and performance data.
● Applied AI/ML to dynamically adapt learning paths, improving learning efficiency, content relevance, and engagement.
● Built a scalable Django and PostgreSQL backend deployed on AWS with validation, API security, and database optimization.
● Designed RESTful APIs with authentication, authorization, logging, retries, and a React Native app for seamless access.

EDUCATION
Bachelor of Technology – Artificial Intelligence & Machine Learning
Jai Narain College of Technology, Bhopal
2022 – 2026

CERTIFICATIONS
● AWS Certified Cloud Practitioner (August 2025) – Amazon Web Services
● Wipro TalentNext – .NET Full Stack Developer Certification (October 2025)– Wipro Limited

"""

job_description = """
We are seeking an enthusiastic and detail-oriented Python Trainee to join our development team. This role is ideal for fresh graduates or early professionals who are passionate about programming and eager to build a strong career in Python development through hands-on experience and guided mentorship.

Key Responsibilities

Support the development and maintenance of Python-based applications

Write clean, maintainable, and efficient code under supervision

Assist in debugging, testing, and resolving application issues

Collaborate with team members to understand project requirements

Learn and implement best practices in coding and software development

Participate in internal training sessions and code reviews

Requirements
Basic knowledge of Python programming

Understanding of object-oriented programming concepts

Familiarity with databases and basic SQL is an advantage

Exposure to frameworks such as Django or Flask is a plus

Good analytical and problem-solving skills

Strong willingness to learn and adapt
"""

# ---------------------------
# 3️⃣ Extract sections
# ---------------------------
def extract_section(text, heading):
    pattern = rf"{heading}([\s\S]*?)(?=(?:\n[A-Z ]+\n)|$)"
    match = re.search(pattern, text)
    return match.group(1).strip() if match else ""

summary_text = extract_section(resume_text, "PROFILE SUMMARY")
skills_text = extract_section(resume_text, "SKILLS & COMPETENCIES")
experience_text = extract_section(resume_text, "EXPERIENCE")
projects_text = extract_section(resume_text, "PROJECTS")  # optional

# ---------------------------
# 4️⃣ Split bullets for skills & experience
# ---------------------------
def split_bullets(text):
    lines = text.split("\n")
    bullets = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("●") and len(line) > 5:
            bullets.append(line)
        elif line.startswith("●"):
            bullets.append(line[1:].strip())
    return bullets

skills_bullets = split_bullets(skills_text)
experience_bullets = split_bullets(experience_text)

# ---------------------------
# 5️⃣ Function to generate JSON per bullet
# ---------------------------
def generate_json(section_name, bullet_text, jd_text):
    prompt = f"""
You are an ATS-friendly resume optimizer.

TASK:
1. Rewrite this resume bullet to match the job description.
2. Keep facts truthful.
3. Output ONLY valid JSON for this bullet.

JSON FORMAT:
{{
  "{section_name}": [],
  "keywords_matched": []
}}

RESUME BULLET:
{bullet_text}

JOB DESCRIPTION:
{jd_text}
"""
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(device)
    
    outputs = model.generate(
        **inputs,
        max_length=128,
        do_sample=True,
        top_k=50,
        top_p=0.95
    )
    
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    try:
        parsed = json.loads(result)
        return parsed
    except json.JSONDecodeError:
        # fallback: just return the bullet itself
        keywords = [word for word in jd_text.split() if word.lower() in bullet_text.lower()]
        return {section_name: [bullet_text.strip()], "keywords_matched": list(set(keywords))}

# ---------------------------
# 6️⃣ Generate JSON for all bullets
# ---------------------------
final_json = {"name": "Shashank Kumar Namdeo"}

# Summary
summary_json = generate_json("summary", summary_text, job_description)
final_json.update(summary_json)

# Skills
all_skills = []
all_skills_keywords = []
for bullet in skills_bullets:
    res = generate_json("skills", bullet, job_description)
    all_skills.extend(res.get("skills", []))
    all_skills_keywords.extend(res.get("keywords_matched", []))
final_json["skills"] = all_skills
final_json["keywords_matched"] = list(set(all_skills_keywords))

# Experience
all_experience = []
all_exp_keywords = []
for bullet in experience_bullets:
    res = generate_json("experience", bullet, job_description)
    all_experience.extend(res.get("experience", []))
    all_exp_keywords.extend(res.get("keywords_matched", []))
final_json["experience"] = all_experience
final_json["keywords_matched"] = list(set(all_skills_keywords + all_exp_keywords))

# Projects (optional)
if projects_text:
    projects_json = generate_json("projects", projects_text, job_description)
    final_json["projects"] = projects_json.get("projects", [])

# ---------------------------
# 7️⃣ Output final JSON
# ---------------------------
print(json.dumps(final_json, indent=2))
