from urllib.request import urlopen
from urllib.parse import urlencode
from time import sleep

#读取ProSeq.fa文件
md = open('E:/zhuomian/222/py2/ProSeq.fa','rt')
md1 = md.readlines()
md.close()

#生成名为seqs的字典，蛋白质id作为key，蛋白质序列作为value
seqs = {}
for line in md1:
    if line[0] == '>':
        name = line[1:].strip()
        seqs[name] = ''
    else:
        seqs[name] += line.strip()

#将字典的value转化为名为value的list
value = list(seqs.values())

#访问web网页
url="http://ibi.hzau.edu.cn/FDserver/cido.php"

#初始化,并且将value的蛋白质序列输入web查询，每次查询都有sleep间隔
result = []
for ch in range(len(value)):
    inputs = {'textarea': value[ch], 'radiobutton': 'Two',
    'ButtonRatePred': 'Predict Folding Rate'}
    params = bytes(urlencode(inputs), encoding= 'utf-8')
    f = urlopen(url, params)
    result.append(str(f.read()))
    f.close()
    sleep(1)    

#将result转换为名为FoldingRate的list，并对list的每个元素截取折叠速率结果,转入key2中
key2 = []
FoldingRate = list(result)
for x in result:
    key2.append(x[-16:-6])

#将得到信息按照要求输出到ProFoldingRate.txt文件中
mdname = 'E:/zhuomian/222/py2/ProFoldingRate.txt'
key1 = list(seqs.keys())
md2 = open(mdname, 'wt')
md2.write('ProID'+'\t\t\t')
md2.write('FoldingRate'+'\n')
for ch in range(len(key1)):
    md2.write(key1[ch] +'\t\t')
    md2.write(key2[ch]+'\n')
    md2.write('……………………………………………………………………………'+'\n')
md2.close()
