from datetime import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from .models import PollsModel, AnswerModel, QuestionModel, ChoiceModel
from .serializers import (
    AnswerSerializers,
    QuestionSerializers,
    PollsSerializer)


class GetPolls(GenericAPIView):
    """Получить список активных опросов"""
    serializer_class = PollsSerializer

    def get(self, request, format=None):
        polls = PollsModel.objects.filter(data_start__gte=datetime.now())
        active_polls = self.serializer_class(polls, many=True)
        return Response(active_polls.data)

class PollsListView(ListAPIView):
    """Список опросов"""
    serializer_class = PollsSerializer


class PollsDetailView(RetrieveAPIView):
    """Список опросов"""
    serializer_class = PollsSerializer


class PollsUpdateView(UpdateAPIView):
    """Список опросов"""
    serializer_class = PollsSerializer
    permission_classes = [permissions.IsAuthenticated]


class PollsCreateView(CreateAPIView):
    """Список опросов"""
    serializer_class = PollsSerializer
    permission_classes = [permissions.IsAuthenticated]


class PollsDeleteView(DestroyAPIView):
    """Список опросов"""
    serializer_class = PollsSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionListView(ListAPIView):
    """Список фильмов"""
    serializer_class = QuestionSerializers


class QuestionDetailView(RetrieveAPIView):
    """Список фильмов"""
    serializer_class = QuestionSerializers


class QuestionUpdateView(UpdateAPIView):
    """Список фильмов"""
    serializer_class = QuestionSerializers
    permission_classes = [permissions.IsAuthenticated]


class QuestionCreateView(CreateAPIView):
    """Список фильмов"""
    serializer_class = QuestionSerializers
    permission_classes = [permissions.IsAuthenticated]


class QuestionDeleteView(DestroyAPIView):
    """Список опросов"""
    serializer_class = PollsSerializer
    permission_classes = [permissions.IsAuthenticated]


class AnswerListView(ListAPIView):
    """Список фильмов"""
    serializer_class = QuestionSerializers


class AnswerDetailView(RetrieveAPIView):
    """Список фильмов"""
    serializer_class = QuestionSerializers


class AnswerUpdateView(UpdateAPIView):
    """Список фильмов"""
    serializer_class = QuestionSerializers
    permission_classes = [permissions.IsAuthenticated]


class AnswerCreateView(CreateAPIView):
    """Список фильмов"""
    serializer_class = QuestionSerializers
    permission_classes = [permissions.IsAuthenticated]


class AnswerDeleteView(DestroyAPIView):
    """Список опросов"""
    serializer_class = PollsSerializer
    permission_classes = [permissions.IsAuthenticated]



