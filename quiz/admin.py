from django.contrib import admin
from .models import Quiz, QuizQuestion

# Register your models here.

@admin.register(Quiz)
class CreateQuizAdmin(admin.ModelAdmin):
    list_display = ('title','category')

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'correct_answer', 'incorrect_answers')
    list_display_links = ('question', 'correct_answer', 'incorrect_answers')
    # list_filter = ('quiz',)
