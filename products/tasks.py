# products/tasks.py

from celery import shared_task
from django.utils import timezone
from datetime import timedelta

from .models import Product


@shared_task
def delete_old_products():
    one_year_ago = timezone.now() - timedelta(days=365)

    deleted_count, _ = Product.objects.filter(
        created_at__lt=one_year_ago
    ).delete()

    return f"{deleted_count} products older than 1 year deleted"