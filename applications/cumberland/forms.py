from django import forms

from .models import Box, Suggestion, Recipient
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_forms import layout
from crispy_forms import layout, bootstrap
from crispy_forms.bootstrap import Field, FormActions

#from captcha.fields import ReCaptchaField

class BoxForm(forms.ModelForm):
    class Meta:
        model = Box
        fields = ('title','description', 'email', 'expiring_date', )
    '''
    def clean_body(self):
        data = self.cleaned_data.get('body')
        if len(data) <= 5:
            raise forms.ValidationError('Message in the body is too short')
        return data
    '''
