from django.urls import path

from api import views

urlpatterns = [
    path("user/", views.UserDetailAPIView.as_view()),
    path("check/", views.Loginapiview.as_view()),
    path("computer/", views.ComputerList.as_view()),
]