
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from profiles.serializers import UserAPISerializer
from profiles.constants import ERROR_IS_NOT_DEMO_USER
from profiles.models import User

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAPISerializer
   
    @action(detail=False, methods=['post'])
    def create_from_demo_user(self, request):
        
        if not request.user.is_demo_user:
            return Response(ERROR_IS_NOT_DEMO_USER, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.create_from_demo_user(request, serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        