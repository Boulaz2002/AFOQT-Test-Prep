from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.TabularInline):  
    model = Answer
    extra = 1  # Allows adding multiple answers directly in the question form

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'category', 'difficulty')
    list_filter = ('category', 'difficulty')
    search_fields = ('text',)
    inlines = [AnswerInline]  # Allows adding answers in the same page as the question

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('text', 'question__text')
