from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include, handler404, handler500
from django.contrib import admin

#handler404 = 'applications.delivrem.views.handler404'
#handler500 = 'applications.delivrem.views.handler500'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('applications.cumberland.urls')),
    url(r'^account/', include('applications.account.urls')),
    url('social-auth/',include('social.apps.django_app.urls', namespace='social')),
]
#Static files serves with WhiteNoise (pip install WhiteNoise)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
