from django.shortcuts import render
from django.http import JsonResponse

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from .serializers import LoginSerializer
from rest_framework import viewsets
from rest_framework import parsers

from drf_yasg import openapi
from drf_yasg.app_settings import swagger_settings
from drf_yasg.utils import no_body, swagger_auto_schema
import logging

logger = logging.getLogger(__name__)
import sys

@permission_classes((AllowAny,))
class LoginUser(viewsets.ModelViewSet):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser)

    @csrf_exempt
    @swagger_auto_schema(
        operation_description="login",
        request_body=LoginSerializer)
    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            if username is None or password is None:
                return JsonResponse({'message': 'Please provide both username and password', 'success': False},
                                status=400)
            user = authenticate(username=username, password=password)
            if not user:
                return JsonResponse({'message': 'Invalid Credentials', 
                                    'success': False},
                                    status=404)
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': token.key, 'success': True},
                                status=200)
        except Exception as error:
            *_, exc_tb = sys.exc_info()
            logger.error(" Type & error: " + str(error.__repr__()) +
                        " Reason: " + str(error.__doc__) +
                        " Line No: " + str(exc_tb.tb_lineno))
            return JsonResponse({"message": "internal_server_error", 
                "more_info": str(error), 'success': False}, status=500)