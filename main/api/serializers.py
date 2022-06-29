from rest_framework import serializers

from main.models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):
    # url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = ContactMessage
        fields = '__all__'
