from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializes a name filed for testing out API VIEW"""
    name = serializers.CharField(max_length = 10)
