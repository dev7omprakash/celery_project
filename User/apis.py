# Copyright 2023 licenser.author
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from rest_framework.generics import GenericAPIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_204_NO_CONTENT,
)
from User.models import User
from User.tasks import send_mail_to_all_users


class UserListApi(GenericAPIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.CharField()
        name = serializers.CharField()
        phone = serializers.CharField()
        email = serializers.EmailField()
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return Response(self.OutputSerializer(self.get_queryset(), many=True).data, status=HTTP_200_OK)


class SendMailToUsersApi(GenericAPIView):
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        send_mail_to_all_users.delay()
        return Response(status=HTTP_200_OK)
