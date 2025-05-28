from django.urls import path
from .views import UserLoginView, UserRegistrationView, UserProfileView, VerifyContributorView, DietaryPreferenceView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('verify/<int:user_id>/', VerifyContributorView.as_view(), name='verify-contributor'),
    path('preferences/', DietaryPreferenceView.as_view(), name='dietary-preferences'),
]
