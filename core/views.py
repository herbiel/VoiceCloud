from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Extension
from .serializers import ExtensionSerializer


class ExtensionListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        extensions = Extension.objects.filter(number = request.user.id)
        serializer = ExtensionSerializer(extensions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'number': request.data.get('number'),
            'password': request.data.get('password'),
            'displayname': request.user.id,
            'domain':request.data.get('domain'),
            'enable':request.data.get('enable'),
            'displayname':request.data.get('displayname')
        }
        serializer = ExtensionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)