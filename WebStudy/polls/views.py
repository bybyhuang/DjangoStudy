from django.http import HttpResponse
from .models import  Question
from django.template import loader
from django.shortcuts import get_object_or_404,render

# 直接返回读取出来的数据
# def index(request):
#     list = Question.objects.order_by('-pub_date')[:5]
#     output = ','.join([p.question_text for p in list])
#     return HttpResponse(output)



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    for i in latest_question_list:
        print(i.question_text)
    template = loader.get_template('index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    # list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list':list,
    # }
    # return HttpResponse(template.render(context,request))

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'detail.html',{'question':question})
    return HttpResponse("这是你请求的question_id=%s"%question_id)

# 投票
def vote(request,question_id):
    return HttpResponse("这是你请求的question_id=%s" % question_id)
    return HttpResponse("投票成功了")

