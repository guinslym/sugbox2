import socket

ROOT_URLCONF = 'sugbox.urls'
WSGI_APPLICATION = 'sugbox.wsgi.application'
#My laptop is name 'Guinsly-thinkpad-lenovo'
if 'guinsly' in socket.gethostname():
    from .development import *
    print('--dev--settings--')
else:
    from .production import *
    #print('prod--settings')
#this file won't be load in git and in the
