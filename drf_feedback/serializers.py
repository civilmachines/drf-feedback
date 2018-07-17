from rest_framework import serializers


class AddFeedbackSerializer(serializers.ModelSerializer):
    """
    Serializer for Adding Feedback
    """
    class Meta:
        from .models import Feedback

        model = Feedback
        fields = ('name', 'email', 'mobile', 'message')
