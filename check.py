#!/user/bin/env python
# -*- coding: utf-8 -*-

import os
import datetime

#本地录音备份存放目录
localdir=u'F:\\Python\\test'
#远程生产录音存放目录
remotedir=u'\\\\192.168.30.217\\fileserver\\1\\0'

#转换为整形函数
def int_change(d):
	try:
		d=int(d)
	except:
		d=0
	finally:
		return d

#录音日期目录列表，并转换为整形
locallist=map(int_change, [d for d in os.listdir(localdir)])
remotelist=map(int_change, [d for d in os.listdir(remotedir)])
#获得list中最大的元素
local_maxdate=max(locallist)
remote_maxdate=str(max(remotelist))
date_str=remote_maxdate[:4]+'-'+remote_maxdate[4:6]+'-'+remote_maxdate[6:8]
date_time=datetime.datetime.strptime(date_str, '%Y-%m-%d') + datetime.timedelta(days=-1)
remote_maxdate=int_change(date_time.strftime('%Y%m%d'))




import send_email

if not local_maxdate == remote_maxdate:
	send_email.server.set_debuglevel(1)
	send_email.server.login(send_email.from_addr, send_email.password)
	send_email.server.sendmail(send_email.from_addr, send_email.to_addr, send_email.msg.as_string())
	send_email.server.quit()
else:
	print ('Sync Success')
