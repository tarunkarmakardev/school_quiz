from django.contrib import admin
from .models import Quiz, QuizQuestion, QuizScore, StudenAttemptRecord

# Register your models here.

@admin.register(Quiz)
class CreateQuizAdmin(admin.ModelAdmin):
    list_display = ('title','category')
    list_filter = ('category',)

@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'correct_answer', 'incorrect_answers')
    list_display_links = ('question', 'correct_answer', 'incorrect_answers')
    # list_filter = ('quiz',)

@admin.register(QuizScore)
class QuizScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'question', 'marks', 'correct_answer', 'selected_answer')
    list_filter = ('student',)
    list_display_links = ('student', 'question', 'marks', 'correct_answer', 'selected_answer')

@admin.register(StudenAttemptRecord)
class StudenAttemptRecordAdmin(admin.ModelAdmin):
    pass
    # list_display = ('student', 'question', 'marks', 'correct_answer', 'selected_answer')
    # list_filter = ('student',)
    # list_display_links = ('student', 'question', 'marks', 'correct_answer', 'selected_answer')