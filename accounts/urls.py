from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]