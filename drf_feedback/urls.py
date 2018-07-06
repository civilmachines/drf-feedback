from django.conf.urls import url
from . import views


app_name = "drf_feedback"


urlpatterns = [
    url(r'add/$', views.AddFeedbackView.as_view(), name='add-drf_feedback'),
]