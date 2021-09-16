from django.urls import path
from .views import ActivePollsList, UpdatePoll, CreatePoll, DeletePoll, QuestionsList, UpdateQuestion, CreateQuestion, \
    DeleteQuestion, GetPoll, QuestionAnswer, UserInfo

urlpatterns = [
    path('polls/', ActivePollsList.as_view(), name='active_polls'),
    path('polls/create', CreatePoll.as_view(), name='create_polls'),
    path('polls/<int:pk>/update', UpdatePoll.as_view(), name='update_polls'),
    path('polls/<int:pk>/delete', DeletePoll.as_view(), name='delete_polls'),
    path('polls/<int:pk>/', GetPoll.as_view(), name='poll_detail'),
    path('questions/', QuestionsList.as_view(), name='list_questions'),
    path('questions/create', CreateQuestion.as_view(), name='create_questions'),
    path('questions/<int:pk>/update', UpdateQuestion.as_view(), name='update_questions'),
    path('questions/<int:pk>/delete', DeleteQuestion.as_view(), name='delete_questions'),
    path('answer', QuestionAnswer.as_view(), name='answer_questions'),
    path('user/<int:pk>', UserInfo.as_view(), name='info_user'),

]
