from django import forms

from .models import Box, Suggestion, Recipients

class PostForm(forms.ModelForm):
    class Meta:
        model = Box
        fields = ('title','description', 'email', 'expiring_date', )

    def clean_body(self):
        data = self.cleaned_data.get('body')
        if len(data) <= 5:
            raise forms.ValidationError('Message in the body is too short')
        return data
