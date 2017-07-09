import logging
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import JsonResponse
logger = logging.getLogger(__name__)


def login_user(request):
    if request.method == 'POST':
        if request.POST['action'] != 'login_user':
            data = {
                'user_signed_in': False,
                'error': 'Don`t play with js ;)'
            }
            return JsonResponse(data)
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=request.POST['username'])
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(email=request.POST['username'])
            except UserModel.DoesNotExist:
                data = {
                    'user_signed_in': False,
                    'error': 'There is no user with that username or email'
                }
                return JsonResponse(data)
        user = authenticate(username=user.username, password=request.POST['password'])
        if user is None:
            data = {
                'user_signed_in': False,
                'error': 'Password is incorrect'
            }
            return JsonResponse(data)
        else:
            login(request=request, user=user)
            data = {
                'user_signed_in': True
            }
            return JsonResponse(data)
