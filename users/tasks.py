from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email_task(subject, message, recipient_list):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipient_list,
        fail_silently=False,
    )
    return "Email sent successfully"




# # 1. Create the network (if it doesn't exist)
# docker network create mz_network

# # 2. Connect both containers to it
# docker network connect mz_network <django_container_name>
# docker network connect mz_network redis

# # 3. Restart Django container with correct env vars
# docker stop <django_container_name>

# docker run -d -p 8000:8000 --network mz_network -e CELERY_BROKER_URL=redis://redis:6379/0 -e CELERY_RESULT_BACKEND=redis://redis:6379/0 mz_store python manage.py runserver 0.0.0.0:8000