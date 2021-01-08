from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('display_quiz/<str:quiz_title>/<int:ques_num>', views.display_quiz, name = 'display_quiz'),
    path('display_quiz/<str:quiz_title>/<int:ques_num>/<str:reveal_correct_answer>/<str:allow_next_ques>', views.display_quiz, name = 'display_quiz'),
    path('create_quiz/', views.create_quiz, name = 'create_quiz'),
    path('display_quiz_results/<str:quiz_title>', views.display_quiz_results, name = 'display_quiz_results'),
    path('already_attempted', views.already_attempted, name = 'already_attempted'),
]