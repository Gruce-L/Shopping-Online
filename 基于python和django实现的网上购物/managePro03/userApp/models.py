from django.db import models

# Create your models here.

#定义模型对象
class UserInfo(models.Model):
    #'''
    #    列           类型          要求
    #  用户编号        int           pk
    #  用户账号      varchar       unique
    #  用户密码      varchar
    #  生日           date
    #  性别          varchar
    #'''
    #定义属性       表中列的定义
    userID = models.BigIntegerField(primary_key=True)   #编号设置为主键
    userAccount = models.CharField(max_length=50, unique=True)
    userPass = models.CharField(max_length=30)
    userBirth = models.DateField(null=True)
    userSex = models.CharField(max_length=6,default="男")
    pros = models.ManyToManyField("Product")          #用户和商品多对多关系

    pass

class OrderInfo(models.Model):
    '''
    订单
        列           类型          要求
     订单编号       varchar         pk
     下单日期       datatime        
     订单金额       float
     用户编号                       fk
    '''
    orderId = models.CharField(primary_key=True,max_length=100)
    orderData = models.DateTimeField(auto_now=True)     #添加数据是默认系统当前时间
    orderMon = models.FloatField()
    userInfo = models.ForeignKey(UserInfo,on_delete=models.CASCADE)     #设置外键关联
    
    class Meta:
        db_table='order_table'      #自定义表名

#商品模型表
class Product(models.Model):
    proId = models.BigAutoField(primary_key=True)                 #商品编号自增长
    proName = models.CharField(max_length=200)                    #商品名称
    proPrice = models.FloatField(default=0.0)                     #商品单价
    proImg = models.CharField(max_length=200);                   #商品图片


