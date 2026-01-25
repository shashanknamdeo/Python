
from django.contrib import admin
from .models import Job


@admin.action(description="Retry selected jobs")
def retry_jobs(self, request, queryset):
    queryset.update(
        apply_status="pending",
        job_status="unknown",
        last_error=None
    )


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "naukri_job_id",
        "job_url",
        # 
        "scrape_status",
        "resume_match",
        "job_status",
        "apply_status",
        # 
        "created_at",
        "updated_at",
        # 
        "last_error",
    )
    # 
    list_filter = (
        "scrape_status",
        "resume_match",
        "job_status",
        "apply_status",
        "created_at",
        "updated_at",
    )
    # 
    search_fields = (
        "naukri_job_id",
        "job_url",
    )
    # 
    readonly_fields = (
        "naukri_job_id",
        "job_url",
        # 
        "created_at",
        "updated_at",
    )
    # 
    ordering = ("-created_at",)
    # 
    actions = [retry_jobs]   # 👈 THIS LINE
    # 
    list_per_page = 50


