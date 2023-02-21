from django import forms
from rest_framework import serializers
from django.contrib.auth.models import User


class registerform(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']