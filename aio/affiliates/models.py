# affiliates/models.py

"""

    Models for the Affiliates app, which organizes, processes, stores,
    and retrieves friends, patrons, and partners on the AIO website.

    Douglas Meehan
    dmeehan@gmail.com
    
""" 

from django.db import models
from localflavor.us.models import PhoneNumberField, USStateField

from filebrowser.fields import FileBrowseField

from managers import HomeFeatureManager
from fields import PositionField

class AffiliateLevel(models.Model):
    """
       The level and type of affiliate
    """
    order = PositionField()
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return u'%s' % self.name


class Affiliate(models.Model):
    """
    
    Affiliate model for supporters of AIO
        
    """
    #standard Model Manager
    objects = models.Manager()
    
    # custom Model Managers
    home_feature = HomeFeatureManager()
    
    AFFILIATE_TYPES = (
        ('person', 'Person'),
        ('entity', 'Entity'),
    )
    
    
    # core fields
    affiliate_type = models.CharField(choices=AFFILIATE_TYPES, max_length=30)
    affiliate_level = models.ForeignKey(AffiliateLevel)
    name = models.CharField(max_length=100,
                            help_text="""If the affiliate is a person,
                                       enter his or her name in the 
                                       format: firstname lastname""")
    
    website = models.URLField(blank=True)
    image = FileBrowseField("Image", format="Image", max_length=200, 
                            blank=True, null=True,
                            help_text="Valid file formats: .jpg, .png")
    
    # metadata
    featured_home = models.BooleanField(verbose_name="featured on Home page")
    featured_affiliates = models.BooleanField(verbose_name="featured on Affiliates page")
    slug = models.SlugField(unique=True, 
                            help_text="""Unique web title automatically 
                                         generated from name.""")

    # auto-generated fields
    first_name = models.CharField(max_length=255, editable=False, blank=True)
    last_name = models.CharField(max_length=255, editable=False, blank=True)
                                             
    class Meta:
        ordering = ['affiliate_level', 'affiliate_type', 'last_name', 'first_name', 'name']
    
    def save(self, force_insert=False, force_update=False):
        if self.affiliate_type == 'person':
            names = self.name.split()
            self.first_name = names[0]
            self.last_name = names[-1]
        else:
            self.first_name = ""
            self.last_name = ""
        super(Affiliate, self).save(force_insert, force_update)
    
    def __unicode__(self):
        return u'%s' % self.name
