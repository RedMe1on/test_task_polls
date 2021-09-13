from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.response import Response

from .models import PollsModel, AnswerModel, QuestionModel, ChoiceModel
from .serializers import (
    AnswerSerializers,
    QuestionSerializers,
    PollsSerializer, PollsSerializersWithoutStartDate, UserInfoSerializers)


class ActivePollsList(ListAPIView):
    """Получить список активных опросов"""
    serializer_class = PollsSerializer

    def get_queryset(self):
        polls = PollsModel.objects.filter(data_start__lte=datetime.now(), data_end__gte=datetime.now())
        return polls


class GetPoll(RetrieveAPIView):
    """Получить опрос с вопросами"""
    serializer_class = PollsSerializer

    def get_queryset(self):
        polls = PollsModel.objects.filter(data_start__lte=datetime.now(), data_end__gte=datetime.now())
        return polls


class QuestionAnswer(GenericAPIView):
    """Ответить на вопрос"""
    serializer_class = AnswerSerializers

    def post(self, request, format=None):
        answer = AnswerSerializers(data=request.data, context=request)
        if answer.is_valid(raise_exception=True):
            answer.save()
            return Response({'result': 'OK'})


class UserInfo(RetrieveAPIView):
    """Получить информацию по пройденным опросам"""
    queryset = User.objects.all()
    serializer_class = UserInfoSerializers


class UpdatePoll(UpdateAPIView):
    """Обновить опрос"""
    serializer_class = PollsSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            serializer_class = PollsSerializersWithoutStartDate

        return serializer_class


class CreatePoll(CreateAPIView):
    """Создать опрос"""
    serializer_class = PollsSerializer
    permission_classes = [permissions.IsAdminUser]


class DeletePoll(DestroyAPIView):
    """Удалить опрос"""
    serializer_class = PollsSerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionsList(ListAPIView):
    """Получить список вопрос"""
    serializer_class = QuestionSerializers


class UpdateQuestion(UpdateAPIView):
    """Обновить вопрос"""
    serializer_class = QuestionSerializers
    permission_classes = [permissions.IsAdminUser]


class CreateQuestion(CreateAPIView):
    """Создать вопрос"""
    serializer_class = QuestionSerializers
    permission_classes = [permissions.IsAdminUser]


class DeleteQuestion(DestroyAPIView):
    """Удалить вопрос"""
    serializer_class = QuestionSerializers
    permission_classes = [permissions.IsAdminUser]
