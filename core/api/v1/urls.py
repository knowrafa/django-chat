from django.urls import path, include
# from core.views import PainelView, LoginView, LogoutView
from rest_framework_nested import routers
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from core.api.v1 import views

app_name = 'core'

router = routers.DefaultRouter()

# router.register('chat', views.ChatView, basename='chat')

urlpatterns = [
    path('chat/', views.ChatView.as_view(), name='chat'),
    path('', include(router.urls)),
    path('login/', LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
