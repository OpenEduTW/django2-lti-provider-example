"""
WSGI config for MyProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
os.environ["DJANGO_SETTINGS_MODULE"] = "MyProject.settings"

#if Use ENV
import sys
from os.path import join,dirname,abspath
PROJECT_DIR = dirname(dirname(abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)
from MyProject.local_settings import VIRTUALENV_PATH
sys.path.insert(0,VIRTUALENV_PATH)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
