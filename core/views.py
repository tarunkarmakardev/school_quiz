from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from quiz.models import Quiz

# Create your views here.
@login_required(login_url='accounts:loginUser')
def index(request):

    quizzes = Quiz.objects.all()

    context ={
        'quizzes':quizzes

    }
    return render(request, "core/index.html", context)