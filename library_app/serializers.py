# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 13:58:20 2025

@author: hp
"""

from rest_framework import serializers
from .models import AdminUser, Book
from django.contrib.auth.hashers import make_password

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = ['id', 'email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
