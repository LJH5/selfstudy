from django.urls import path
from . import views     # 현재위치(자기자신)으로부터  views 가져오기

app_name = 'movies'
urlpatterns = [
    path('details/', views.details, name='details')
]
