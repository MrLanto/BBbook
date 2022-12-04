from Bbadmin import DDDDOCR_School_BNU_YMQ
import sys
import datetime

d = sys.argv[1]
k = sys.argv[2]
p = eval(sys.argv[3])
t = sys.argv[4]
s = sys.argv[5]
print(datetime.datetime.now())
print('当前设定申请的格林尼治时间为：%s'%t)
print(f"设定的北京时间为：{datetime.datetime.strftime(datetime.datetime.strptime(t,'%H:%M:%S')+datetime.timedelta(hours=8),'%H:%M:%S')}\n\n-----START----\n\n")
# my_ymq = DDDDOCR_School_BNU_YMQ(d,k,p,t,s)
# my_ymq.main_apply_task()







