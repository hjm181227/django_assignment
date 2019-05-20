from django.urls import path

from .views import BoardListCreateAPIView, ResumeListCreateAPIView


urlpatterns = [
    path('resume/', ResumeListCreateAPIView.as_view()),
    path('board/', BoardListCreateAPIView.as_view()),
]
