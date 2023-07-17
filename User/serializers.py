from rest_framework import serializers

from User.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class EmailInputSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=100, required=True)
    message = serializers.CharField(max_length=200, required=True)

    class Meta:
        pass
