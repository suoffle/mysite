from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
import logging
logger = logging.getLogger('mysite')

from ..models import Question

def index(request):
    logger.info("INFO 레벨로 출력")
    page=request.GET.get('page',1)
    kw=request.GET.get('kw','')
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list=question_list.filter(
            Q(subject__icontains=kw)|
            Q(content__icontains=kw)|
            Q(answer__content__icontains=kw)|
            Q(author__username__icontains=kw)|
            Q(answer__author__username__icontains=kw)
        ).distinct()

    paginator = Paginator(question_list, 10)
    page_obj=paginator.get_page(page)
    context = {'question_list': page_obj, 'page':page, 'kw':kw}
    return render(request, 'mysite/question_list.html', context)

    #return HttpResponse("Hello, world. polls index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'mysite/question_detail.html', context)
