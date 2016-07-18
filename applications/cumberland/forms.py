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
        widget=forms.DateInput(
            attrs={"class":"datepicker",
                    'type': 'date',
                    'placeholder':"07/17/2016",
                    "cols":3,}
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
        self.fields['description'].widget = forms.Textarea(
                                            attrs={'rows': '8'})

        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("Create a Suggestion Box"),
                Field("title", css_class="input-block-level"),
                Field('expiring_date'),
                Field("email", css_class="input-block-level"),
                Field("description", css_class="input-block-level"),
                ),
                FormActions(
                    layout.Submit("submit", _("Save")),
                    layout.Button('cancel', 'Cancel', onclick="window.location.href='/';")
                )
        )
######################################################
######################################################
######################################################
######################################################
######################################################
######################################################
######################################################

class SuggiesFormCrispyForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ('comment',)

    '''
    def clean_comment(self):
        data = self.cleaned_data.get('body')
        if len(data) <= 5:
            raise forms.ValidationError('The Suggies is too short')
            return data
    '''

    def __init__(self, *args, **kwargs):
        super(SuggiesFormCrispyForm,self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = ""
        self.helper.form_method = "POST"
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-3'
        self.helper.field_class = 'col-sm-4'
        self.fields["comment"].required = True
        self.fields['comment'].widget = forms.Textarea(
                                            attrs={'rows': '3', 'cols':'4'})

        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("Add a Suggies"),
                Field("comment", css_class="input-block-level"),
                ),
                FormActions(
                    layout.Submit("submit", _("Add suggies")),
                    layout.Button('cancel', 'Cancel', onclick="window.location.href='/';")
                )
        )


from django_comments.forms import CommentForm

class BoxCommentForm(CommentForm):
    class Meta:
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """Setup the form to work with crispy_forms."""
        super(BoxCommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        # For some reason the form_id is not working. Leaving it as a reminder
        # to fix it at some point
        self.helper.form_id = 'comment-form'
        self.helper.layout = Layout(
            Fieldset(
                'Post Comment',
                'comment',
                'content_type',
                'object_pk',
                'timestamp',
                'security_hash',
            ),
            FormActions(
                Button('post', 'Post'),
            )
            )
