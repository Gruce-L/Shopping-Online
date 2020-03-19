from django.db import models
from userApp import models as userModels        #引入其他应用中的模块

# Create your models here.

class AddressInfo(models.Model):
    address=models.CharField(max_length=200)
    userInfo=models.ForeignKey(to=userModels.UserInfo,on_delete=models.DO_NOTHING)    #关联

    class Mate:
        db_table = 'addressTable'
    pass
