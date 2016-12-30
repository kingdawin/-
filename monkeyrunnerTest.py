# -*- coding: utf-8 -*-

# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi

# Connects to the current device, returning a MonkeyDevice object
#这是一个阻塞方法，设置超时时间10s
device = mr.waitForConnection(10)
#device = mr.waitForConnection(30,'123123135002735')

# press menu
#device.press('KEYCODE_MENU', md.DOWN_AND_UP)


#安装apk包
#预置资源时，批量安装
def installAPK(apkName):
	#device.installPackage('D:/Yahoo Mail.apk'.decode('utf-8'))
	device.installPackage('D:/SubwaySurf.apk'.decode('utf-8'))
	device.installPackage('D:/psiphon3.apk'.decode('utf-8'))
	print 'finish install'

'''
批量卸载apk，要知道apk包名
com.psiphon3
'''
def removeAPK(packageName):
	device.removePackage('com.psiphon3')
	device.removePackage('com.kiloo.subwaysurf')	
	print 'finish uninstall'
	
#拖动操作，四个参数，前两个是初始点、结束点坐标，0.5是持续时间，1是步数
def drag(start,end,duration,step):
	device.drag((100,500),(550,500), 0.0, 1)

#将日志输出到外部文件,在python中使用中文，需要在文件开头将编码设置为utf-8,否则乱码
log = open('d:/monkenyLog.txt', 'w')
log.write('等待手机')
log.close()

installAPK('')
#removeAPK('')

