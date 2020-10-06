from random import randint
from random import choice
import os 
ops = ['+','-','*','/']
bra = ['(', '', ')']
com = input('>') #用户输入
com_list = eval(com)
'''
while com_list[2].isdigit() == False:
    print('题目数量必须是正整数')
    com = input('>') #用户输入
    com_list = com.split()
    '''

def xx():
    s1 = randint(1,10)
    s2 = randint(1,10)
    s3 = randint(1,10)
    s4 = randint(1,10)
    op1 = choice(ops) #随机运算符
    op2 = choice(ops)
    op3 = choice(ops)
    """括号"""
    bra_1 = ['' , '' ,'']
    bra_2 = ['' , '' , '']
    i = ii =0
    while (i ==0 and ii ==2) or abs(i-ii)==1 \
        or ii < i  :
        i = randint(0,2)
        ii = randint(0,2)

    bra_1[i] = '(';   bra_2[ii]=')'

    while op1 == op2 == op3 :
        op1 = choice(ops) #随机运算符
        op2 = choice(ops)
        op3 = choice(ops)

    eq = bra_1[0] + str(s1) + op1 + bra_1[1] + str(s2) + \
    bra_2[0] + op2 + bra_1[2] + str(s3) + bra_2[1] + op3 \
    + str(s4) + bra_2[2]
    res = eval(eq) 
    return [eq,res]



eq = [];  res = []
while len(res) < com_list:
    a = xx()
    if a[1] in res or len((str(a[1])) ) >6: #结果一样的直接就不要
        continue
    eq.append(a[0])
    res.append(a[1])

f= open('题目.txt','w')
for i in range(len(eq)):
    print('{0:15}'.format(eq[i]),end = '')
    print(res[i])
    xxx = 17 - len(eq[i])
    f.write(str(eq[i]+' '*xxx))
    f.write(str(res[i])+'\n')
f.close()
os.system('题目.txt')  #决定是否打开txt