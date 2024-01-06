import json
import random
import string
import time
from account.models import UserModel
from django.http import JsonResponse
from django.views.generic import View
from django.core.mail import send_mail
from django.conf import settings


class ForgotPasswordView(View):

    @staticmethod
    def send_email(name, email, password):
        send_mail(
            name,
            f'Hello {name} your password is {password}, please don\'t forgot your password!!!',
            settings.EMAIL_HOST_USER,
            [email],
        )

    def get_new_password(self, user):
        password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        self.send_email(user.username, user.email, password)
        return password

    def get(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'ok': False, 'message': 'you are not logged in'})
        password = self.get_new_password(request.user)
        request.session['password'] = password
        request.session['time'] = time.time()
        return JsonResponse({'ok': True, 'message': 'please check your email'})

    def post(self, request):
        data = json.loads(request.body)
        if not (data.get('username', False) and data.get('email', False)):
            return JsonResponse({'ok': False, 'message': 'enter your email please'})
        if not UserModel.objects.filter(username=data.get('username'), email=data.get('email')).exists():
            return JsonResponse({'ok': False, 'message': 'user not found'})
        password = self.get_new_password(UserModel.objects.get(username=data.get('username')))
        request.session['password'] = password
        return JsonResponse({'ok': True, 'message': 'please check your email'})

    @staticmethod
    def put(request):
        data = json.loads(request.body)
        if not (data.get('username', False) and data.get('email', False)):
            return JsonResponse({'ok': False, 'message': 'username and email please'})
        if not UserModel.objects.filter(username=data.get('username'), email=data.get('email')).exists():
            return JsonResponse({'ok': False, 'message': 'user not found'})
        if not data.get('password', False):
            return JsonResponse({'ok': False, 'message': 'enter your password please'})
        if data['password'] != request.session['password']:
            return JsonResponse({'ok': False, 'message': 'wrong password'})
        if time.time() - request.session['time'] < 60:
            return JsonResponse({'ok': False, 'message': 'time limit exceeded'})
        user = request.user if request.user.is_authenticated else UserModel.objects.get(username=data.get('username'))
        user.set_password(request.session.pop('password', None))
        return JsonResponse({'ok': True})
