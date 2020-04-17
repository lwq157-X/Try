import  re
import  requests
url = r'https://www.jihaoba.com/tools/haoduan/'
r = requests.get(url)
citys = re.findall('<a href="/haoduan/([a-z]+)/" target="_blank">',r.text)
with open (r'C:\Users\Lwq\Desktop\sor\2.text','w') as f:
    f.write('city = {}\n')
    for i in citys:
        f.write("city['{0}'] = {{}}\n".format(i))
city = 'zhenjiang'
url0 = 'https://www.jihaoba.com/haoduan/{0}/'.format(city)
r = requests.get(url0)
tar = re.findall('<a href="/haoduan/(\d{{3}})/{0}.htm"'.format(city), r.text)
for now in tar:
    url = 'https://www.jihaoba.com/haoduan/{0}/{1}.htm'.format(now,city)
    r = requests.get(url)
    aim = re.findall('<li class="hd-city01"><a href="/haoduan/{0}/(\d{{7}})\.htm'.format(city), r.text)
    if aim !=[]:
        with open(r'C:\Users\Lwq\Desktop\sor\2.text', 'a') as f:
            f.write("city['{0}']['{1}'] =[".format(city,now))
            for i in aim[:-1]:
                f.write('{0},'.format(int(i[3:])))
                print(i[3:])
            print(int(aim[-1][3:]),'end')
            f.write(str(int(aim[-1][3:])))
            f.write(']\n')