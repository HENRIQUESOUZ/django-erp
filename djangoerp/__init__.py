#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This file is part of the django ERP project.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

__author__ = 'Emanuele Bertoldi <emanuele.bertoldi@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2014, django ERP Team'
__version__ = '0.0.5'

from django.db.models.loading import cache
from django.db.models.signals import post_syncdb

# Workaround for Django's ticket #10405.
# See http://code.djangoproject.com/ticket/10405#comment:10 for more info.
if not cache.loaded:
    cache.get_models()

# Installation of application specific stuff.
INSTALLING = False

def install_apps(sender, **kwargs):
    global INSTALLING
    if INSTALLING:
        return
    
    INSTALLING = True
    
    print "Installing apps ..."
    
    from django.conf import settings
    for app in settings.INSTALLED_APPS:
        if not app.startswith('django.'):
            management = __import__("%s.management" % app, {}, {}, ["install"])
            try:
                install_func = management.install
                if callable(install_func):
                    print "Installing app %s" % app
                    install_func(sender, **kwargs)
            except AttributeError:
                pass
    
post_syncdb.connect(install_apps, dispatch_uid="install_apps")
)
