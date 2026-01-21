

import os
from dotenv import load_dotenv
from google import genai

from PromptFunction import *

# --------------------------------------------------------------------------


def fetchGeminiAccessKey():
    """
    """
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

def generateGeminiResponse(api_key, job_description):
    """
    """
    # 1. Create client with API key
    client = genai.Client(api_key=api_key)
    # 
    # 2. Use supported model
    model = "models/gemini-2.5-flash"
    # 
    # 3. Simple prompt
    prompt = generatePrompt(job_description=job_description)
    print(prompt)
    # 
    print("Check Gemini : ", client.models.generate_content(
        model=model,
        contents="""Hello, Gemini"""
    ).text)
    response = client.models.generate_content(
        model=model,
        contents=prompt
    )
    # 
    # 5. Print output
    print('response : ', response)
    print('response.text : ', response.text)
    return response.text


# --------------------------------------------------------------------------

job_description = """
Job description
JD - Job Description
Network Eng
Job Description
We are seeking a Network Admin Level 3 to join our dynamic IT team. In this role, you will be responsible for Design, Build, Implementation, and L2/L3 support for our network infrastructure, ensuring optimal network performance and uptime. The ideal candidate possesses a strong foundation in networking fundamentals and a keen interest in learning and growing within the field.
Responsibilities:
Design, implement, and manage network infrastructure, including FortiGate and Cisco Meraki Suit, including Firewalls & Switches, VPN, SD-WAN Cisco ISE, Aruba Clear Pass, AWS Load Balancers, Cisco & Meraki Wireless LAN Controllers and Access Points.
Monitor and maintain network infrastructure, including FortiGate and Cisco Meraki Suit, including Firewalls & Switches, VPN, SD-WAN Cisco ISE, Aruba Clear Pass, AWS Load Balancers, Cisco & Meraki Wireless LAN Controllers, and Access Points.
Troubleshoot and resolve network connectivity issues, escalating complex problems to higher-level engineers as needed.
Configure and maintain network devices according to established procedures and standards.
Implement network access control policies and procedures to enhance security.
Provide technical support to end-users for network-related issues.
Document network configurations, troubleshooting steps, and resolution processes.
Stay updated on emerging network technologies and industry best practices.
Qualifications:
Bachelor s degree in computer science, Information Technology, or a related field preferred.
Strong understanding of networking fundamentals, including TCP/IP, routing, switching, Firewalls, Cloud technology, and network protocols.
Hands-on experience with FortiGate and Cisco Meraki Suit, including Firewalls & Switches, VPN, SD-WAN Cisco ISE, Aruba Clear Pass, AWS Load Balancers, Cisco & Meraki Wireless LAN Controllers and Access Points.
Knowledge of Network Access Control (NAC) principles and technologies.
Excellent troubleshooting and problem-solving skills.
Strong communication and interpersonal skills.
Ability to work independently and as part of a team.
Desired Skills:
Proven L3/L4 Troubleshooting Experience in complex environments.
Experience with Multivendor OEM platforms ( Cisco, Meraki, FortiGate, Zscaler ) design, build, and Implementation.
Experience with cloud networking platforms design and implementation (AWS, Azure).
Proven Experience with network virtualization technologies (SD-WAN, SDN).
Experience with network automation and scripting (Python, Ansible, etc.).
Proven Experience with network DDI solution design and implementation.
Experience with network monitoring and analysis tools.
Experience with scripting languages (e.g., Python, PowerShell).
IT certifications CCNP , NSE 3/4 are a plus.
Role: Network (Support) Engineer
Industry Type: IT Services & Consulting
Department: Engineering - Hardware & Networks
Employment Type: Full Time, Permanent
Role Category: IT Network
Education
UG: Any Graduate
PG: Any Postgraduate
"""

# --------------------------------------------------------------------------

if __name__ == "__main__":
    api_key = fetchGeminiAccessKey()
    print(api_key)
    # 
    print(job_description)
    generateGeminiResponse(api_key=api_key, job_description=job_description)