#本程序用于爬取号段信息并构筑主程序源代码
import  requests
import re
url = r'https://www.jihaoba.com/tools/haoduan/'
r = requests.get(url)
citys = re.findall('<a href="/haoduan/([a-z]+)/" target="_blank">',r.text)#获取城市
with open (r'C:\Users\Lwq\Desktop\sor\1.text','w') as f:
    f.write('city = {}\n')
    for i in citys:
        f.write("city['{0}'] = {{}}\n".format(i))
for city in citys:#定位城市
    url0 ='https://www.jihaoba.com/haoduan/{0}/'.format(city)
    r = requests.get(url0)
    tar = re.findall('<a href="/haoduan/(\d{{3}})/{0}.htm"'.format(city),r.text)#获取前三位
    for now in tar:#定位前三位
        url = 'https://www.jihaoba.com/haoduan/{0}/{1}.htm'.format(now,city)
        r = requests.get(url)
        aim = re.findall('<li class="hd-city01"><a href="/haoduan/{0}/(\d{{7}})\.htm'.format(city),r.text)#获取前七位
        if aim != []:#int()空值会报错故加入此判断
            with open (r'C:\Users\Lwq\Desktop\sor\1.text','a') as f:
                f.write("city['{0}']['{1}'] =[".format(city,now))
                for i in aim[:-1]:
                    f.write('{0},'.format(int(i[3:])))
                f.write(str(int(aim[-1][3:])))
                f.write(']\n')
        print(city,':',now,'over')
print('all:over')