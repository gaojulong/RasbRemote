#coding:utf-8
import os
def getCPUTemp():
    file = open("/sys/class/thermal/thermal_zone0/temp")
    temp = float(file.read()) / 1000
    file.close()
    print ("Temp: %.1f ℃" %temp)
    return temp

def getDisk():  
    #get Disk information,DISK[8],[9],[10],[11]:Size, Used. free, Used %  
    DISK = os.popen('df -h /').read().split()[8:12]  
    Disktotal = 'Disk total space is %s ' %DISK[0]
    DiskUsed = 'Disk Used  space is %s ' %DISK[1] +'and is %s' %DISK[3]
    DiskFree = 'Disk Free  space is %s ' %DISK[2]
    DiskDict={
            'total':'Disk total  space is %s ' %DISK[0],
            'used':'Disk Used  space is %s ' %DISK[1]+'and is %s' %DISK[3] ,
            'free':'Disk Free  space is %s ' %DISK[2]
            }
    return DiskDict

def getRAM():  
    #get RAM as list,list[7],[8],[9]:total,used,free  
    RAM = os.popen('free').read().split()[7:10]  
    #convert kb in Mb for readablility  
    RAM0 = float(RAM[0])/1024  
    print ('RAM Total is %.1f MB' %RAM0)  
    RAM1 = float(RAM[1])/1024  
    percent = RAM1/RAM0*100  
    print ('RAM Used  is %.1f MB, %.2f' %(RAM1,percent) +'%')  
    RAM2 = float(RAM[2])/1024  
    print ('RAM Free  is %.1f MB' %RAM2)  

getCPUTemp()
dict=getDisk()
print(dict['total'])
print(dict['used'])
print(dict['free'])
getRAM()
