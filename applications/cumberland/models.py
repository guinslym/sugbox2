from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django_extensions.db.models import  TimeStampedModel
from django.core.urlresolvers import reverse
from basis.models import TimeStampModel
import uuid

@python_2_unicode_compatible
class Box(TimeStampModel):
    """
    Box model
    """
    def __str__(self):
        return self.title

    title = models.CharField(max_length=60, blank=False, null=False)
    description = models.CharField(max_length=250, blank=True, null=True)
    identify = models.BooleanField(default=False)
    activate = models.BooleanField(default=False)
    slug = models.UUIDField(default=uuid.uuid4, editable=False)
    activation_key = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=True, null=True)
    #receivers = models.EmailField(blank=True, null=True)
    expiring_date = models.DateField(blank=True, null=True)
    '''
    def get_absolute_url(self):
        return reverse('suggies:detail_box',
                       args=[str(self.slug)]
                )
    '''

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
