from django.urls import path
from .views import SignUpView, ProfileUpdate, EmailUpdate
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup'),
    path('profile/', ProfileUpdate.as_view(), name = 'profile'),
    path('profile/email/', EmailUpdate.as_view(), name = 'profile_email'),
    path('password_reset/', views.passReset, name = 'password_reset')
]