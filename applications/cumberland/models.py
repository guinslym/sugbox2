from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django_extensions.db.models import  TimeStampedModel
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from basis.models import TimeStampModel
import datetime
from django.utils import timezone
import uuid
import arrow

@python_2_unicode_compatible
class Box(TimeStampModel):
    """
    Box model
    """
    def __str__(self):
        return self.title

    title = models.CharField(max_length=60, verbose_name=_('Title'),
                            blank=False, null=False,
                            help_text="Add a title on you Suggestion " \
                            "Box i.e: How did you find my presentation")
    description = models.CharField(max_length=250,
                            blank=True, null=True,
                            help_text="Your beautiful description"\
                            " of this Suggestion Box")
    email = models.EmailField(blank=False, null=False,
                            help_text="We will send you an email so that "\
                            "you can activate your new Suggestion Box")
    expiring_date = models.DateField(
                        default=(timezone.now() + datetime.timedelta(days=30)),
                        blank=True, null=True,
                        help_text="Select a date of Expiration." \
                        " By default it is set two 1 months")
    identify = models.BooleanField(default=False)
    activate = models.BooleanField(default=False)
    slug = models.UUIDField(default=uuid.uuid4, editable=False)
    activation_key = models.UUIDField(default=uuid.uuid4, editable=False)
    #receivers = models.EmailField(blank=True, null=True)
    '''
    def get_absolute_url(self):
        return reverse('suggies:detail_box',
                       args=[str(self.slug)]
                )
    '''
    @property
    def time_ago(self):
        time_ago = arrow.get(self.created)
        return time_ago.humanize(locale='pt')

    class Meta:
        ordering = ['-id']

@python_2_unicode_compatible
class Suggestion(TimeStampModel):
    """
    For adding comments (or suggestions)
    """
    def __str__(self):
        return self.comment[0:10]

    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name='suggies')
    comment = models.CharField("",max_length=250, blank=True, null=True)
    slug = models.UUIDField(default=uuid.uuid4, editable=False)
    #participant = participan_id

    '''
    def get_absolute_url(self):
        return reverse('suggies:detail_suggies',
                       args=[str(self.id)]
                )
    '''
    class Meta:
        ordering = ['-created_at']

@python_2_unicode_compatible
class Recipient(TimeStampModel):
    """
    For adding comments (or suggestions)
    """
    def __str__(self):
        return self.receiver

    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name='recipients')
    receiver = models.EmailField(blank=True, null=True)
    #participant = participan_id

    '''
    def get_absolute_url(self):
        return reverse('suggies:detail_suggies',
                       args=[str(self.id)]
                )
    '''
    class Meta:
        ordering = ['-created_at']
