from django.db import transaction
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT)

from celery_with_django import settings
from User.models import User
from User.serializers import EmailInputSerializer, UserModelSerializer
from User.tasks import send_mail_to_all_users


class UserListApi(GenericAPIView):
    class OutputSerializer(UserModelSerializer):
        class Meta(UserModelSerializer.Meta):
            ref_name = 'user_list_output'
            fields = ("name", "phone", "email")

    def get_queryset(self):
        return User.objects.all()

    def get(self, request, *args, **kwargs):
        return Response(self.OutputSerializer(self.get_queryset(), many=True).data, status=HTTP_200_OK)


class SendMailToUsersApi(GenericAPIView):
    class InputSerializer(EmailInputSerializer):
        class Meta:
            ref_name = 'email_subject_message_input'
    serializer_class = InputSerializer

    def get_queryset(self):
        return User.objects.all()

    @transaction.atomic
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Access input from the serializer
        email_subject = serializer.validated_data['subject']
        email_message = serializer.validated_data['message']
        reciever_mail = []
        for user in self.get_queryset():
            reciever_mail.append(user.email)
        send_mail_to_all_users.delay(
            subject=email_subject, message=email_message, sender=settings.EMAIL_HOST_USER, receiver=reciever_mail
        )
        return Response(status=HTTP_200_OK)
