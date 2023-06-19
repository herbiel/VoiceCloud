#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：VoiceCLoud 
@File    ：urls.py
@Author  ：herbiel8800@gmail.com
@Date    ：2023/6/18 02:10 
'''
from django.urls import path, include

from .views import (
    ExtensionListApiView,
)

urlpatterns = [
    path('api', ExtensionListApiView.as_view()),
]