from rest_framework import serializers

class fileDataRequestModel(serializers.Serializer):
    json_file = serializers.FileField(required=True, )
