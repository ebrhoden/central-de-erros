from django.db import models

# Create your models here.
from django.core.validators import validate_ipv4_address
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

import datetime

# Create your models here.


LEVEL_CHOICES = [
    ('critical', 'critical'),
    ('debug', 'debug'),
    ('error', 'error'),
    ('warning', 'warning'),
    ('information', 'info'),
]

AMBIENT_CHOICES = [
    ('production', 'Produção'),
    ('homologation', 'Homologação'),
    ('dev', 'dev'),
]


class Log(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=False)
    description = models.CharField(max_length=200, blank=True, null=False)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, blank=True, null=False)
    event = models.IntegerField(blank=True, null=False)
    origin = models.GenericIPAddressField(validators=[validate_ipv4_address], null=True)
    archived = models.BooleanField(default=False)
    ambient = models.CharField(max_length=20, choices=AMBIENT_CHOICES, blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def archived_true(self):
        self.archived = True

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]

