from django.shortcuts import render,redirect
from userApp.models import UserInfo,OrderInfo,Product
from userApp import util
from userApp import service     #定义业务模块
import time
import datetime

# Create your views here.

def toIndex(req):
    return render(req,"index.html")

#html页面访问
def topage(req,pageName):
    
    return render(req,pageName)

#用户注册
#测试数据添加
def userReg(req):
    #获得用户的注册信息
    userAcc=req.POST.get("userAcc")
    service.createUserId()
    #判断用户账号是否存在
    if service.accOunIsNotExit(userAcc):
        userPass=req.POST.get("userPass")
        userSex=req.POST.get("userSex")
        userObj=UserInfo()      #创建userInfo对象
        userObj.userID=service.createUserId()
        userObj.userAccount=userAcc
        userObj.userPass=userPass
        userObj.userSex=userSex
        userObj.userBirth=datetime.date(1998,8,16)
        userObj.save()      #添加用户对象
        return render(req,"test.html")
    #return render(req,'register.html')
    return redirect("/page/register.html")

#登录操作
def userLogin(req):
    userAcc=req.POST.get("userAcc")
    userPass=req.POST.get("userPass")
    logUser=service.loginUser(userAcc,userPass)     #用户登录，账号密码正确，返回对象，否则返回空
    if logUser != None :
        req.session['info']={'name':'李志兴','userSex':'男'}
        req.session['logUser']=logUser.userAccount
        #查询商品名称中带鞋的所有商品
        pros = Product.objects.filter(proName__contains='鞋')
        cont=dict()
        cont['pros']=pros


    else:
        return render(req,'login.html',context={"error":"账号或密码错误"})

    return render(req,'main.html',context=cont)

#返回订单编号的时间信息
#def idInfo():
    #格式化时间
 #   idInfo = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))     #获得当前系统时间
 #   return idInfo
#idInfo()

#显示登录者的购物车
def showUserGoods(req):
    #查找登录的用户对象
    user=UserInfo.objects.get(userAccount=req.session.get('logUser'))
    products=user.pros.all()      #获得当前用户的购物车商品
    cont={'pros':products}
    return render(req,'goodsPage.html',context=cont)


def orderAdd(req):
    #查询这个账号密码的用户
    user = UserInfo.objects.filter(userAccount='lzx1001',userPass='123456')[0]   #过滤条件查询
    #添加订单
    OrderInfo.objects.create(orderId=(str(user.userID)+util.idInfo()),orderMon=123.5,userInfo=user)
    return None

#用户商品添加
def userAddGoods(req):
    #只有一个商品添加时的方法
    #proIdInfo=req.GET.get("proId")                              #字符串类型
    #print(proIdInfo)
    #pro = Product.objects.get(proId=int(proIdInfo));            #获得一个商品对象
    #user=UserInfo.objects.get(userAccount=req.session.get('logUser'))  #查找登录的用户对象
    #user.pros.add(pro)      #用户添加一个商品
    #查询商品名称中带鞋的所有商品
    #pros = Product.objects.filter(proName__contains='鞋')
    #cont=dict()
    #cont['pros']=pros

    proIdInfos=req.GET.getlist("proId")                              #字符串类型
    #print(proIdInfo)
    user=UserInfo.objects.get(userAccount=req.session.get('logUser'))  #查找登录的用户对象

    for proIdInfo in proIdInfos:
        pro = Product.objects.get(proId=int(proIdInfo))            #获得一个商品对象
        user.pros.add(pro)      #用户添加一个商品
    #查询商品名称中带鞋的所有商品
    pros = Product.objects.filter(proName__contains='鞋')
    cont=dict()
    cont['pros']=pros

    return render(req,"main.html",cont)

#删除用户的商品
def userdeleGoods(req):
    proIdInfo=req.GET.get("proId")                              #字符串类型
    pro = Product.objects.get(proId=int(proIdInfo))            #获得一个商品对象
    #pro.delete()    #对象删除
    user=UserInfo.objects.get(userAccount=req.session.get('logUser'))  #查找登录的用户对象
    user.pros.remove(pro)      #用户删除一个商品
    return redirect("../../goods/addGoods")