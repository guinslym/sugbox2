from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

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
    template_name = 'cumberland/create.html'
    success_url = '/'

class AboutUsTemplateView(TemplateView):
    template_name = 'cumberland/about_us.html'

class HowToTemplateView(TemplateView):
    template_name = 'cumberland/howto.html'

import uuid
def activate_box(request, activate_box_key):
    #import pdb; pdb.set_trace()
    activate_box_key = uuid.UUID(activate_box_key)
    box = get_object_or_404(Box, activation_key=activate_box_key)
    if not box.activate :
        box.activate = True
        box.save()
        messages.add_message(request, messages.INFO, 'Box is activated.')
        return render(request,
            'cumberland/box_activated.html',{'box':box}
             )
    else:
        return render(request, 'cumberland/already_box_activated.html', {'box':box, 'message':'Your box is already activate'})

'''
def bookmarks_list(request):
    bookmarks = None
    user = request.user
    if user.is_authenticated():
        bookmarks = Bookmark.objects.filter(user=user)
    return render(request, 'index.html', {'bookmarks': bookmarks})


def add_bookmark(request):
    user = request.user
    form = AddBookmarkForm(request.POST or None)
    if form.is_valid():
        bookmark = form.save(commit=False)
        bookmark.user = user
        bookmark.save()
        return redirect('bookmarks_list')
'''
