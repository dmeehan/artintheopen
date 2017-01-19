# managers.py

from django.db import models

class HomeFeatureManager(models.Manager):
    def get_queryset(self):
        return super(HomeFeatureManager, self).get_queryset().filter(featured_home=True)