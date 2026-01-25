from django.core.management.base import BaseCommand
import logging

from Workers.ApplyTypeWorker import applyTypeWorker

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Handle apply_type based job applications"

class Command(BaseCommand):
    help = "Handle chatbot based applications"

    def handle(self, *args, **options):
        logger.info("Chatbot command started")

        applyTypeWorker().run()

        logger.info("Chatbot command finished")
