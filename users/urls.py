#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  urls.py
#  
#  Copyright 2020 lizy <674051537@qq.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""为应用程序users定义URL模式"""
from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from . import views

urlpatterns=[
	# 登录页面(该方法为过去版本的，新版本3.0不存在此功能了，故此处作废该功能)
	# path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
	# 注销页面
	path('logout',views.logout,name='logout'),

]

app_name='users';




