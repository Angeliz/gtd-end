from rest_framework import serializers

from users.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_name', 'user_id', 'user_info')


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_name', 'user_id', 'user_info')

    def to_representation(self, instance):
        return {
            'user_id': instance.user_id,
            'user_name': instance.user_name,
            'user_info': instance.user_info
        }


class UsersRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_name', 'user_id', 'user_info')

    def to_representation(self, instance):
        return {
            'user_id': instance.user_id,
            'user_name': instance.user_name,
            'user_info': instance.user_info
        }


class UsersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_name', 'user_password', 'user_info')

    def update(self, instance, validated_data):
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.user_password = validated_data.get('user_password', instance.user_password)
        instance.user_info = validated_data.get('user_info', instance.user_info)
        instance.save()
        return instance


class UsersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_name', 'user_password')

    def create(self, validated_data):
        return Users.objects.create(**validated_data)

    def to_representation(self, instance):
        return {
            'user_name': instance.user_name,
            'user_id': instance.user_id
        }
