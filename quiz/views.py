from django.shortcuts import render, redirect
from .models import QuizQuestion, Quiz, QuizScore, StudenAttemptRecord
from django.contrib import messages
import random
import requests

# Views:

def display_quiz(request, quiz_title, ques_num, reveal_correct_answer = False , allow_next_ques = False ):

    # Redirecting to results view when questions are done!
    if(ques_num>10):
        return redirect('quiz:display_quiz_results', quiz_title )
    
    quiz = Quiz.objects.get(title = quiz_title)
    previously_attempted = False

    try:
        previously_attempted = StudenAttemptRecord.objects.filter(quiz = quiz, student = request.user).exists()
    except:
        pass
    
    if(previously_attempted):
        return redirect('quiz:already_attempted')

    # Fixing ques_num to match queryset index number
    ques_num = ques_num-1
    # Fetching data for the ques_num
    question_objects = QuizQuestion.objects.filter(quiz__title = quiz_title)
    question_object = question_objects[ques_num]
    correct_answer = question_objects[ques_num].correct_answer
    incorrect_answers = question_objects[ques_num].incorrect_answers

    
    # Create list of choices by casting the answers into string and splitting the string at ','
    answer_choices = (str(correct_answer) + "," + str(incorrect_answers)).split(",")
    random.shuffle(answer_choices)
    
    # Handling POST request when answer is submitted:    
    if request.method == "POST":   
        try:
            selected_answer = request.POST['selected_answer']
        except:
            messages.error(request, "No answer selected, you'll be marked 0")
            reveal_correct_answer = True
            allow_next_ques = True
            return redirect('quiz:display_quiz', quiz_title, ques_num+1, reveal_correct_answer, allow_next_ques )
        

        allow_next_ques = True
        if (correct_answer==selected_answer):
            messages.success(request, "Correct answer!")
            marks = 1
        else:
            messages.error(request, "Incorrect answer!")
            reveal_correct_answer = True
            marks = 0
        
        # Saving student record in Database:
        quiz = Quiz.objects.get(title = quiz_title)
        QuizScore.objects.create(student = request.user, quiz = quiz, question = question_object.question, selected_answer = selected_answer, correct_answer = correct_answer, marks = marks)
       
    context = {
        'quiz_title': quiz_title,
        'ques_num': ques_num+1,
        'next': ques_num+2,
        'answer_choices': answer_choices,
        'question_object': question_object,
        'correct_answer': correct_answer,

        'reveal_correct_answer': reveal_correct_answer,
        'allow_next_ques':  allow_next_ques,
    }

    return render(request, "quiz/display_quiz_question.html", context)


def create_quiz(request):

    # Fetching categories from 'Open Trivia Database'
    response = requests.get('https://opentdb.com/api_category.php')
    data = response.json()
    categories = []
    for category in data['trivia_categories']:
        categories.append(category)
    
    
    if request.method == 'POST':
        selected_category = request.POST['selected_category']
        quiz_title = request.POST['quiz_title']

        if (not quiz_title or selected_category=="Open this menu"):
            messages.error(request, "Make sure to enter a name and select a category!")
            return redirect('quiz:create_quiz')

        # Creating new quiz
        try:
            new_quiz = Quiz.objects.create(title = quiz_title, category= selected_category)
        except:
            messages.error(request, "Name already taken!")
            return redirect('quiz:create_quiz')

        # Fetching data for the selected category:
        response = requests.get(f'https://opentdb.com/api.php?amount=10&type=multiple&category={selected_category}')
        print(f'https://opentdb.com/api.php?amount=10&type=multiple&category={selected_category}')
        data = response.json()
        data_dict_list = []

        for entry in data['results']:

            # Making comman seprated string for incorrect answers
            incorrect_answers_string = ''
            incorrect_answers_string = ','.join(entry['incorrect_answers'])

            # Saving questions for quiz = new_quiz:
            
            questions = QuizQuestion(quiz = new_quiz, question = entry['question'], correct_answer = entry['correct_answer'], incorrect_answers = incorrect_answers_string  )
            questions.save()
    
    quizzes = Quiz.objects.all()

    context = {
        "categories": categories,
        'quizzes': quizzes,
        
    }

    return render(request, "quiz/create_quiz_question.html", context)


def display_quiz_results(request, quiz_title):

    quiz = Quiz.objects.get(title=quiz_title)
    question_objects = quiz.quizscore_set.all().filter(student = request.user)
    total_marks = 0
    result = False

    for item in question_objects:
        total_marks += item.marks

    if total_marks>6:
        result = True
  
    if request.method == 'POST':
        print(request.POST['time_taken_formatted'])
        StudenAttemptRecord.objects.create(student = request.user, quiz = quiz , time_taken = request.POST['time_taken_formatted'])

    context = {
        'question_objects': question_objects,
        'total_marks':total_marks,
        'result': result,

    }

    return render(request, "quiz/display_quiz_results.html", context)


def already_attempted(request):
    return render(request, "quiz/already_attempted.html")