from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet
from .views_profile import ProfileDetailView

router = DefaultRouter()
router.register(r'activities', ActivityViewSet, basename='activity')

urlpatterns = [
    path('', include(router.urls)),
    # Current user's profile
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
]
