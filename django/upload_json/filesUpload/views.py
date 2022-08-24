from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from rest_framework import parsers

import logging
import sys
import json

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework import viewsets

from drf_yasg import openapi
from drf_yasg.app_settings import swagger_settings
from drf_yasg.utils import no_body, swagger_auto_schema

from .serializers import fileDataRequestModel
from .models import FileData

logger = logging.getLogger(__name__)

auth_param = openapi.Parameter('Authorization', openapi.IN_HEADER, "token param", type=openapi.TYPE_STRING)
page_param = openapi.Parameter('page_number', openapi.IN_QUERY, "page number param", type=openapi.TYPE_STRING)
# Create your views here.
# @csrf_exempt
# @api_view(["POST"])
# def jsonFileUpload(request):
#     return Response(data, status=HTTP_200_OK)

class FileUpload(viewsets.ModelViewSet):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser,)

    @csrf_exempt
    @swagger_auto_schema(
        operation_description="Upload json file",
        manual_parameters=[auth_param],
        request_body=fileDataRequestModel)
    def post(self, request):
        """API to upload json file"""
        try:
            data = request.data
            json_file = data["json_file"]
            if json_file.content_type != "application/json":
                return JsonResponse({"message": "Invalid json file", "success": False}, status=400)
            json_data = json.loads(json_file.read().decode("utf-8"))
            records = []
            for row in json_data:
                records.append(FileData(userID=row["userId"], title=row["title"], body=row["body"]))
            FileData.objects.bulk_create(records)
            return JsonResponse({"message": "success", "success": True}, status=200)
        except Exception as error:
            *_, exc_tb = sys.exc_info()
            logger.error(" Type & error: " + str(error.__repr__()) +
                        " Reason: " + str(error.__doc__) +
                        " Line No: " + str(exc_tb.tb_lineno))
            return JsonResponse({"message": "internal_server_error", 
                "more_info": str(error), 'success': False}, status=500)

class ViewUploadedData(viewsets.ModelViewSet):
    
    @csrf_exempt
    @swagger_auto_schema(
        operation_description="View Uploaded Data",
        manual_parameters=[auth_param, page_param])
    def get(self, request):
        try:
            file_data = FileData.objects.all()
            paginator = Paginator(file_data, 20)
            page_number = request.GET.get("page_number")
            if page_number is not None:
                page_number = int(page_number)
            else:
                page_number = 1
            page = paginator.get_page(page_number)
            records = []
            for row in page:
                rec = {
                    "id": row.id,
                    "user_id": row.userID,
                    "title": row.title,
                    "body": row.body
                }
                records.append(rec)
            from pprint import pprint
            pprint(records)
            return JsonResponse({"data": records, "count": file_data.count(), "has_previous": page.has_previous(), "has_next": page.has_next(), "success": True})
        except Exception as error:
            *_, exc_tb = sys.exc_info()
            logger.error(" Type & error: " + str(error.__repr__()) +
                        " Reason: " + str(error.__doc__) +
                        " Line No: " + str(exc_tb.tb_lineno))
            return JsonResponse({"message": "internal_server_error", 
                "more_info": str(error), 'success': False}, status=500)
