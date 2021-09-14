from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from .models import PollsModel, AnswerModel, QuestionModel, ChoiceModel


class ChoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChoiceModel
        exclude = ['question', ]


class QuestionSerializers(serializers.ModelSerializer):
    """Serializer for questions"""
    choices = ChoiceSerializers(many=True, read_only=True)

    class Meta:
        model = QuestionModel
        fields = ['pk', 'text', 'type_q', 'poll', 'choices']


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
    poll_id = serializers.IntegerField(min_value=1)
    answers = serializers.JSONField()
    user_id = serializers.IntegerField(required=False, min_value=1)

    def validate_answers(self, answers):
        if not answers:
            raise serializers.ValidationError("Ответ не должен быть пустым")
        return answers

    def validate_poll_id(self, poll_id):
        if not poll_id:
            raise serializers.ValidationError("poll_id не должен быть пустым")
        return poll_id

    def validate_choice_question(self, choice: ChoiceModel, question: QuestionModel) -> bool:
        """Валидатор принадлежности выбора к вопросу"""
        if choice.question != question:
            raise serializers.ValidationError("Вариант ответа не принадлежит вопросу")
        return True

    def validate_poll_question(self, poll_id: int, question: QuestionModel) -> bool:
        """Валидатор принадлежности выбора к вопросу"""
        if question.poll.pk != poll_id:
            raise serializers.ValidationError("Вопрос не принадлежит опросу")
        return True

    def save(self):
        answers = self.data['answers']
        user_id = self.data['user_id']
        poll_id = self.data['poll_id']

        try:
            user = User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            user = None  # или создать, если нужен анонимный юзер с id, чтобы видеть, что ответил один и тот же

        for question_id in answers:
            question = QuestionModel.objects.get(pk=question_id)
            if self.validate_poll_question(poll_id=poll_id, question=question):
                choices = answers[question_id]
                if question.type_q == QuestionModel.ONE:
                    AnswerModel(user=user, question=question, text=choices).save()
                else:
                    for choice_id in choices:
                        choice = ChoiceModel.objects.get(pk=choice_id)
                        if self.validate_choice_question(choice=choice, question=question):
                            AnswerModel(user=user, question=question, choice=choice).save()


class AnswerSerializersInfo(serializers.ModelSerializer):
    question = QuestionSerializers(read_only=True)

    class Meta:
        model = AnswerModel
        fields = ['question', 'choice', 'text', 'data_created']


class UserInfoSerializers(serializers.ModelSerializer):
    """Get user info by polls and answer"""
    answers = AnswerSerializersInfo(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['pk', 'username', 'answers']
