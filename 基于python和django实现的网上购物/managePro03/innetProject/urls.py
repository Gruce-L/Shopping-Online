"""innetProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from userApp import views as userViews
from orderApp import views as orderViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userViews.toIndex),
    path('page/<str:pageName>', userViews.topage),
    path("user/add/",userViews.userReg),
    path("user/log/",userViews.userLogin),
    path("test/orderadd/",userViews.orderAdd),
    path("test/adduserGods/",userViews.userAddGoods),
    path("goods/addGoods/",userViews.showUserGoods),
    path("goods/deleGoods/",userViews.userdeleGoods),
    path("test/",orderViews.test)
]
