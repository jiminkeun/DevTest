import os
##### 파일 읽기 #####
# rt => r:읽기전용, t:텍스트파일
f = open('E:/Dev/PYTHON_WORKSTATION/pythonTest/buy_list.txt', 'rt')
lines = f.readlines()

for item in lines:
    print(item, end='')

##### 파일 쓰기 #####
# wt => w:쓰기전용, t:텍스트파일
fw = open('E:/Dev/PYTHON_WORKSTATION/pythonTest/sel_list.txt', 'wt')
fw.write('삼성전자\n')
fw.write('SK하이직스\n')
fw.close()

### 연습문제

# 7-1
f1 = open('E:/Dev/PYTHON_WORKSTATION/pythonTest/numbers.txt', 'wt')
for i in range(1,11):
    f1.write('%s\n'%i)
f1.close()

# 7-2
file_path = input('경로입력?')
f2 = open('E:/Dev/PYTHON_WORKSTATION/pythonTest/files.txt','wt')
flist = os.listdir(file_path)
for x in flist:
    f2.write('%s\n'%x)
f2.close()

