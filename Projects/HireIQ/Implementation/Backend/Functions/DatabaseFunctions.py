
import os
import sys

# -----------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

print("BASE_DIR =", BASE_DIR)

# -----------------------------------------------

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# -----------------------------------------------

from jobs.models import Job

# 🔹 See total entries
print('Job Count : ', Job.objects.count())

# 🔹 See last 5 jobs
print('Last 5 Job : ', Job.objects.order_by("-created_at")[:5])

# 🔹 Pretty print
print('Printing All Jobs')
for job in Job.objects.all():
    print(f'{job.naukri_job_id}    |    {job.scrape_status}    |    {job.job_url}')

print('Printing Comparision Result')
def fmt(val, width):
    return f"{'' if val is None else str(val):<{width}}"

for job in Job.objects.all()[10:]:
    print(
        f"{fmt(job.naukri_job_id, 20)}    |    "
        f"{fmt(job.scrape_status, 10)}    |    "
        f"{fmt(job.resume_match, 5)}    |    "
        f"{fmt(job.job_status, 15)}    |    "
        f"{fmt(job.apply_status, 10)}"
    )

