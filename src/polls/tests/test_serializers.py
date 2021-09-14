from datetime import datetime, timedelta

from django.test import TestCase

from polls.models import PollsModel, QuestionModel, ChoiceModel
from polls.serializers import ChoiceSerializers, QuestionSerializers


class ChoiceSerializersTestCase(TestCase):
    """Test case for choice serializer"""

    def setUp(self) -> None:
        data_end = datetime.now() + timedelta(days=1, hours=3)
        data_start = datetime.now()
        poll = PollsModel.objects.create(id=1, title='Poll 1', data_end=data_end, data_start=data_start)
        question = QuestionModel.objects.create(id=1, text='Question 1', poll=poll)
        self.choice_attributes = {
            'question': question,
            'title': 'TestChoice'
        }

        self.choice = ChoiceModel.objects.create(**self.choice_attributes)
        self.serializer = ChoiceSerializers(instance=self.choice)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'title', 'data_update', 'data_created'})

    def test_title_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['title'], self.choice_attributes['title'])


class QuestionSerializersTestCase(TestCase):
    """Test case for choice serializer"""

    def setUp(self) -> None:
        data_end = datetime.now() + timedelta(days=1, hours=3)
        data_start = datetime.now()
        poll = PollsModel.objects.create(id=1, title='Poll 1', data_end=data_end, data_start=data_start)
        self.question_attributes = {
            'poll': poll,
            'text': 'TestChoice'
        }

        self.choice = QuestionModel.objects.create(**self.question_attributes)
        self.serializer = QuestionSerializers(instance=self.choice)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'pk', 'text', 'type_q', 'poll', 'choices'})

    def test_poll_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['poll'], 1)

    def test_text_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['text'], self.question_attributes['text'])
