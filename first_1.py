str1 = 'MNAPERQPQPDGGDAPGHEPGGSPQDELDFSILFDYEYLNPNEE\
EPNAHKVASPPSGPAYPDDVLDYGLKPYSPLASLSGEPPGRFGEPDRVGPQ\
KFLSAAKPAGASGLSPRIEITPSHELIQAVGPLRMRDAGLLVEQPPLAGVA\
ASPRFTLPVPGFEGYREPLCLSPASSGSSASFISDTFSPYTSPCVSPNNGG\
PDDLCPQFQNIPAHYSPRTSPIMSPRTSLAEDSCLGRHSPVPRPASRSSSP\
GAKRRHSCAEALVALPPGASPQRSRSPSPQPSSHVAPQDHGSPAGYPPVAG\
SAVIMDALNSLATDSPCGIPPKMWKTSP'

acid = 'ACDEFGHIKLMNPQRSTVWY'
freq = {}# 定义一个空字典
for i in range(len(acid)):
    freq[acid[i]] = round(str1.count(acid[i]) / len(str1),3)# 统计频率


resoult = {}  # 定义一个空字典
for i in str1:  # 遍历输入的字符串，以键值对的方式存储在字典中
    resoult[i] = str1.count(i)  
for key in resoult:  # 遍历字典，格式化输出结果
    print(f'{key}  {resoult[key]}')

file = open('D:/test/frq.txt', 'w')
for k in freq.keys():
    file.write(str(k) + '\t')
file.write('\n')
for v in freq.values():
    file.write(str(v) + '\t')
    
    
file.close()  # 关闭文件
