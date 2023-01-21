import email
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from django.core.mail import send_mail


@api_view(['POST'])
def individual_mail(request):
    subject = request.data['subject']
    message = request.data['message']
    email_from = settings.EMAIL_HOST_USER
    recipient_list = request.data['email']
    send_mail(subject, message, email_from, [recipient_list])
    return Response("email Sent")

