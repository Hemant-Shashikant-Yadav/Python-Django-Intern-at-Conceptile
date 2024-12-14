from django.contrib import admin
from .models import Question, QuizSession


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Customize admin interface for Question model
    """
    list_display = ('text', 'correct_answer')
    search_fields = ('text',)

@admin.register(QuizSession)
class QuizSessionAdmin(admin.ModelAdmin):
    """
    Customize admin interface for QuizSession model
    """
    list_display = ('id', 'total_questions', 'correct_answers', 'created_at')
    readonly_fields = ('id', 'created_at')