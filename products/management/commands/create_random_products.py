import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from products.models import Product, ProductTag


class Command(BaseCommand):
    help = "Create random products"

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=1000,
            help='Number of products to create'
        )

    def handle(self, *args, **options):
        count = options['count']
        currencies = ['GEL', 'USD', 'EUR']

        tag_names = ['Tech', 'Food', 'Clothes', 'Home', 'Sport']
        tags = []

        for name in tag_names:
            tag, _ = ProductTag.objects.get_or_create(name=name)
            tags.append(tag)

        products = []

        self.stdout.write(self.style.WARNING(f'Creating {count} products...'))

        with transaction.atomic():
            for i in range(count):
                # 50% older than 1 year, 50% newer than 1 year
                if i % 2 == 0:
                    created_at = timezone.now() - timedelta(
                        days=random.randint(366, 800)
                    )
                else:
                    created_at = timezone.now() - timedelta(
                        days=random.randint(1, 300)
                    )

                products.append(
                    Product(
                        name=f"Product_{i}_{random.randint(1000, 9999)}",
                        description=f"Random description for product {i}",
                        price=round(random.uniform(10, 5000), 2),
                        currency=random.choice(currencies),
                        created_at=created_at,
                    )
                )

            created_products = Product.objects.bulk_create(products)

            for product in created_products:
                product.tags.set(
                    random.sample(tags, random.randint(0, len(tags)))
                )

        self.stdout.write(self.style.SUCCESS('✅ Products created successfully!'))