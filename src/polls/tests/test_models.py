from datetime import datetime, timedelta

from django.test import TestCase

from polls.models import PollsModel, QuestionModel, ChoiceModel


class PollsModelTestCase(TestCase):
    """Test for model Polls"""

    @classmethod
    def setUpTestData(cls):
        data_end = datetime.now() + timedelta(days=1, hours=3)
        data_start = datetime.now()
        PollsModel.objects.create(id=1, title='Poll 1', data_end=data_end, data_start=data_start)

    def test_str_method(self):
        category = PollsModel.objects.get(id=1)
        expected_object_name = category.title
        self.assertEqual(str(category), expected_object_name)


class QuestionModelTestCase(TestCase):
    """Test for model QuestionModel"""

    @classmethod
    def setUpTestData(cls):
        data_end = datetime.now() + timedelta(days=1, hours=3)
        data_start = datetime.now()
        poll = PollsModel.objects.create(id=1, title='Poll 1', data_end=data_end, data_start=data_start)
        QuestionModel.objects.create(id=1, text='Question 1', poll=poll)

    def test_str_method(self):
        question = QuestionModel.objects.get(id=1)
        expected_object_name = question.text
        self.assertEqual(str(question), expected_object_name)


class ChoiceModelTestCase(TestCase):
    """Test for model ChoiceModel"""

    @classmethod
    def setUpTestData(cls):
        data_end = datetime.now() + timedelta(days=1, hours=3)
        data_start = datetime.now()
        poll = PollsModel.objects.create(id=1, title='Poll 1', data_end=data_end, data_start=data_start)
        question = QuestionModel.objects.create(id=1, text='Question 1', poll=poll)
        ChoiceModel.objects.create(id=1, title='Choice 1', question=question)

    def test_str_method(self):
        choice = ChoiceModel.objects.get(id=1)
        expected_object_name = choice.title
        self.assertEqual(str(choice), expected_object_name)
