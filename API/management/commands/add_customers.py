from django.core.management.base import BaseCommand
import csv
import os

from django.conf import settings

from ...models import Customer

customers_file_path = "API/customers.csv"
customers_file = os.path.join(settings.BASE_DIR, customers_file_path)

# Use this command to poblate the db with the csv provided
# python manage.py add_customers


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--id")
        parser.add_argument("--first_name")
        parser.add_argument("--last_name")
        parser.add_argument("--email")
        parser.add_argument("--gender")
        parser.add_argument("--company")
        parser.add_argument("--city")
        parser.add_argument("--title")

    def handle(self, *args, **options):
        with open(customers_file, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            print(header)
            for row in reader:
                customer = Customer()
                customer.id = row[0]
                customer.first_name = row[1]
                customer.last_name = row[2]
                customer.email = row[3]
                customer.gender = row[4]
                customer.company = row[5]
                customer.city = row[6]
                customer.title = row[7]
                customer.save()
