# main/urls.py

from django.urls import path
from . import views

# 앱 이름을 지정하여 나중에 리디렉션 시 충돌을 방지합니다.
app_name = 'main'

urlpatterns = [
    # http://127.0.0.1:8000/main/
    path('', views.index, name='index'), 
    
    # http://127.0.0.1:8000/main/add/ 경로로 POST 요청이 오면 views.add_click 실행
    path('add/', views.add_click, name='add_click'), 
]