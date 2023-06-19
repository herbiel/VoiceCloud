#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：VoiceCLoud 
@File    ：serializers.py
@Author  ：herbiel8800@gmail.com
@Date    ：2023/6/18 02:01 
'''

from rest_framework import serializers
from .models import Extension
class ExtensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extension
        fields = ["number", "password", "displayname", "domain", "enable"]