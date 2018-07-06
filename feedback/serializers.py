from .models import Feedback
from rest_framework import serializers


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('created', 'ip', 'name', 'form_name', 'email', 'phone_number', 'message')
        read_only_fields = ('pk', )
