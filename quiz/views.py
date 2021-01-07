from django.shortcuts import render
from .models import QuizQuestion, Quiz
from django.contrib import messages
import random
import requests

# Create your views here.

def display_quiz(request, id):

    question_objects = QuizQuestion.objects.all()
    question_object = question_objects[id-1]
    correct_answer = question_objects[id-1].correct_answer
    incorrect_answers = question_objects[id-1].incorrect_answers
    submitted = False

    reveal_correct_answer= False
    allow_next_ques = False

    # Create list of choices by casting the answers into string and splitting the string at ','
    
    answer_choices = (str(correct_answer) + "," + str(incorrect_answers)).split(",")
    random.shuffle(answer_choices)
        
        
           
    if request.method == "POST":
        allow_next_ques = True
        selected_answer = request.POST['selected_answer']
        if (correct_answer==selected_answer):
            messages.success(request, "Correct answer!")
        else:
            messages.error(request, "Incorrect answer!")
            reveal_correct_answer = True
        
    
    
    


    context = {
        'ques_num': id,
        'next': id+1,
        'answer_choices': answer_choices,
        'question_object': question_object,
        'reveal_correct_answer': reveal_correct_answer,
        'correct_answer': correct_answer,
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

        # Creating new quiz
        new_quiz = Quiz.objects.create(title = quiz_title, category= selected_category)

        # Fetching data for the selected category:
        response = requests.get(f'https://opentdb.com/api.php?amount=10&type=multiple&category={selected_category}')
        data = response.json()
        data_dict_list = []

        for entry in data['results']:

            # Making comman seprated string for incorrect answers
            incorrect_answers_string = ''
            incorrect_answers_string = ','.join(entry['incorrect_answers'])

            # Saving questions for quiz = new_quiz:
            
            questions = QuizQuestion(quiz = new_quiz, question = entry['question'], correct_answer = entry['correct_answer'], incorrect_answers = incorrect_answers_string  )
            questions.save()


            
       



    context = {
        "categories": categories,
        
    }

    return render(request, "quiz/create_quiz_question.html", context)