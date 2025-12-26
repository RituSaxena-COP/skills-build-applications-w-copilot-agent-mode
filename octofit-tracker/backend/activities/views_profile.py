from rest_framework import generics, permissions
from .serializers import ProfileSerializer, PublicProfileSerializer
from .models import Profile

class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Return the profile for the authenticated user
        return self.request.user.profile


class PublicProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = PublicProfileSerializer
    permission_classes = [permissions.AllowAny]


class PublicProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = PublicProfileSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'user__username'

    def get_object(self):
        username = self.kwargs.get('username')
        return generics.get_object_or_404(Profile, user__username=username)
