from django import forms

from .models import Box, Suggestion, Recipient
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from crispy_forms import layout
from crispy_forms import layout, bootstrap
from crispy_forms.bootstrap import Field, FormActions
from bootstrap3_datetime.widgets import DateTimePicker
from django.forms.extras.widgets import SelectDateWidget

#from captcha.fields import ReCaptchaField

class BoxFormCrispyForm(forms.ModelForm):
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
    expiring_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),
        required=False,
    )
    def __init__(self, *args, **kwargs):
        super(BoxFormCrispyForm,self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = ""
        self.helper.form_method = "POST"
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-4'
        self.fields["title"].required = True
        self.date = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))
        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("Create a Suggestion Box"),
                Field("title", css_class="input-block-level"),
                Field('expiring_date'),
                Field("email", css_class="input-block-level"),
                Field("description", css_class="input-block-level", rows="3"),
                ),
                FormActions(
                    layout.Submit("submit", _("Save")),
                    layout.Button('cancel', 'Cancel', onclick="window.location.href='/';")
                )
        )
