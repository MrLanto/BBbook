from Bbadmin import DDDDOCR_School_BNU_YMQ
import sys

'''
-------------------------------------------------
1. 建议还是bat文件启动 ，windows自带的任务计划程序执行，建议windows计划任务启动时间设置应比程序启动时间提前5min.
2. 温馨提示：如果直接用IDE执行，请自行把sys.argv[*]替换为你想要的内容，注意除了数组均需加引号。
示例
d = '20646853468'
k = 'wodemima'
p = [1265,64864]
t = '07:30:00'
s = 'server酱的key,自行百度'
3. 下方为命令行启动的python文件 用法(替换引号内容)：
python handle_main.py '学号' '密码' 场地代号 '预约时间' 'server酱的key'
-------------------------------------------------
'''
d = sys.argv[1]
k = sys.argv[2]
p = eval(sys.argv[3])
t = sys.argv[4]
s = sys.argv[5]
print('当前设定申请的时间为：%s'%t)
my_ymq = DDDDOCR_School_BNU_YMQ(d,k,p,t,s)
my_ymq.main_apply_task()





