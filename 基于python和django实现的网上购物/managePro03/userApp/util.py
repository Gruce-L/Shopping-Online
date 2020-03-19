import time

#返回订单编号的时间信息
def idInfo():
    #格式化时间
    idInfo = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))     #获得当前系统时间
    return idInfo

print(idInfo())