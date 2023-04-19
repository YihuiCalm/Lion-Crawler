import requests
import urllib
import os
import time
from bs4 import BeautifulSoup

url='http://livingwithlions.org/mara/browse/all/all/'    #有全部狮子信息的界面
strhtml=requests.get(url)
soup=BeautifulSoup(strhtml.text,'lxml')                  #将网页源代码拷贝下来，实例化

#所需要的姓名性别年龄在相应的狮子主页中html代码对应的代码块位置
address_name='#content > div > h2 > a '                 
address_gender='#content > div > ul > li:nth-child(1)'
address_age='#content > div > ul > li:nth-child(2)'

#根据上面的代码块位置 提取出狮子的相应信息成list
data_name_link = soup.select(address_name)
data_gender = soup.select(address_gender)
data_age = soup.select(address_age)

#构建所需狮子信息的相应list
name=[]
gender=[]
age=[]
link=[]
index=[]

#将未分类的list分类到各自list中
for item in data_name_link:
    name.append(item.get_text())
    link.append(item.get('href'))
for item in data_gender:   
    gender.append(item.get_text().replace('Gender: ',''))
for item in data_age:
    age.append(item.get_text().replace('Age: ',''))

#建立以狮子姓名性别年龄为标题的文件夹
for i in range(0,len(name)):
    index.append(name[i]+';'+gender[i]+';'+age[i])
for item in index:
    os.makedirs('F:\TECH\CODE\python\lion\\'+item)   #根据自己电脑文件路径修改一下

#上述list中link[]为存有各个狮子主页的链接 其中就有鼻子以及胡须图片 依次将图片下载存入相应文件夹
for i in range(0,len(link)):
    url=link[i]
    strhtml=requests.get(url)
    soup=BeautifulSoup(strhtml.text,'lxml')
    data_face=soup.select('#lion_photos > li > a')
    print(name[i]+' ')
    #下载鼻子照片 因为网页源代码元素的命名经过拷贝变得不规律 需要进行相应字符串操作使其规范化
    for item in data_face:
        if item.get_text().find('Nose')!= -1 : 
            print(item.get_text())     
            #根据自己电脑文件路径修改一下下面路径              
            urllib.request.urlretrieve(item.get('href'),'F:\TECH\CODE\python\lion\\'+index[i]+'\\'+item.get_text().replace('\n\n','').replace(' ','').replace('/','-').replace('\\','-')+'.jpeg') 
            time.sleep(1)           #等待1秒钟 以免访问网站过快造成网站防攻击机制响应          
            print(item.get('href'))   

    #下载胡须照片 因为网页源代码元素的命名经过拷贝变得不规律 需要进行相应字符串操作使其规范化
    for item in data_face:
        if item.get_text().find('Whiskers')!= -1 :  
            print(item.get_text())  
            #根据自己电脑文件路径修改一下下面路径                 
            urllib.request.urlretrieve(item.get('href'),'F:\TECH\CODE\python\lion\\'+index[i]+'\\'+item.get_text().replace('\n\n','').replace(' ','').replace('/','-').replace('\\','-')+'.jpeg')        
            time.sleep(1)          #等待1秒钟 以免访问网站过快造成网站防攻击机制响应
            print(item.get('href'))
        
        



