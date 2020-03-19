from django.shortcuts import render
from userApp import models as userModels

# Create your views here.

def test(req):
    user=userModels.UserInfo.objects.get(userAccount='lzx001')
    print(user)
    return render(req,"test.html")