from django.urls import path
from .views import login_view, register_view, interview_get_view, interview_api_view, home_view

urlpatterns = [
    path('', home_view, name='home'), # 指向首頁
    path('login/', login_view, name='login'), # 指向登入頁
    path('register/', register_view, name='register'), # 指向註冊頁
    path('interview/', interview_get_view, name='interview'), # 指向面試頁
    path('api/interview/', interview_api_view, name='interview_api'), # 指向面試API
]

# http://127.0.0.1:8000.com/