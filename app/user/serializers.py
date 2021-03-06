from django.contrib.auth import get_user_model,authenticate
from django.utils.translation import ugettext_lazy as _ #whenever we output a message to screen,its better to pass them through this traslation.so that if we add another language in future.it is easy to translate text

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for users object"""

    class Meta:
        model=get_user_model()
        fields=('email','password','name')
        extra_kwargs={'password':{'write_only':True,'min_length':5}}

    def create(self,validated_data):#overide
        """create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self,instance,validated_data):
        """update a user,setting the password correctly and return it"""
        password=validated_data.pop('password',None)
        user=super().update(instance,validated_data)

        if password:
            user.set_password(password)
            user.save()
            
        return user

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email=serializers.CharField()
    password=serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace=False
    )

    def validate(self,attrs):
        """validate and authenticate the user"""
        email=attrs.get('email')
        password=attrs.get('password')

        user=authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg=_('Unable to authenticate with provided credentials') #message passing through translation function
            raise serializers.ValidationError(msg,code='authentication')

        attrs['user']=user
        return attrs #when you override validate functionnyou must return values at the end

