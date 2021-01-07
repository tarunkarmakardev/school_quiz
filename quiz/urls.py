from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('display_quiz/<int:id>', views.display_quiz, name = 'display_quiz'),
    path('create_quiz/', views.create_quiz, name = 'create_quiz'),
]