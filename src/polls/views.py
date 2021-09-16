from datetime import datetime

from django.contrib.auth.models import User

# Create your views here.
from django.utils.decorators import method_decorator
from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.response import Response

from .models import PollsModel, AnswerModel, QuestionModel, ChoiceModel
from .serializers import (
    AnswerSerializers,
    QuestionSerializers,
    PollsSerializer, PollsSerializersWithoutStartDate, UserInfoSerializers)


@method_decorator(name='get',
                  decorator=swagger_auto_schema(operation_summary="Получить список активных опросов", tags=['Опросы']))
class ActivePollsList(ListAPIView):
    """Получить список активных опросов"""
    serializer_class = PollsSerializer

    def get_queryset(self):
        polls = PollsModel.objects.filter(data_start__lte=datetime.now(), data_end__gte=datetime.now())
        return polls


@method_decorator(name='get',
                  decorator=swagger_auto_schema(operation_summary="Получить опрос с вопросами", tags=['Опросы']))
class GetPoll(RetrieveAPIView):
    """Получить опрос с вопросами"""
    serializer_class = PollsSerializer

    def get_queryset(self):
        polls = PollsModel.objects.filter(data_start__lte=datetime.now(), data_end__gte=datetime.now())
        return polls


class QuestionAnswer(GenericAPIView):
    """Ответить на вопрос"""
    serializer_class = AnswerSerializers

    @swagger_auto_schema(
        operation_summary="Ответить на вопрос",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['answers', 'user_id', 'poll_id'],
            properties={
                'user_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'poll_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                'answers': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    required=['questions'],
                    properties={'questions': openapi.Schema(type=openapi.TYPE_ARRAY,
                                                            items=openapi.Schema(
                                                                type=openapi.TYPE_OBJECT,
                                                                required=['id'],
                                                                properties={
                                                                    'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                                                    'choice': openapi.Schema(
                                                                        type=openapi.TYPE_OBJECT,
                                                                        properties={
                                                                            'id': openapi.Schema(
                                                                                type=openapi.TYPE_ARRAY,
                                                                                items=openapi.Schema(
                                                                                    type=openapi.TYPE_INTEGER)),
                                                                            'text': openapi.Schema(
                                                                                type=openapi.TYPE_STRING)
                                                                        })
                                                                }
                                                            ))})
            }),
        tags=['Вопросы']
    )
    def post(self, request, format=None):
        answer = AnswerSerializers(data=request.data, context=request)
        if answer.is_valid(raise_exception=True):
            answer.save()
            return Response({'result': 'OK'})


@method_decorator(name='get',
                  decorator=swagger_auto_schema(operation_summary="Получить информацию по пройденным опросам",
                                                tags=['Пользователь']))
class UserInfo(RetrieveAPIView):
    """Получить информацию по пройденным опросам"""
    queryset = User.objects.all()
    serializer_class = UserInfoSerializers


@method_decorator(name='put', decorator=swagger_auto_schema(operation_summary="Обновить опрос", tags=['Опросы']))
@method_decorator(name='patch', decorator=swagger_auto_schema(operation_summary="Обновить опрос", tags=['Опросы']))
class UpdatePoll(UpdateAPIView):
    """Обновить опрос"""
    serializer_class = PollsSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = PollsModel.objects.all()

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            serializer_class = PollsSerializersWithoutStartDate

        return serializer_class


@method_decorator(name='post', decorator=swagger_auto_schema(operation_summary="Создать опрос", tags=['Опросы']))
class CreatePoll(CreateAPIView):
    """Создать опрос"""
    serializer_class = PollsSerializer
    permission_classes = [permissions.IsAdminUser]


@method_decorator(name='delete', decorator=swagger_auto_schema(operation_summary="Удалить опрос", tags=['Опросы']))
class DeletePoll(DestroyAPIView):
    """Удалить опрос"""
    serializer_class = PollsSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = PollsModel.objects.all()


@method_decorator(name='get',
                  decorator=swagger_auto_schema(operation_summary="Получить список вопрос", tags=['Вопросы']))
class QuestionsList(ListAPIView):
    """Получить список вопрос"""
    serializer_class = QuestionSerializers
    queryset = QuestionModel.objects.all()


@method_decorator(name='put', decorator=swagger_auto_schema(operation_summary="Обновить вопрос", tags=['Вопросы']))
@method_decorator(name='patch', decorator=swagger_auto_schema(operation_summary="Обновить вопрос", tags=['Вопросы']))
class UpdateQuestion(UpdateAPIView):
    """Обновить вопрос"""
    serializer_class = QuestionSerializers
    permission_classes = [permissions.IsAdminUser]
    queryset = QuestionModel.objects.all()


@method_decorator(name='post', decorator=swagger_auto_schema(operation_summary="Создать вопрос", tags=['Вопросы']))
class CreateQuestion(CreateAPIView):
    """Создать вопрос"""
    serializer_class = QuestionSerializers
    permission_classes = [permissions.IsAdminUser]


@method_decorator(name='delete', decorator=swagger_auto_schema(operation_summary="Удалить вопрос", tags=['Вопросы']))
class DeleteQuestion(DestroyAPIView):
    """Удалить вопрос"""
    serializer_class = QuestionSerializers
    permission_classes = [permissions.IsAdminUser]
    queryset = QuestionModel.objects.all()
