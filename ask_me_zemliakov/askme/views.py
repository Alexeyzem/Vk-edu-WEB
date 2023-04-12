from . import models
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import BadRequest

def index(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'index.html', context)


def question(request, question_id):
    if len(models.QUESTIONS) > question_id:
        context = {'question': models.QUESTIONS[question_id]}
        return render(request,'question.html', context)
    else:
        raise BadRequest('non-existent question')



def ask(request):
    return render(request,'ask.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def settings(request):
    return render(request,"settings.html")

def tags(request, tags_text):
    context = {'questions':[]}
    for ques in  models.QUESTIONS:
        for ques_tag in  (ques['tags']):
            if ques_tag['text']==tags_text:
                context['questions'].append(ques)
                break
    if len(context['questions']) > 0:
        return render(request,'tags.html',context)
    else:
        raise BadRequest('not founded this tags')

def hot(request):
    context = {'questions': []}
    tmp = []
    for q in models.QUESTIONS:
        tmp.append(q)
    tmp.sort(key = lambda dictionary: dictionary['like'])
    for t in tmp:
        context['questions'].insert(0, t)
    return render(request, 'hot.html', context)