# managers.py

from django.db import models

class HomeFeatureManager(models.Manager):
    def get_query_set(self):
        return super(HomeFeatureManager, self).get_query_set().filter(featured_home=True)