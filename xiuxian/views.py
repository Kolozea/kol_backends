from django.shortcuts import render
from .code import Code
from .models import User
import random
# Create your views here.

def sign_in(request):
    response = {'code':200,'data':None,'error_info':""}
    try:
        uid = request.GET.get("uid")
        if not uid:
            raise Exception("缺少参数uid")
        user = User.objects.all().filter(uid=uid)
        if user:
            user = user[0]
            response.update({'data':{'spiritual_power':random.random()*10000}})
    except Exception as e:
        response.update({'code':Code.common_error,'error_info':str(e)})