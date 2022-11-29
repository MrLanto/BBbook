from Bbadmin import DDDDOCR_School_BNU_YMQ
import sys

d = sys.argv[1]
k = sys.argv[2]
p = eval(sys.argv[3])
t = sys.argv[4]
s = sys.argv[5]
my_ymq = DDDDOCR_School_BNU_YMQ(d,k,p,t,s)
my_ymq.main_apply_task()







