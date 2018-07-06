from rest_framework.generics import CreateAPIView
from .models import Feedback
from drfaddons.serializer import IsOwnerFilterBackend


class AddFeedbackView(CreateAPIView):
    """
    Adds a new FeedBack
    """
    from .serializers import AddFeedbackSerializer

    queryset = Feedback.objects.all()
    serializer_class = AddFeedbackSerializer
    filter_backend = (IsOwnerFilterBackend, )

    def perform_create(self, serializer):
        from drfaddons.add_ons import get_client_ip
        if self.request.user.is_authenticated:
            serializer.save(created_by=self.request.user, ip=get_client_ip(self.request))
        else:
            serializer.save(created_by=None, ip=get_client_ip(self.request))
