from django.core.management.base import BaseCommand
import logging

from Workers.ApplyWorker import applyJobWorker

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Apply to matched jobs"

    def handle(self, *args, **options):
        logger.info("Apply Jobs command started")

        applyJobWorker().run()

        logger.info("Apply Jobs command finished")
