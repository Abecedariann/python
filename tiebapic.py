# -*- coding:utf-8 -*-  
import sys
import re
import urllib
import urllib2
import os
from lxml import etree

reload(sys)  
sys.setdefaultencoding('utf8')
class Spider:
	def __init__(self,a):
		self.switch=True
		self.num=0
		self.key=a
		self.page=1
		self.path=os.getcwd()
	def returnhtml(self,url,header):
		header={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"}
		request=urllib2.Request(url=url,headers=header)
		response=urllib2.urlopen(request)
		html=response.read()
		return html
		# print html
	def firstpage(self,sp):
		url="https://tieba.baidu.com/f?kw="+self.key+"&pn="+sp
		header={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"}
		html=self.returnhtml(url,header)
		# link_list=xml.xpath('//div[@class="t_con cleafix"]/div/div[@class="threadlist_lz clearfix"]/div/a/@href')
		pattern=re.compile('<a href="(.*?)"\s.*class="j_th_tit ">')
		con=pattern.findall(html)	
		xml=etree.HTML(html)	
		link_image=xml.xpath('//img[@class="BDE_Image"]/@src')
		# for link in link_image:
		# 	self.writeimage(link)
		# 	print link
		for i in con:
			self.loadpage(i)
	def loadpage(self,link):
		# url="http://www.neihan8.com"+str(self.page)
		url="https://tieba.baidu.com"+link
		header={"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"}
		xml=etree.HTML(self.returnhtml(url,header))
		link_image=xml.xpath('//img[@class="BDE_Image"]/@src')
		# print "222"
		for link in link_image:
			self.writeimage(link)
	def writeimage(self,link):
		header={
			"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
		}

		request=urllib2.Request(link,headers=header)
		# image2=urllib2.urlopen(request2).read()
		image=urllib2.urlopen(request).read()
		filename=link[-4:]
		with open(self.path+"/"+str(self.page)+"/"+str(self.num)+filename,"wb") as f:
			self.num+=1
			print "saving "+str(self.num)+filename
			f.write(image)
			# print os.getcwd()
	def startwork(self,sp,lp):
		while sp<=lp:
			self.page=sp
			if not os.path.exists(self.path+"/"+str(self.page)+"/"):
				os.mkdir(r"./"+str(self.page))
			print "*****"+"第"+str(sp)+"页"+"*****"
			sp2=(sp-1)*50
			self.firstpage(str(sp2))
			sp+=1
			self.num=0
		# command=raw_input("press Enter(or input quit)")
		# if command=="quit":
		# 	self.switch=False
			

if __name__=="__main__":
	a=raw_input("please input name:")
	sp=int(raw_input("please input startpage:"))
	lp=int(raw_input("please input lastpage:"))
	duanzi=Spider(a)
	duanzi.startwork(sp,lp)
