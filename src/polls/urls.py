from django.urls import path
from .views import GetPolls

urlpatterns = [
    path('polls/', GetPolls.as_view(), name='active_polls'),


]