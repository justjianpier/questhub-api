from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

@extend_schema_view(
    post=extend_schema(
        tags=['Autenticación'],
        summary='Registrar usuario',
        description='Registra un nuevo usuario. La ruta es pública.'
    )
)
class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    
@extend_schema_view(
    post=extend_schema(
        tags=['Autenticación'],
        summary='Iniciar sesión',
        description='Obtiene access y refresh tokens.'
    )
)
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
@extend_schema(tags='Autenticación')
@extend_schema_view(
    get=extend_schema(
        summary='Obtener perfil',
        description='Obtiene el perfil del usuario autenticado'
    ),
    put=extend_schema(
        summary='Actulizar perfil',
        description='Actualiza el perfil de usuario autenticado'
    )
)

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user