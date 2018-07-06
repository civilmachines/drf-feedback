from rest_framework.generics import ListCreateAPIView, CreateAPIView
from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackView(CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
