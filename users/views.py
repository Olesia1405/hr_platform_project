from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []
