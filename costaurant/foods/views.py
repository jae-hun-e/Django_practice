from django.shortcuts import render
from datetime import datetime


def index(request):
    today = datetime.today().date()
    context = {"date": today}
    return render(request, 'foods/index.html', context=context)


def food_detail(req, food):
    context = {'name': food}
    return render(req, 'foods/detail.html', context=context)