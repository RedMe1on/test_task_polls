from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from .models import PollsModel, AnswerModel, QuestionModel, ChoiceModel


class QuestionSerializers(serializers.ModelSerializer):
    """Serializer for questions"""

    class Meta:
        model = QuestionModel
        fields = ['pk', 'text', 'type_q', 'poll']


class PollsSerializer(serializers.ModelSerializer):
    """Serializer for polls"""
    questions = QuestionSerializers(many=True, read_only=True)

    class Meta:
        model = PollsModel
        fields = ['pk', 'title', 'description', 'data_start', 'data_end', 'questions']


class PollsSerializersWithoutStartDate(serializers.ModelSerializer):
    """Serializer for polls without start_date for update"""

    class Meta:
        model = PollsModel
        fields = ['pk', 'title', 'description', 'data_end']


class AnswerSerializers(serializers.Serializer):
    """Serializer for answers"""
    answers = serializers.JSONField()
    user_id = serializers.IntegerField(required=False)

    def validate_answers(self, answers):
        if not answers:
            raise serializers.ValidationError("Ответ не должен быть пустым")
        return answers

    def validate_choice_question(self, choice: ChoiceModel, question: QuestionModel) -> bool:
        """Валидатор принадлежности выбора к вопросу"""
        if choice.question != question:
            raise serializers.ValidationError("Ответ не должен быть пустым")
        return True

    def save(self):
        answers = self.data['answers']
        user_id = self.data['user_id']
        try:
            user = User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            user = None

        for question_id in answers:
            question = QuestionModel.objects.get(pk=question_id)
            choices = answers[question_id]
            if question.type_q == QuestionModel.ONE:
                AnswerModel(user=user, question=question, text=choices).save()
            else:
                for choice_id in choices:
                    choice = ChoiceModel.objects.get(pk=choice_id)
                    if self.validate_choice_question(choice=choice, question=question):
                        AnswerModel(user=user, question=question, choice=choice).save()
