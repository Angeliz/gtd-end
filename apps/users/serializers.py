from django.contrib.auth import get_user_model
from rest_framework import serializers

# from users.models import Users
Users = get_user_model()

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'id', 'user_info')


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'id', 'user_info')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'user_info': instance.user_info
        }


class UsersRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'id', 'user_info')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'user_info': instance.user_info
        }


class UsersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'password', 'user_info')

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.user_info = validated_data.get('user_info', instance.user_info)
        instance.save()
        return instance


class UsersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'password')

    def create(self, validated_data):
        user = super(UsersCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_representation(self, instance):
        return {
            'username': instance.username,
            'id': instance.id
        }
