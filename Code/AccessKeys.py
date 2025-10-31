import os
from dotenv import load_dotenv

# get path from environment variable (Windows)
secrets_path = os.getenv("SECRETS_FILE")
if not secrets_path:
    raise SystemExit("SECRETS_FILE environment variable is not set.")

# load the file into the process environment
load_dotenv(dotenv_path=secrets_path, override=False)

# now access secrets via os.getenv
api_key = os.getenv("API_KEY")