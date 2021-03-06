from rest_framework import serializers

from main.models import ContactMessage, SocialIcon


class ContactMessageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=40, error_messages={
        'required': 'Provided name.',
        'blank': 'Provided name.',
        'null': 'Provided name.',
        'max_length': 'Name must have 3 to 40 characters.'
    })
    email = serializers.EmailField(required=True, allow_null=False, allow_blank=False, error_messages={
        'required': 'Provided email.',
        'blank': 'Provided email.',
    })
    subject = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=200, error_messages={
        'required': 'Provided subject.',
        'blank': 'Provided subject.',
        'max_length': 'Subject must not exceed 200 characters.'
    })
    message = serializers.CharField(
        required=True, allow_null=True, allow_blank=False, max_length=500, error_messages={
            'required': 'Provided message.',
            'blank': 'Provided message.',
            'max_length': 'Message must not exceed 500 characters.'
        })

    class Meta:
        model = ContactMessage
        fields = '__all__'


class SocialIconsSerializer(serializers.ModelSerializer):
    provider = serializers.CharField(required=True, allow_null=False, allow_blank=False, max_length=40, error_messages={
        'required': 'Provid provider.',
        'blank': 'Provid provider.',
        'null': 'Provid provider.',
        'max_length': 'Provider must have 3 to 40 characters.'
    })
    icon = serializers.URLField(required=True, allow_null=False, allow_blank=False, error_messages={
        'required': 'Provid icon.',
        'blank': 'Provid icon.',
    })

    class Meta:
        model = SocialIcon
        # fields = '__all__'
        exclude = ['created_at', 'updated_at']
