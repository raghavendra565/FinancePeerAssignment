from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(help_text='username', required=True)
    password = serializers.CharField(help_text='password', required=True)

