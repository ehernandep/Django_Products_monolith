from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("waiting for the database...")
        conn = None
        while not conn:
            try:
                conn = connections['default']
            except OperationalError:
                self.stdout.write(
                    'Database unavialable, waiting for 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('database available!'))
