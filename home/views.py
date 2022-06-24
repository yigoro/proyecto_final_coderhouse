from django.shortcuts import render
from django.db.models import Q

from empleo.models import Empleo
from user.models import Avatar

def index(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    empleos = Empleo.objects.all()
    context_dict.update({
        'empleos': empleos,
    })
    print('context_dict: ', context_dict)
    return render(
        request=request,
        context=context_dict,
        template_name="home/main.html"
    )


def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {"url": avatars[0].image.url}
    return {}


def search(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    if request.GET['search_param']:
        search_param = request.GET['search_param']
        query = Q(empresa__contains=search_param)
        empleos = Empleo.objects.filter(query)
        context_dict.update({
            'empleos': empleos,
            'search_param': search_param,
        })
    return render(
        request=request,
        context=context_dict,
        template_name="home/main.html",
    )


def AboutSebaView(request):
    return render(
        request=request,
        template_name="home/seba.html",
    )

def AboutStephyView(request):
    return render(
        request=request,
        template_name="home/stephy.html",
    )