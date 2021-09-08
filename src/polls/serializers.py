from rest_framework import serializers
from .models import PollsModel, AnswerModel, QuestionModel, ChoiceModel


class PollsSerializer(serializers.ModelSerializer):
    """Serializer for polls"""

    class Meta:
        model = PollsModel
        fields = ['pk', 'title', 'description', 'data_start', 'data_end']


class QuestionSerializers(serializers.ModelSerializer):
    """Serializer for questions"""

    class Meta:
        model = QuestionModel
        fields = ['pk', 'text', 'type_q', 'poll']


class AnswerSerializers(serializers.ModelSerializer):
    """Serializer for answers"""

    class Meta:
        model = AnswerModel
        fields = ['pk', 'user', 'question', 'choice']

