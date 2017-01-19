# artists/models.py

"""

    Models for the Artists app, which organizes, processes, stores,
    and retrieves artist information on the AIO website.

    Douglas Meehan
    dmeehan@gmail.com
    
""" 

from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User

from localflavor.us.models import PhoneNumberField, USStateField
from filebrowser.fields import FileBrowseField

from locations.widgets import LocationPickerWidget
from locations.fields import LocationField
from managers import HomeFeatureManager

class LiveArtistManager(models.Manager):
    def get_queryset(self):
        return super(LiveArtistManager, self).get_queryset().filter(status=self.model.LIVE_STATUS)
    
class Artist(models.Model):
    """
    
        An artist and his/her related information.
    
    """
    #standard Model Manager
    objects = models.Manager()
    
    # custom Model Manager 
    live = LiveArtistManager()
    home_feature = HomeFeatureManager()

    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )
    
    # core fields
    user = models.OneToOneField(User, blank=True, null=True, help_text="Create a user account for the artist.")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = USStateField(blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    phone = PhoneNumberField(blank=True, help_text="Format: XXX-XXX-XXXX")
    photo = FileBrowseField("Photo", format="Image", max_length=200, 
                            blank=True, null=True,
                            help_text="Valid file formats: .jpg, .png")
    image = FileBrowseField("Image", format="Image", max_length=200, 
                            blank=True, null=True,
                            help_text="Valid file formats: .jpg, .png") 
    bio = models.TextField(help_text="A short biography for the artist")
    website = models.URLField(blank=True, help_text="The artists website")
    
    
    # metadata
    location = LocationField(verbose_name="current location", 
                             blank=True, max_length=255, 
                             help_text="The artists current location during the festival")
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS, help_text="Only entries with live status will be publicly displayed.")
    featured_home = models.BooleanField(verbose_name="featured on Home page")
    featured_artists = models.BooleanField(verbose_name="featured on Artists page")
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from name. Must be unique.")
    
    class Meta:	
        ordering = ['last_name', 'first_name', 'status', 'featured_home', 'featured_artists']

    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)
        
    def __unicode__(self):
        return u'%s' % self.full_name
        
    @permalink
    def get_absolute_url(self):
        return ('artist_detail', [str(self.slug)])
        
    def get_next_by_id(self, obj):
        next_queryset = self.filter(id__gt=obj.id)
        if next_queryset.count() > 0:
            return next_queryset.order_by('id')[0]
        return None