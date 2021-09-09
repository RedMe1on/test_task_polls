from django.contrib.auth.models import User, AnonymousUser
from django.db import models


# Create your models here.

class PublicationModel(models.Model):
    """Class for data create and update"""
    data_update = models.DateField(auto_now=True, verbose_name='Дата обновления')
    data_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        abstract = True


class PollsModel(PublicationModel):
    """Model for polls"""
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание опроса', blank=True)
    data_start = models.DateTimeField(verbose_name='Дата старта',)
    data_end = models.DateTimeField(verbose_name='Дата окончания')

    def __str__(self):
        return self.title


class QuestionModel(PublicationModel):
    """Model for survey questions"""

    ONE = 'Ответ текстом'
    TWO = 'Ответ с выбором одного варианта'
    THREE = 'Ответ с выбором нескольких вариантов'
    TYPE_CHOICES = [
        (ONE, 'Ответ текстом'),
        (TWO, 'Ответ с выбором одного варианта'),
        (THREE, 'Ответ с выбором нескольких вариантов'),
    ]

    text = models.TextField(verbose_name='Текст вопроса')
    type_q = models.CharField(max_length=40, choices=TYPE_CHOICES, default=ONE)
    poll = models.ForeignKey(PollsModel, on_delete=models.CASCADE, verbose_name='Опрос', related_name='questions')

    def __str__(self):
        return self.text


class ChoiceModel(PublicationModel):
    """Model for choice """
    question = models.ForeignKey(QuestionModel, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=4096)

    def __str__(self):
        return self.title


class AnswerModel(models.Model):
    """Model for answers"""
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Пользователь', null=True)
    question = models.ForeignKey(QuestionModel, on_delete=models.DO_NOTHING, verbose_name='Вопрос')
    choice = models.ForeignKey(ChoiceModel, on_delete=models.DO_NOTHING, verbose_name='Ответ', null=True, blank=True)
    text = models.TextField(verbose_name='Текстовый ответ', null=True, blank=True)
    data_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.text


