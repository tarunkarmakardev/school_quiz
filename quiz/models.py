from django.db import models

# Create your models here.

class Quiz(models.Model):

    title = models.CharField('Title', max_length=100)
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





 