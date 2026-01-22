
from Core.Logger import get_logger
logger = get_logger("hireiq.prompt.function")

# -----------------------------------------------

def generatePrompt(job_description, verbose=False):
    """
    """
    logger.info("Initialize Function - generatePrompt") if verbose else None
    # 
    prompt = """
You are a resume–job matching engine designed to help a candidate decide
whether they SHOULD apply for a role, not whether they will be rejected
by an ultra-strict ATS.

TASK:
Compare the candidate’s resume with the job description and determine
whether applying to this role is reasonable and beneficial for the candidate.

IMPORTANT INTERPRETATION RULES:
- Treat academic projects, self-initiated projects, internships, and certifications
  as VALID experience for fresher and entry-level roles.
- Do NOT consider personal or academic project experience as "industry experience"
  unless the job description explicitly excludes project-based learning.
- If a role is marked as "Fresher", "0 years", or "Entry-level", candidates with
  strong academic or project-based experience are STILL considered eligible.
- Being over-skilled is NOT a rejection criterion.
- Focus on whether the candidate can perform or grow into the role,
  not whether they exactly match a trainee-only profile.

EVALUATION CRITERIA:
Return True if:
- The candidate meets the education requirement
- There is clear overlap with required skills (even at a learning or project level)
- The role aligns with the candidate’s career direction
- The candidate is NOT explicitly disqualified by hard constraints

Return False only if:
- Required core skills are missing
- Mandatory qualifications are unmet
- The role is clearly irrelevant to the candidate’s background or goals

OUTPUT RULES:
- Output ONLY one word: True or False
- No explanations, no extra text


INPUTS:
1. Resume :

SHASHANK KUMAR NAMDEO | Gender : Male 
shashanknamdeo28@gmail.com | +91 9981325976
linkedin.com/in/shashanknamdeo28 | github.com/shashanknamdeo
Bhopal, India

PROFILE SUMMARY :
Highly motivated B.Tech student specializing in Artificial Intelligence and Machine Learning with strong hands-on experience
in Python, Django, AWS, and API-based systems. Skilled in designing scalable backend architectures, AI-driven applications,
and cloud-native solutions. Passionate about building real-world products in EdTech, FinTech, and mobile applications, with
a focus on clean architecture, automation, and performance optimization.

SKILLS & COMPETENCIES :
● Programming: Python, JavaScript, SQL
● Frameworks: Django, React Native, Node.js
● Cloud & DevOps: AWS (EC2, RDS, IAM, S3), Elastic Beanstalk, Docker
● Databases: PostgreSQL, MongoDB
● APIs & Tools: REST APIs, Git, GitHub
● Core Concepts: OOP, Data Structures, Algorithmic Thinking, System Design, Microservices, Agile Methodologies

PROJECTS & PRACTICAL EXPERIENCE :

1. NeuroLearn – AI-Based Personalized Learning Platform
Generative AI (Gemini ), React Native, AWS Cloud, Django, PostgreSQL
● Created NeuroLearn to revolutionize personalized learning and accelerate skill mastery.
● Leverages AI & ML algorithms to generate dynamic, adaptive study plans for each learner.
● Integrates Python, Django, React Native, and AWS Cloud for seamless, scalable performance.
● Empowers learners to achieve goals faster, enhancing knowledge retention and productivity.

2. IntelliTrade – Automated Trading & Analytics System
Django, AI & Machine Learning, Data Analysis, Kotak Securities API, Zerodha API
● Created IntelliTrade, an AI-powered algorithmic trading platform to automate multi-asset trading.
● Built using Python, Django, HTML/CSS/JS, deployed on AWS for scalable, real-time performance.
● Integrated Kotak Securities API for precise trade execution and Zerodha API for live market data.
● Enables smart, data-driven trading, real-time monitoring, and advanced analytics dashboards.
● Improves profitability, decision-making speed, and ensures secure, disaster-proof trade data storage.

3. SNK – Material Management Mobile Application
React Native, AWS Amplify, AWS S3, AWS Cognito
● Developed SNK App to automate secure cloud sync for local files, solving manual backup challenges.
● Implemented React Native frontend with AWS Amplify, S3 storage, and PostgreSQL for manifest tracking.
● Built auto-sync and conflict resolution using custom manifest comparison and MD5 hashing.
● Enabled real-time multi-device sync, reducing data loss risk and boosting productivity for end users.

EDUCATION :
Bachelor of Technology – Artificial Intelligence & Machine Learning
LNCT Group Of Colleges, Bhopal
2022 – 2026

CERTIFICATIONS : 
AWS Certified Cloud Practitioner – Amazon Web Services
Wipro TalentNext – .NET Full Stack Developer Certification – Wipro Limited

2. Job Description (Text):

    """
    # 
    return prompt + job_description

if __name__ == "__main__":
    print(generatePrompt(job_description='jd'))