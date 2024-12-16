from django.urls import path,include
from .views import RegisterView, LoginView, UserDetailView, SocialMediaUserViewSet
from rest_framework.routers import DefaultRouter
from .models import SocialMediaUser


router = DefaultRouter()
router.register(r'users', SocialMediaUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserDetailView.as_view(), name='profile'),
    path('follow/<int:user_id>/', SocialMediaUserViewSet.as_view({'post': 'follow_user'}), name='follow-user'),
    path('unfollow/<int:user_id>/', SocialMediaUserViewSet.as_view({'post': 'unfollow_user'}), name='unfollow-user'),
]

