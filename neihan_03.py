#coding:utf-8
import time
import urllib
import urllib2
import re
import sys
import json

after_time="1512209386"
neihan_list=[]
# print after_time
def main():
	global after_time
	page="/bar/1/?is_json=1&app_name=neihanshequ_web&max_time="
	url="http://neihanshequ.com"+page+after_time
	header={"User-Agent":"Mozilla/5.0dows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"}
	# print url+after_url
	request=urllib2.Request(url,headers=header)
	response=urllib2.urlopen(request)
	html=response.read()
	hjson=json.loads(html)
	# pattern=re.compile('<div\sclass="detail">(.*?)</div>',re.S)
	# pattern=re.compile('<li\sclass="share-wrapper right".*data-text="(.*)"')
	# pattern=re.compile('<p>(.*)</p>')
	# pattern2=re.compile('<a\s+href="(.*)"\s+class="J-next-btn"\s+data-group-id=".*"\s+id="prevGroupLink">上一条</a>')
	pattern=re.compile('<p>(.*?)</p>')
	con=pattern.findall(html)
	# for i in con:
		# print i.decode("utf-8")
	# for i in con:
		# print i.decode("utf-8")
	ttime=str(hjson['data']['max_time'])
	after_time=ttime[:-2]
	print hjson['data']['has_more']
	if str(hjson['data']['has_more'])=="True":
		print hjson['data']['has_more']
		print hjson['data']['max_time']
		for i in range(20):
			print hjson['data']['data'][i]['group']['content']
			if no_same(hjson['data']['data'][i]['group']['content']):
				print hjson['data']['data'][i]['group']['content']
			# with open("a.txt","a+") as f:
			# 	f.write(str(i)+"."+hjson['data']['data'][i]['group']['content'].encode("utf-8"))
		# with open("a.txt","a+") as f:
		# 	f.write("\n\n\n")

		print after_time
	else:
		print "nomore new"
		print after_time
def no_same(str):
	global neihan_list
	for m in neihan_list:
		if m==str:
			return False
		else:
			neihan_list.append(str)
			return True

if __name__ == '__main__':
	main()
	while True:
		a=raw_input("continue:")
		if a!="quit":
			main()
		else:
			break


# print type(con2[0])
# a=con2[0]	#list
# b=a[0]		#tuple
# print con[0]
# print b
# page=b
# dealpage(con)
# def writepage(self,item):
# 	# print item
# 	# print type(item)
# 	with open("a.txt","a+") as f:
# 		f.write(item+"\n")

# def dealpage(self,con):
# 	for i in con:
# 		# i=i.replace("&ldquo;","").replace("&rdquo;","").replace("&nbsp;","").replace("&lsquo","").replace("&rsquo","").replace("&hellip;","")
# 		i=i.decode("utf-8")
# 		# print type(i)
# 		self.writepage(i)
# 		# print i
# 	with open("a.txt","a+") as f:
# 		f.write("\n")
# def startwork(self):
# 	while self.time!=0:
# 		self.time-=1
# 		self.loadpage()
# 		print "deal with "+str(self.time)
	# command=raw_input("press Enter(or input quit)")
	# if command=="quit":
	# 	self.switch=False