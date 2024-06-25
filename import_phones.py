import os
import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Import phones data from CSV file'

    def handle(self, *args, **options):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'phones.csv')

        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                phone = Phone(
                    id=row['id'],
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists']
                )
                phone.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported phones data'))
