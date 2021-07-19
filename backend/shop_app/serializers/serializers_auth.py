import jwt
from rest_framework_simplejwt.tokens import RefreshToken
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from ..models import User
from rest_framework import serializers
from django.contrib.auth import password_validation
from django.conf import settings


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, max_length=32)

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']
        extra_kwargs = {
            'passowrd': {'write_only': True}
        }

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        email = data['email']

        if password != password2:
            raise serializers.ValidationError('Passwords are diffrent')

        password_validation.validate_password(password)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('This email is already exist')

        return data

    def create(self, data):
        password = data.get('password')
        email = data['email']

        user = User(
            username=email,
            email=email)

        user.set_password(password)
        user.save()

        return user


class EmailVerifySerializer(serializers.Serializer):
    token = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        model = User
        fields = ['token']


class RequestPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True, max_length=64)

    class Meta:
        model = User
        fields = ['email']

    def validate(self, data):
        email = data.get('email')

        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('This email is not exist')

        return data

    def save(self):

        email = self.validated_data['email']
        user = User.objects.get(email=email)

        merge_data = {
            'user': user,
            'protocol': "http",
            'domain': '127.0.0.1:8000',
            'token': RefreshToken.for_user(user=user).access_token
        }

        subject = render_to_string("email/email_password_reset/email_subject.txt", merge_data).strip()
        html_body = render_to_string("email/email_password_reset/email_body.html", merge_data)

        msg = EmailMultiAlternatives(subject=subject, to=["mbanach2@edu.cdv.pl"])
        msg.attach_alternative(html_body, "text/html")
        msg.send()


class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, max_length=32)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, max_length=32)
    token = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        model = User
        fields = ['password', 'password2', 'token']

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError('Passwords are diffrent')

        password_validation.validate_password(password)

        return data

    def save(self):
        try:
            token = self.validated_data['token']

            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

            user = User.objects.get(id=payload['user_id'])
            password = self.validated_data['password']

            user.set_password(password)
            user.save()

        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Activation already expired')

        except jwt.exceptions.DecodeError:
            raise serializers.ValidationError('Invalid token')


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'street', 'zip_code', 'city']

