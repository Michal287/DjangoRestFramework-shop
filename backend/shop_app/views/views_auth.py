from rest_framework.viewsets import ModelViewSet
from ..models import User
from ..serializers.serializers_auth import UserListSerializer, UserSerializer, RegisterSerializer, RequestPasswordResetSerializer, PasswordResetSerializer, EmailVerifySerializer
from ..permissions import IsNotAuthenticated, IsAdmin, IsOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import jwt
from django.conf import settings
from rest_framework.generics import CreateAPIView


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsNotAuthenticated]


class EmailVerifyView(APIView):
    serializer_class = EmailVerifySerializer

    def post(self, request):

        try:
            token = request.POST.get('token')

            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])

            if not user.is_active:
                user.is_active = True
                user.save()
                return Response(status=status.HTTP_200_OK)

            elif user.is_active:
                return Response({"message": "Your account is still active."}, status=status.HTTP_200_OK)

            return Response({"message": "Congratulations, you activated the account."}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError:
            return Response({'error: Activation already expired'}, status=status.HTTP_400_BAD_REQUEST)

        except jwt.exceptions.DecodeError:
            return Response({'error: Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class RequestPasswordResetView(CreateAPIView):
    permission_classes = [IsNotAuthenticated]
    serializer_class = RequestPasswordResetSerializer


class PasswordResetView(CreateAPIView):
    permission_classes = [IsNotAuthenticated]
    serializer_class = PasswordResetSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        else:
            return UserSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'retrieve']:
            self.permission_classes = [IsAuthenticated, IsOwner]
        elif self.action in ['destroy', 'list', 'create']:
            self.permission_classes = [IsAuthenticated, IsAdmin]
        return super(self.__class__, self).get_permissions()

