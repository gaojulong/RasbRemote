#coding:utf-8
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print ("GPIO引入失败")

#设置模式
GPIO.setmode(GPIO.BOARD)
#将引脚设置为输出模式
GPIO.setup(7, GPIO.OUT)

def on_led():
    #给引脚输出高电平
    GPIO.output(7,GPIO.HIGH)
def off_led():
    #给引脚输出低电平
    GPIO.output(7,GPIO.LOW)
