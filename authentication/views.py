from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse_lazy
from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_STRING
from drf_yasg.utils import swagger_auto_schema
from .serializers import RegisterSerializer, EmailVerifySerializer, LoginSerializer, LogoutSerializer
from .models import User
from .helpers import send_email
from os import environ
from jwt import decode, ExpiredSignatureError, DecodeError


# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        # Obtener el objeto Usuario
        user_object = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user_object).access_token

        endpoint_verify = reverse_lazy('email_verify')

        url = f'http://{environ.get("DJANGO_HOST")}:{environ.get("DJANGO_PORT")}{endpoint_verify}?token={token}'

        data = {
            'subject': 'Confirmar usuario',
            'body': f'Hola {user_object.username}, usa este link para activar tu cuenta {url}',
            'to': f'{user_object.email}'
        }

        send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class EmailVerifyView(views.APIView):
    serializer_class = EmailVerifySerializer

    token_params = Parameter('token', in_=IN_QUERY, description='Token Autenticación', type=TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_params])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = decode(token, environ.get('SECRET_KEY'), algorithms='HS256')

            user = User.objects.get(id=payload['user_id'])
            message = 'El usuario ya ha sido activado anteriormente'

            if not user.is_verified:
                message = 'El usuario ha sido activado'
                user.is_verified = True
                user.is_active = True
                user.save()

            return Response({
                'success': message
            }, status=status.HTTP_200_OK)

        except ExpiredSignatureError:
            return Response({
                'error': 'El token ha expirado'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except DecodeError:
            return Response({
                'error': 'Token incorrecto'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'success': 'Se cerro la sesión'
        }, status=status.HTTP_200_OK)
