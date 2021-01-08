from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Quiz(models.Model):

    title = models.CharField('Title', max_length=100, unique=True)
    category = models.CharField('Category', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Create a Quiz'
        verbose_name_plural = 'Create a Quiz'

    def __str__(self):
        return self.title

class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField('quesiton',max_length=255)
    correct_answer = models.CharField('Correct answer', max_length=20)
    incorrect_answers = models.CharField('Incorrect answers (comma seperated)', max_length=20)

    class Meta:
        verbose_name = 'Create Quiz questions'
        verbose_name_plural = 'Create Quiz questions'

    def __str__(self):
        return self.question


class QuizScore(models.Model):

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField('Quesiton',max_length=255)
    selected_answer = models.CharField('Selected answer',max_length=100)
    correct_answer = models.CharField('Correct answer', max_length=100)
    marks = models.IntegerField('Marks', blank=True, null=True)
    

    class Meta:
        verbose_name = "Student's Score"
        verbose_name_plural = "Student's Score"

    def __str__(self):
        return self.student.first_name


class StudenAttemptRecord(models.Model):

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    time_taken = models.CharField('Time Taken to complete the test', max_length=100)

    def __str__(self):
        return self.student.first_name



 