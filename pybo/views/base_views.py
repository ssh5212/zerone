from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from ..models import Question, Category, Answer


def main(request):
    # return render(request, 'pybo/main.html')

    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')

    category_name = ['free', 'practice', 'portfolio', 'qna', 'notice']
    page_obj = [0 for i in range(5)]
    for i in range(5):
        category = get_object_or_404(Category, name=category_name[i])
        _question_list = Question.objects.filter(category__name=category.name)
        _question_list = _question_list.order_by('-create_date')

        paginator = Paginator(_question_list, 5)
        page_obj[i] = paginator.get_page(page)

    all_question = Question.objects.all()
    all_question = all_question.order_by('-create_date')
    paginator = Paginator(all_question, 5)
    all_question = paginator.get_page(page)

    context = {'all': all_question, 'free': page_obj[0], 'practice': page_obj[1], 'portfolio': page_obj[2], 'qna': page_obj[3], 'notice': page_obj[4]}
    return render(request, 'pybo/main.html', context)


def index(request, category_name):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')

    category = get_object_or_404(Category, name=category_name)
    _question_list = Question.objects.filter(category__name=category.name)

    # 정렬
    if so == 'recommend':
        _question_list = _question_list.order_by('-voter', '-create_date')
    elif so == 'popular':
        _question_list = _question_list.order_by('-answer', '-create_date')
    else:
        _question_list = _question_list.order_by('-create_date')

    # 검색
    if kw:
        _question_list = _question_list.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(author__username__icontains=kw) # 질문 글쓴이검색
            # Q(answer__author__username__icontains=kw) # 답글 글쓴이검색
        ).distinct()

    # 페이징 처리
    paginator = Paginator(_question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'category': category, 'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answer_list = question.answer_set.all()
    answer_list = answer_list.order_by('-voter', '-create_date')
    context = {'question': question, 'category': question.category, 'answer_list': answer_list}
    return render(request, 'pybo/question_detail.html', context)
