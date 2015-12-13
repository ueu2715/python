# -*- coding: utf-8 -*-
"""
@author: Akagi201
"""

from splinter.browser import Browser
from time import sleep
import traceback

###容错做的不好，考虑的情况也不够多，大家见谅

# 用户名，密码
username = u"xxxx"
passwd = u"xxxx"
# cookies值得自己去找, 下面两个分别是上海, 营口东
starts = u"%u5317%u4EAC%2CBJP"
ends = u"%u6210%u90FD%2CCDW"
# 时间格式2016-01-31
dtime = u"2016-02-10"
# 车次，选择第几趟，0则从上之下依次点击
order = 0
###乘客名
pa = u"xxxx"

"""网址"""
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
login_url = "https://kyfw.12306.cn/otn/login/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"


def login():
    b.find_by_text(u"登录").click()
    sleep(3)
    b.fill("loginUserDTO.user_name", username)
    sleep(1)
    b.fill("userDTO.password", passwd)
    sleep(1)
    print (u"等待验证码，自行输入...")
    while True:
        if b.url != initmy_url:
            sleep(1)
        else:
            break

def huoche():
    global b
    b = Browser(driver_name="chrome")
    b.visit(ticket_url)

    while b.is_text_present(u"登录"):
        sleep(1)
        login()
        if b.url == initmy_url:
           break

    try:
        print (u"购票页面")
        # 跳回购票页面
        b.visit(ticket_url)

        # 加载查询信息
        b.cookies.add({"_jc_save_fromStation": starts})
        b.cookies.add({"_jc_save_toStation": ends})
        b.cookies.add({"_jc_save_fromDate": dtime})
        b.reload()

        

        b.find_by_text(u"更多选项").click()
        sleep(1)
        b.find_by_id("inp-train").fill("k117")
        b.find_by_id("add-train").click()
        b.find_by_text(u"K-快速").click()
        b.find_by_text(u"请选择")[1].click()
        b.find_by_text(u"硬卧")[1].click()
        b.execute_script("$.closeSelectSeat()")
        sleep(2)

        count = 0
        flag = ""
        # 循环点击预订
        print ("order is %s" % order)
        if order != 0:
            
            while b.url == ticket_url:
                b.find_by_text(u"查询").click()
                count +=1
                print (u"循环点击查询... 第 %s 次" % count)
                sleep(5)
                try:
                    b.find_by_text(u"预订")[order - 1].click()
                except:
                    print (u"还没开始预订")
                    continue
        else:
            while b.url == ticket_url:
                b.find_by_text(u"查询").click()
                count += 1
                flag = b.find_by_id("YW_240000K11711")[0].text
                print (u"循环点击查询... 第 %s 次 tickets count is %s" % (count,flag))
                
                #print ("ticket count is %s" % flag)
                
                try:
                    #for i in b.find_by_text(u"预订"):
                    #    i.click()
                    if flag != "--" and flag != u"无":
                        b.execute_script("$($('#YW_240000K11711').nextAll()[4]).children().click()")
                        break
                except:
                    print (u"还没开始预订")
                    continue
                sleep(5)
        
        while True:
            try:
                b.find_by_text(pa)[1].click()
                break
            except:
                print (u"努力选中陛下的乘客信息中~~~")
            sleep(0.5)
        print ( u"能做的都做了.....不再对浏览器进行任何操作")
    except Exception as e:
        print(traceback.print_exc())

if __name__ == "__main__":
    huoche()