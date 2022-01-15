from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreatePostView.as_view()),
    path('like/', views.CreateLikeView.as_view()),
    path('unlike/', views.UnlikeView.as_view()),
    path('analytics/', views.LikesRangeDateFilter.as_view()),
    path('all/', views.ListPostView.as_view()),
    path('index/', views.index),
]

