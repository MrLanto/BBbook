# 北师大羽毛球馆预约程序

## Introduction
使用python语言编写，Cython编译，so 文件是在linux上执行的类文件（类似于windows上的dll文件）。 经过测试可用。
本程序仅可在LINUX上可用，自己没有云服务器的话，建议还是用github自带的ACTION WORKFLOW(见方法二)。

## 使用说明
## 入口函数handle_main.py使用说明
```
# 通过LINUX命令行调用python

d = sys.argv[1] # d是学号
k = sys.argv[2] # 密码
p = eval(sys.argv[3]) # 场地代号，这里填入两个数字的数组 如  [5988,5977]
t = sys.argv[4] # 预约时间，格林尼治时间。比如学校7:30:00开始预约，那我们这里需要填为23:30:00
s = sys.argv[5] # server酱的key,请自行百度，为了提醒是否预约成功或失败，推送至你的微信。
my_ymq = DDDDOCR_School_BNU_YMQ(d,k,p,t,s)
my_ymq.main_apply_task()
```

### 方法一：
直接下载本仓库文件至本地的linux系统，安装requestments依赖后，执行handle_main.py文件即可。 
note: python须小于等于3.10
1. 首先，cd到文件夹下，然后输入进行测试 （可以删除py文件的时间提醒，那玩意是为workflow准备的）
```
python handle_main.py 学号 密码 场地代号 预约时间 server酱的key
```
2. 建立cron调度命令，cron cd 你的地址;python handle_main.py 学号 密码 场地代号 预约时间 server酱的key >> BBbadmin.log 2>&1

(__温馨提示：设定的最好在目标时间前1-2分钟执行__)

### 方法二：
使用github上自带的github action workflow
1. 点击右上角Fork到自己的仓库
2. Settings==> Security(左下角)==> Secrets ==> Actions ==> 创建自己的Secrets (自己的环境变量，别人看不到的) ==> 
```
建议把变量group设置为 obj_infor,否则还得改yml文件；
设置下面的变量：
YOUR_SECRET_K            （密码）
YOUR_SECRET_NAME         
YOUR_SECRET_PLACE
YOUR_SECRET_SERVERJ
YOUR_SECRET_TIME         （格林尼治时间，写成23:30:00,注意是英文符号）
```
3. 建立触发器（github action自己的定时触发器非常难用，所以自己创建触发器即可）
3.1 以免费的华为云函数为例 不详细讲了 我看百度上很容易搜到 先自学 https://blog.csdn.net/qq_28778001/article/details/124891438
3.2 创建python 3.10 ,其他的默认就行啦
3.3 粘贴触发代码 记得输入你的token(token怎么搞后面说)
```
# -*- coding:utf-8 -*-
import requests
import json

def run():
    payload = json.dumps({"ref": "main"})
    header = {'Authorization': 'Bearer 你的token',
              "Accept": "application/vnd.github+json"}
    url = 'https://api.github.com/repos/baelow/BBbook/actions/workflows/41743763/dispatches'
    r = requests.post(url = url, headers = header,data=payload)
    print(r)
    print(r.text)

# 云函数入口
def handler(event, context):
    return run()
```
3.4 设置触发器 Timer 设置好时间 不会的自行百度 Cron 任务完成
4. Token获取
https://docs.github.com/en/rest/reference/actions#create-a-workflow-dispatch-event
也可参考： https://blog.csdn.net/l1937gzjlzy/article/details/117753465

### 测试
1. 输入各种环境变量后，测试github上的工作流是否正常。
* 点击Action 
* 右边有个run workflow 等待看结果
2. 测试华为云函数
部署测试完 是否有报错，更改时间，测试是否运作,—__设定Cron时间应比目标预约时间提前5-10min(github服务器容易拥堵)__

## 场地ID
| 时间          | 3号场地 | place 4 | place 5 | 小馆2号  | 小馆3号  | 允许预约时间   |
|-------------|------|---------|---------|-------|-------|----------|
| 8:00-9:00   | 5997 | 6047    | 35426   | 50469 | 50519 | Mon-Fri  |
| 9:00-10:00  | 5995 | 6045    | 35424   | 50467 | 50517 | Mon-Fri  |
| 10:00-11:00 | 5993 | 6043    | 35422   | 50465 | 50515 | Mon-Fri  |
| 11:00-12:00 | 5991 | 6041    | 35420   | 50463 | 50513 | Mon-Fri  |
| 12:00-13:00 | 5989 | 6039    | 35418   | 50461 | 50511 | Mon-Fri  |
| 13:00-14:00 | 5987 | 6037    | 35416   | 50459 | 50509 | Mon-Fri  |
| 14:00-15:00 | 5985 | 6035    | 35414   | 50457 | 50507 | Mon-Fri  |
| 15:00-16:00 | 5983 | 6033    | 35412   | 50455 | 50505 | Mon-Fri  |
| 16:00-17:00 | 5981 | 6031    | 35410   | 50453 | 50503 | Mon-Fri  |
