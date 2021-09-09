from django.urls import path
from .views import ActivePollsList, UpdatePoll, CreatePoll, DeletePoll, QuestionsList, UpdateQuestion, CreateQuestion, \
    DeleteQuestion, GetPoll, QuestionAnswer

urlpatterns = [
    path('polls/', ActivePollsList.as_view(), name='active_polls'),
    path('polls/update', UpdatePoll.as_view(), name='update_polls'),
    path('polls/create', CreatePoll.as_view(), name='create_polls'),
    path('polls/delete', DeletePoll.as_view(), name='delete_polls'),
    path('polls/<int:pk>/', GetPoll.as_view(), name='poll_detail'),
    path('questions/', QuestionsList.as_view(), name='list_questions'),
    path('questions/update', UpdateQuestion.as_view(), name='update_questions'),
    path('questions/create', CreateQuestion.as_view(), name='create_questions'),
    path('questions/delete', DeleteQuestion.as_view(), name='delete_questions'),
    path('answer', QuestionAnswer.as_view(), name='answer_questions'),

]
