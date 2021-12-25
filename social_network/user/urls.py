from django.urls import path
from . import views

urlpatterns = [
    path('activity/<str:email>/', views.UserActivityView.as_view()),
]

