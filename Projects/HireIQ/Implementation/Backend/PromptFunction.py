
def generatePrompt(job_description):
    """
    """
    prompt_1 = """
You are an ATS-style resume matching engine.

TASK:
Compare the candidate resume (in JSON format) with the job description text and evaluate how well the resume matches the job requirements.

INPUTS:
1. Resume (JSON):
{
  "profile": {
    "name": "Shashank Kumar Namdeo",
    "email": "shashanknamdeo28@gmail.com",
    "phone": "+91 9981325976",
    "location": "Bhopal, India",
    "linkedin": "https://linkedin.com/in/shashanknamdeo28",
    "github": "https://github.com/shashanknamdeo",
    "summary": "Highly motivated B.Tech student specializing in Artificial Intelligence and Machine Learning with strong hands-on experience in Python, Django, AWS, and API-based systems. Skilled in designing scalable backend architectures, AI-driven applications, and cloud-native solutions. Passionate about building real-world products in EdTech, FinTech, and mobile applications, with a focus on clean architecture, automation, and performance optimization."
  },
  "education": [
    {
      "degree": "Bachelor of Technology",
      "specialization": "Artificial Intelligence and Machine Learning",
      "institution": "Jai Narain College of Technology, Bhopal",
      "duration": "2022-2026"
    }
  ],
  "skills": {
    "programming": [
      "Python",
      "JavaScript",
      "SQL",
      "HTML",
      "CSS"
    ],
    "frameworks_libraries": [
      "Django",
      "React Native",
      "Node.js",
      "REST Framework"
    ],
    "cloud_devops": [
      "AWS",
      "EC2",
      "RDS",
      "IAM",
      "S3",
      "Elastic Beanstalk",
      "Docker",
      "AWS Amplify",
      "AWS Cognito"
    ],
    "databases": [
      "PostgreSQL",
      "MongoDB"
    ],
    "ai_ml_data": [
      "Machine Learning",
      "Artificial Intelligence",
      "Generative AI",
      "Data Analysis",
      "Model Integration",
      "API-based AI Systems"
    ],
    "tools_platforms": [
      "Git",
      "GitHub",
      "REST APIs",
      "Kotak Securities API",
      "Zerodha API"
    ],
    "core_concepts": [
      "Object-Oriented Programming",
      "Data Structures",
      "Algorithmic Thinking",
      "System Design",
      "Microservices Architecture",
      "Agile Methodologies",
      "Clean Architecture",
      "Automation",
      "Performance Optimization"
    ],
    "background_inferred_skills": [
      "Backend Development",
      "Cloud-Native Application Design",
      "Scalable System Architecture",
      "API Integration",
      "Authentication & Authorization",
      "CI/CD Fundamentals",
      "Secure Data Handling",
      "Application Deployment",
      "Real-Time Systems",
      "Debugging and Optimization"
    ]
  },
  "projects": [
    {
      "name": "NeuroLearn",
      "type": "AI-Based Personalized Learning Platform",
      "domain": [
        "EdTech",
        "Artificial Intelligence",
        "Machine Learning"
      ],
      "technologies": [
        "Python",
        "Django",
        "React Native",
        "AWS",
        "PostgreSQL",
        "Generative AI (Gemini)"
      ],
      "description": [
        "Developed an AI-powered platform to generate dynamic and adaptive study plans.",
        "Applied AI and ML algorithms for personalized learning paths.",
        "Built scalable backend using Django and cloud-native AWS services.",
        "Improved knowledge retention and productivity for learners."
      ],
      "skills_gained": [
        "AI-driven application development",
        "Backend scalability",
        "Cloud integration",
        "Personalization systems"
      ]
    },
    {
      "name": "IntelliTrade",
      "type": "Automated Trading & Analytics System",
      "domain": [
        "FinTech",
        "Algorithmic Trading",
        "Data Analytics"
      ],
      "technologies": [
        "Python",
        "Django",
        "Machine Learning",
        "AWS",
        "HTML",
        "CSS",
        "JavaScript",
        "Kotak Securities API",
        "Zerodha API"
      ],
      "description": [
        "Built an AI-powered algorithmic trading platform for multi-asset automation.",
        "Integrated live market data and trade execution APIs.",
        "Deployed scalable real-time system on AWS.",
        "Enabled analytics dashboards and secure data storage."
      ],
      "skills_gained": [
        "Algorithmic trading systems",
        "API-driven architectures",
        "Real-time data processing",
        "Financial data analysis"
      ]
    },
    {
      "name": "SNK",
      "type": "Material Management Mobile Application",
      "domain": [
        "Mobile Applications",
        "Cloud Storage",
        "Automation"
      ],
      "technologies": [
        "React Native",
        "AWS Amplify",
        "AWS S3",
        "AWS Cognito",
        "PostgreSQL"
      ],
      "description": [
        "Developed a mobile app for secure cloud-based file synchronization.",
        "Implemented auto-sync and conflict resolution using MD5 hashing.",
        "Enabled real-time multi-device synchronization.",
        "Reduced risk of data loss and improved user productivity."
      ],
      "skills_gained": [
        "Mobile app development",
        "Cloud storage systems",
        "Authentication systems",
        "Data integrity mechanisms"
      ]
    }
  ],
  "certifications": [
    {
      "name": "AWS Certified Cloud Practitioner",
      "issuer": "Amazon Web Services"
    },
    {
      "name": ".NET Full Stack Developer Certification",
      "issuer": "Wipro TalentNext"
    }
  ],
  "experience_level": "Fresher / Entry-Level",
  "role_preferences": [
    "AI Engineer",
    "Machine Learning Engineer",
    "Backend Developer",
    "Software Engineer",
    "Cloud Engineer"
  ]
}

2. Job Description (Text):

    """
    # 
    prompt_2 = """

SCORING GUIDELINES:
- Score must be an integer between 0 and 100.
- Base the score on:
  • Skills relevance and completeness
  • Experience alignment
  • Education and certifications
  • Tools and technology match
  • Overall role fit
- Do NOT assume missing information.
- Penalize missing required skills.
- Be strict and realistic like an ATS.

OUTPUT RULES (VERY IMPORTANT):
- Output ONLY a single integer number.
- No text, no explanation, no symbols, no JSON.
- Example valid outputs: 23, 67, 94
- Invalid outputs: "Score: 85", { "score": 85 }, 85/100

FINAL OUTPUT:
<single integer between 0 and 100>
    """
    return prompt_1 + job_description + prompt_2

if __name__ == "__main__":
    print(generatePrompt(job_description='jd'))