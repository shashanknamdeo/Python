from django.core.management.base import BaseCommand
import logging

from Workers.JobFinderWorker import jobFinderWorker

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Find new jobs from Naukri and store in DB"

    def handle(self, *args, **options):
        logger.info("Job Finder command started")

        worker = jobFinderWorker()
        worker.run()

        logger.info("Job Finder command finished")
