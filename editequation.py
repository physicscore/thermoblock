from os import *
from pickle import *

f = open('equation.pck','w')


class equation:
	def __init__(self,variables): #variables; {'Length','Width','Height'}
	    self.variables = variables
fstr[0][0] = "def "
fstr[0][1] = '입력받은이름'
fstr[0][2] = ":"
fstr[1][0] = "    def __init__(self,"
fstr[1][1] = '입력받은 variables' #일단비워둘것
fstr[1][2] = ",x,y,z):"
fstr[2] = "self.x = x"
fstr[3] = "self.y = y"
fstr[4] = "self.z = z"

for i in range(len(variables)):
     fstr[5].append(str(variables[i]))
fstr[5] #여기에는 입력받은베리어블끼워넣을 예정
        # fstr[5]는 몇개가될지 모르니까어펜드 쓰고
        # 따로따로 한줄한줄띄어서넣어야함.
fstr[6] = "self.equation(self):"
fstr[7] = "    def equation(self):"
fstr[8] eq=#입력받은 방정식을 넣는데 변수들앞에 다 self. 붙여야함
fstr[9] = "return eq"

g = open('equation.pck','w')
fstr.dump(g)
g.close()

#입력 포문
f=open('equation.py','w')
for i in range(len(fstr)):
    for j in range(len(fstr[i])):
       # f 에 넣음
