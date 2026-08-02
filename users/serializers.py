from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'phone', 'address')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }
    
    def validate_email(self, value):
        user = get_user_model()
        if user.objects.filter(email=value).exists():
            raise serializers.ValidationError('El email ya se encuentra registrado')
        return value
    
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        return token