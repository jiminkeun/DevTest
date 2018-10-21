import os

## 1번
def myaverage(a,b):
    average = (a+b) / 2
    return average

averg = myaverage(5, 150)
print(averg)

## 2번
def get_max_min(data_list):
    max_val = max(data_list)
    min_val = min(data_list)
    return (max_val, min_val)

param_list = [1,5,44,32,35,77,65,20,2]
(max_v, min_v) = get_max_min(param_list)

print("max = %s\nmin = %s" % (max_v,min_v))

## 3번
def get_txt_list(path):
    file_list = os.listdir(path)
    return file_list

path = "E:/Data/dwHelper"
fList = get_txt_list(path)

for i, fileN in enumerate(sorted(fList)):
    print("%s 번째 파일명 : %s" % (i, fileN))

## 4번
def get_bmi_type(w, h):
    bmi_val = w/(h*h)

    print("BMI 지수 : %s" %bmi_val)
    txt_type = ''
    if bmi_val < 18.5:
        txt_type = "마른 체형"
    elif bmi_val < 25.0:
        txt_type = "표준"
    elif bmi_val < 30.0:
        txt_type = "비만"
    else :
        txt_type = "고도 비만"

    return txt_type

typeT = get_bmi_type(75, 1.8)

print("체형 분류 결과 : %s"%typeT)

## 5번
'''
input_w = int(input("몸무게는?"))
input_h = int(input("키는?"))

inputTypeT = get_bmi_type(input_w, (input_h/100))

print("너의 체형 분류 결과 : %s"%inputTypeT)
'''

## 6번
def get_triangle_area(w, h):
    pass

## 7번
def add_start_to_end(st, ed):
    #print(list(range(st, ed)))
    hap = sum(range(st, ed+1))
    return hap

listHap = add_start_to_end(1, 3)
print(listHap)

## 8번
def get_third_word(list):
    result = []
    for val in list:
        result.append(val[:3])

    return result

listR = get_third_word(['Seoul', 'Daegu', 'Kwangju', 'Jeju'])
print(listR)




## 클래스

class NameCard:
    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print("-------------------")
        print("Name : %s"% self.name)
        print("Email : %s" % self.email)
        print("Addr : %s" % self.addr)
        print("-------------------")


nameCard1 = NameCard("김철수", "chul@daou.com", "서울시 강북구")
nameCard1.print_info()

nameCard2 = NameCard("오민수", "oh@naver.com", "경상남도 진해시")
nameCard2.print_info()