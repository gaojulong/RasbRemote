#coding:utf-8
import os
import Systemfun.util as sysutil 
import GPIO.control as gpioset

from flask import Flask,render_template
app = Flask(__name__)

@app.route('/led/<flag>')
def led(flag):
    print(flag);
    if flag=='on':
        print("%s",flag);
        gpioset.on_led()
        return "LED已打开"
    else:
        gpioset.off_led()
        return "LED已关闭"

@app.route('/temp')
def temp():
    temp=sysutil.getCPUTemp()
    return "CPU温度:"+str(temp)+"℃"

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(
    port=80
    )
