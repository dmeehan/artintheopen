# events/models.py

"""

    Models for the Events app, which organizes, processes, stores,
    and retrieves events on the AIO website.

    Douglas Meehan
    dmeehan@gmail.com
    
""" 
import datetime

from django.db import models
from django.db.models import permalink

from localflavor.us.models import PhoneNumberField, USStateField
from filebrowser.fields import FileBrowseField

from managers import HomeFeatureManager
from locations.fields import LocationField
from affiliates.models import Affiliate


class FutureEventManager(models.Manager):
    def get_query_set(self):
        now = datetime.datetime.now()
        return super(FutureEventManager,self).get_query_set().filter(end_date__gte=now).order_by('start_date')

class FeaturedEventManager(models.Manager):
    def get_query_set(self):
        now = datetime.datetime.now()
        return super(FeaturedEventManager,self).get_query_set()\
                                               .filter(end_date__gte=now)\
                                               .filter(featured_home=True)\
                                               .order_by('start_date')
        
class PastEventManager(models.Manager):
    def get_query_set(self):
        now = datetime.datetime.now()
        return super(PastEventManager,self).get_query_set().filter(start_date__lt=now).order_by('-start_date')
        
class UpcomingEventManager(models.Manager):
    def get_query_set(self):
        now = datetime.datetime.now()
        limit = datetime.timedelta(weeks=3)
        diff = now + limit
        return super(UpcomingEventManager,self).get_query_set().filter(start_date__gte=now).filter(start_date__lte=diff).order_by('start_date')
        
class AIOEventManager(models.Manager):
    def get_query_set(self):
        now = datetime.datetime.now()
        return super(AIOEventManager,self).get_query_set().filter(end_date__gte=now).filter(aio=True).order_by('start_date')
        
class AIOPastEventManager(models.Manager):
    def get_query_set(self):
        now = datetime.datetime.now()
        return super(AIOPastEventManager,self).get_query_set().filter(end_date__lt=now).filter(aio=True).order_by('-start_date')
    
class Event(models.Model):
    """
    
    Art in the Open related events.
            
    """
    #standard Model Manager
    objects = models.Manager()
    
    # custom Model Managers 
    future = FutureEventManager()
    past = PastEventManager()
    upcoming = UpcomingEventManager()
    local = AIOEventManager()
    local_past = AIOPastEventManager()
    featured = FeaturedEventManager()
    
    # core fields
    title = models.CharField(max_length=255)
    affiliate = models.ForeignKey(Affiliate, blank=True, null=True)
    aio = models.BooleanField()
    host = models.CharField(max_length=255, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    fee = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    description = models.TextField(blank=True)
    location = LocationField(blank=True, max_length=255)
    location_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = USStateField(blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    contact = models.CharField(verbose_name='contact person', max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField(blank=True, help_text="Format: XXX-XXX-XXXX")
    website = models.URLField(blank=True)
    image = FileBrowseField("Image", format="Image", max_length=200, 
                            blank=True, null=True,
                            help_text="Valid file formats: .jpg, .png")
    
    # meta data
    slug = models.SlugField(unique_for_date="start_date", 
                            help_text="""Suggested value automatically 
                                         generated from name. Must be unique per published date.""")
    featured_home = models.BooleanField(verbose_name="featured on Home page")
    featured_events = models.BooleanField(verbose_name="featured on Events page")
    
    @property
    def display_date(self):
        d = datetime.date.today()
        if self.start_date <= d and self.end_date >= d:
            return d
        else:
            return self.start_date

    def save(self, force_insert=False, force_update=False):
        if self.aio:
            self.host = "Art in the Open"
        elif self.affiliate and not self.host:
            self.host = self.affiliate.name
        if self.start_date and not self.end_date:
            self.end_date = self.start_date
        super(Event, self).save(force_insert, force_update)
        
    def __unicode__(self):
        return u'%s' % self.title
  
    @permalink
    def get_absolute_url(self):
        return ('events_event_detail', None, {
            'year': self.start_date.year,
            'month': self.start_date.strftime('%b').lower(),
            'day': self.start_date.day,
            'slug': self.slug
        })
