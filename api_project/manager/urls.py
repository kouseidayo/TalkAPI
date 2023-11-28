from django.urls import path
from .views import TalkAPIView

urlpatterns = [
    path('talk/', TalkAPIView.as_view(), name='talk'),
]