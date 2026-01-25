from django.core.management.base import BaseCommand
import logging

from Workers.ScraperWorker import scraper_worker

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Scrape job details and compare with resume"

    def handle(self, *args, **options):
        logger.info("Scraper command started")

        scraper_worker().run()

        logger.info("Scraper command finished")
