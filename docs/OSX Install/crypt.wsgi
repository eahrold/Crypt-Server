import os, sys
import site

#Set this to the location of your environment
CRYPT_ENV_DIR = '/path/to/your/crypt_env'

# Use site to load the site-packages directory of our virtualenv
site.addsitedir(os.path.join(CRYPT_ENV_DIR, 'lib/python2.7/site-packages'))

# Make sure we have the virtualenv and the Django app itself added to our path
sys.path.append(CRYPT_ENV_DIR)
sys.path.append(os.path.join(CRYPT_ENV_DIR, 'crypt'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fvserver.settings")
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
