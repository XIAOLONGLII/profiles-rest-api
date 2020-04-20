from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """ Serializes a name filed for testing out API VIEW"""
    name = serializers.CharField(max_length = 10)

#model serializer will connect the userProfileModel
class userProfileSerializer(serializers.ModelSerializer):
    """serializer a user profile object"""

    class Meta: #use meta class to config the model serializer point to specific profiles_project
        model = models.UserProfile  #point to our userprofile
        fields = ('id', 'email', 'name', 'password') #filed to match serializer
        extra_kwargs = { #change password to write-only
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'} #set style, like ***** for password
            }
        }
    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user( # create a new user
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    def update(self, instance, validated_data):
        """handler updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feeditems"""
    #fields = '__all__'
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text','created_on')
        extra_kwargs = {'user_profile': {'read_only':True}}
