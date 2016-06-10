from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views import generic


from .models import Box, Suggestion
from .forms import BoxForm
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'cumberland/home.html'

class BoxCreateView(CreateView):
    """
    """
    model = Box
    form_class = BoxForm
    template_name = 'cumberland/creeate.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        if getattr(request.user, 'first_name', None) == 'Martin':
            raise Http404()
        return super(PostUpdateView, self).post(request, *args, **kwargs)
