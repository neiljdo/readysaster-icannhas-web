from django.db.models.signals import post_save

from .models import AlertWarning


def alert_warning_handler(sender, instance, created, **kwargs):
    if created:
        pass


post_save.connect(alert_warning_handler, sender=AlertWarning)
