""" 1. add get import"""
from rest_framework.views import APIView
from rest_framework.response import Response
""" 2. add post import"""
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers
from profiles_api import models


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

    """3. put """
    def put(self, request, pk = None):
        """ Handle updating an object """
        return Response({'method': 'PUT'})
    """4. patch """
    def patch(self, request, pk = None):
        """ Handle a partial updating an object """
        return Response({'method': 'PATCH'})
    """5. delete """
    def delete(self, request, pk = None):
        """ Handle a partial updating an object """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """return a hello message"""
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using routers',
            'Provide more fuctionlitu with less code',
        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def creat(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response (
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        return Response({'http_method': 'GET'})
    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})
    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})
    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet): # connect serializer class, provide queryse
    """handel creating and updating profiles"""
    serializer_class = serializers.userProfileSerializer
    queryset = models.UserProfile.objects.all()
