from django.urls import path, include

# from core.views import PainelView, LoginView, LogoutView
from .api import urls

# app_name = 'core'

urlpatterns = [
    path('api/', include(urls))
]
