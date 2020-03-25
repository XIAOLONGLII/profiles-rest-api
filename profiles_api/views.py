from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

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
