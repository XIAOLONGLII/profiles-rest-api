""" 1. add get import"""
from rest_framework.views import APIView
from rest_framework.response import Response
""" 2. add post import"""
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """1. Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features
            Http request, will call the get()
        """
        an_apiview = [
        'Uses HTTP methods as fuction (get, post, patch, put, delete)',
        'Is similar to a traditional Djaon View',
        'Hello NYC',
        'Hello world',
        'Hello tokyo',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    """2. post """
    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello{name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
