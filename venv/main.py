city = {}
city['js'] ={}
city['js']['133'] = [528,529,610,2774,2775,2776,2777,3774,3775,3776,3777,3881,4774,4775,4776,4777,5774,5775,5776,5777,7604,7614,7615,7616,7617,7618,7619,8249,8279,8298,8299]

for i in city['js']['133']:
    with open(r'C:\Users\Lwq\Desktop\TN\{0}.vcf'.format(str(i)),'w') as f:
        for j in range(10000):
            num = 133 * 100000000 + i * 10000 + j
            f.write('BEGIN:VCARD\nVERSION:2.1\nN:;{0};;;\nFN:{0}\nTEL;CELL:{1}\nEND:VCARD\n'.format(j,num))
