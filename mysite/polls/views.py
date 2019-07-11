from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
import json
from django.shortcuts import get_object_or_404, render
def index(request):
    latest_question_list = Question.objects.order_by('-quest_Type')[:5]
    ret_obj={}
    for q in latest_question_list:
        ret_obj[q.quest_Type]=q.question_text

    #output = ', '.join([q.question_text for q in latest_question_list])
    #json_data=json.dumps(ret_obj)
    return HttpResponse(str(ret_obj))

    #return HttpResponse("Hello, world. You're at the polls index.")

def question_Type_byid(request,question_id):
   # obj = Question.objects.get(pk=question_id)
    #return HttpResponse(str(obj))
   question = get_object_or_404(Question, pk=question_id)
   return HttpResponse(question)


from django.http import Http404

def detail(request, question_id):
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404("Question does not exist")

        return HttpResponse(str(question))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



def index_html(request):
    latest_question_list = Question.objects.order_by('-quest_Type')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)