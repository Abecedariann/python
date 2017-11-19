#-*- coding: utf-8 -*-
import urllib
import urllib2
from tkinter import *
import tkinter.messagebox
import os

def log():
	try:
		
		id=t1.get()
		password=t2.get()
		if id=='' or password=='':
			tkinter.messagebox.showinfo(title="message",message="asdf")
			return
		url = 'http://1.1.1.2/ac_portal/login.php'  
		data = {  
				'userName': id,  
				'pwd': password,  
				'opr':"pwdLogin",
				'rememberPwd':"0"
		}  
		header={
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
				} 
		full_data=urllib.urlencode(data)
		request=urllib2.Request(url,data=full_data,headers=header)
		response=urllib2.urlopen(request,timeout=1)
		html=response.read()
		msg=str(html)
		b=msg.split(',',6)
		c=b[0].split(':',2)
		m=b[1].split(':',2)
		d=c[1]
		f=d[1:-1]
		tip=m[1]
		top=tip[1:-1]
		global root
		if c[1]=="true":
			tkinter.messagebox.showinfo(title="message",message="登陆成功,程序即将退出")
			root.destroy()
		elif c[1]=="false":
			if top=="用户已在线，不需要再次认证":
				tkinter.messagebox.showinfo(title="message",message=top)
			elif top=="用户名或密码错误":
				tkinter.messagebox.showinfo(title="message",message=top)
		
		ff=open(r"D:\login\info.txt","w")				
		ff.writelines(id+"\n")
		ff.writelines(password)
		ff.close()	
	except Exception,e:
	 	# tkinter.messagebox.showinfo(title="Error",message="Error")
		tkinter.messagebox.showinfo(title="message",message=str(e))
if __name__ == '__main__':
	root=Tk()
	root.title('login v1.0')
	# root.geometry('250x150')
	id=""
	password=""
	t1=StringVar()
	t2=StringVar()
	if(os.path.exists(r"D:\login\info.txt")):
		ff=open(r"D:\login\info.txt")
		id=ff.readline()
		password=ff.readline()
		ff.close()
	else:
		try:
			if os.path.exists(r"D:\login"):
				ff=open("D:\login\info.txt","w")
				ff.close()
			else:
				os.mkdir("D:\login")
				ff=open("D:\login\info.txt","w")
				ff.close()
		except Exception,e:
			tkinter.messagebox.showinfo(title="message",message=str(e))
	if(os.path.exists(r"D:\login\info.txt")):
		t1.set(id.strip())
		t2.set(password.strip())
	entry1=Entry(root,textvariable=t1,width=30).pack()
	entry2=Entry(root,textvariable=t2,width=30).pack()
	btn=Button(root,text='sign in',command=log,width=30)
	btn.pack()
	root.mainloop()
	
