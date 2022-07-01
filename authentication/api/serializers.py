from rest_framework import serializers
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialApp


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True, error_messages={
        'required': 'Firstname is required.',
        'blank': 'Firstname is required.'
    })
    last_name = serializers.CharField(required=True, error_messages={
        'required': 'Lastname is required.',
        'blank': 'Lastname is required.',
    })
    username = serializers.CharField(required=True, error_messages={
        'required': 'Username is required.',
        'blank': 'Username is required.',
    })

    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['password']
        # fields = ['first_name', "last_name", "username", "id"]
        reade_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class SocialAccountProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialApp
        exclude = ['client_id', 'secret']
