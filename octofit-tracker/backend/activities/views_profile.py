from rest_framework import generics, permissions
from .serializers import ProfileSerializer

class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Return the profile for the authenticated user
        return self.request.user.profile
