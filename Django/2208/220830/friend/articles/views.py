from multiprocessing import context
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # print('이게 될까?')
    nums = [1, 5, 7, 4, 3, 2, 6]
    pick = random.choice(nums)
    foods = ['피자', '치킨', '햄버거']
    context = {
        'name': 'ljh',
        'foods': foods,
        'address': {
            'city': 'seoul'
        },
        'pick': pick
    }
    return render(request, 'index.html', context)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    # print('catch에 도달하였다')
    # print(request)
    # print(type(request))
    # print(request.GET)                  # 딕셔너리 형태
    # print(request.GET.get('message'))   

    context = {
        'myMessage': request.GET.get('message')
    }

    return render(request, 'catch.html', context)

def greeting(request, age, word):
    result = False
    if word == word[::-1]:
        result = True
    context = {
        'age': age,
        'result': result,
        'word': word,
    }
    return render(request, 'greeting.html', context)
