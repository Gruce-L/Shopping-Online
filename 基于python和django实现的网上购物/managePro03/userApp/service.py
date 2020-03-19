from userApp.models import UserInfo,OrderInfo,Product
from django.db import models

#定义函数判断用户账号是否存在
def accOunIsNotExit(userAccount):
    #根据用户账号搜索是否有用户数据
    userList=UserInfo.objects.filter(userAccount=userAccount)
    if userList != None and len(userList)>0 :
        return False     #账号存在
    else:
        return True

#生成用户编号
def createUserId():
    resu=UserInfo.objects.aggregate(models.Max("userID"))#获得用户编号最大值
    #print('-------------'+str(resu))
    userId=resu["userID__max"]+1
    return userId

#返回当前登录的用户对象
def loginUser(userAcc,userPass):
    try:#对象存在返回对象，对象不存在抛出异常
        #登录用户对象
        loginuser = UserInfo.objects.get(userAccount=userAcc,userPass=userPass)
        return loginuser
    except Exception:
        return None