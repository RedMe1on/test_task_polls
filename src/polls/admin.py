from django.contrib import admin
from .models import PollsModel, AnswerModel, QuestionModel, ChoiceModel


# Register your models here.


@admin.register(PollsModel)
class PollsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'data_start', 'data_end')
    list_display_links = ('title',)
    ordering = ('id',)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # when editing an object
            return ['data_start']
        return self.readonly_fields


@admin.register(QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'type_q', 'poll')
    list_display_links = ('text',)
    ordering = ('id',)


@admin.register(ChoiceModel)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'title')
    list_display_links = ('title',)
    ordering = ('id',)


@admin.register(AnswerModel)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'choice', 'data_created')
    list_display_links = ('question',)
    ordering = ('id',)
