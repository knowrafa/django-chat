from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from rest_framework import status, mixins, viewsets
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework_jwt.utils import jwt_encode_handler


class ChatView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'chat.html'
    permission_classes = []

    def get(self, request):
        return Response(status=status.HTTP_200_OK)
