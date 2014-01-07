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

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from views import *

urlpatterns = patterns('',

    # User authentication management.
    url(r'^users/login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}, name='user_login'),
    url(r'^users/logout/$', view='django.contrib.auth.views.logout_then_login', name='user_logout'),
    url(r'^users/(?P<pk>\d+)/$', view=DetailUserView.as_view(), name='user_detail'),
    url(r'^users/(?P<pk>\d+)/edit/$', view=UpdateUserView.as_view(), name='user_edit'),
    url(r'^users/(?P<pk>\d+)/delete/$', view=DeleteUserView.as_view(), name='user_delete'),
    
    # Homepage.
    (r'^$', TemplateView.as_view(template_name="index.html")),
)
)
