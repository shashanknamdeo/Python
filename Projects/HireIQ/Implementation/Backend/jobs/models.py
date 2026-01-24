from django.db import models

class Job(models.Model):
    naukri_job_id = models.BigIntegerField(unique=True, db_index=True)
    job_url = models.URLField(max_length=1000, unique=True)
    # 
    resume_match = models.BooleanField(null=True)
    # 
    scrape_status = models.CharField(max_length=20, default="pending")
    chatbot_status = models.CharField(max_length=20, default="unknown")
    apply_status = models.CharField(max_length=20, default="pending")
    # 
    last_error = models.TextField(null=True, blank=True)
    # 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 
    class Meta:
        indexes = [
            models.Index(fields=["scrape_status"]),
            models.Index(fields=["chatbot_status"]),
            models.Index(fields=["apply_status"]),
        ]
    # 
    def __str__(self):
        return f"{self.naukri_job_id}"

