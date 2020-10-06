# -*- coding: utf-8 -*-
import unittest
from f4 import *
import random


def create_equation():  # 随机生成算式
    eq = []
    operator = ["+", "-", "*", "/"]
    for i in range(3):
        eq.append(random.randint(0, 10))
        eq.append(operator[random.randint(0, 3)])
    eq.append(random.randint(0, 10))
    p = random.randint(1, 5)
    if p is 1:
        eq.insert(0, "(")
        eq.insert(4, ")")
    elif p is 2:
        eq.insert(0, "(")
        eq.insert(6, ")")
    elif p is 3:
        eq.insert(2, "(")
        eq.insert(6, ")")
    elif p is 4:
        eq.insert(2, "(")
        eq.append(")")
    elif p is 5:
        eq.insert(4, "(")
        eq.append(")")
    return eq


def reverse_polish(equation):  # 将算式转换为逆波兰表达式
    result = []
    c = []
    slist = [i for i in equation]
    cal = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }
    cal1 = {
        '(': 0,
        ')': 0
    }
    for item in slist:
        if item in range(0, 100):
            result.append(item)
        elif not c and item in cal.keys():
            c.append(item)
            continue
        elif c and item in cal.keys():
            for x in range(c.__len__()):
                z = c[-1]
                temp = cal[z] if z in cal else cal1[z]
                if temp >= cal[item]:
                    result.append(c.pop())
                else:
                    c.append(item)
                    break
            if not c:
                c.append(item)
        elif item is ")":
            for x in range(c.__len__()):
                if c[-1] == "(":
                    c.pop()
                    break
                else:
                    result.append(c.pop())
        elif item is "(":
            c.append(item)
            # print(result,c)
    for x in range(c.__len__()):
        result.append(c.pop())
    return result


class PyStack(object):  # 自定义栈

    def __init__(self, initSize=20, incSize=10):
        self.initSize = incSize
        self.incSize = incSize
        self.stackList = []
        self.top = self.bottom = 0

    def push(self, ele):
        if self.top - self.bottom >= self.initSize:
            self.incSize += self.initSize
        self.stackList.append(ele)
        self.top += 1

    def pop(self):
        if self.top - self.bottom > 0:
            self.top -= 1
            ret = self.stackList.pop()
            return ret
        else:
            return None

    def len(self):
        return self.top - self.bottom


def calculate(re_equation):  # 计算逆波兰表达式
    stack = PyStack()
    sumEnd = 0

    if len(re_equation) is 0:
        return sumEnd
    for i in re_equation:
        if i in range(0, 100):
            stack.push(float(i))
        elif '+' is i:
            a = stack.pop()
            b = stack.pop()
            stack.push(b + a)
        elif '-' is i:
            a = stack.pop()
            b = stack.pop()
            stack.push(b - a)
        elif '*' is i:
            a = stack.pop()
            b = stack.pop()
            stack.push(b * a)
        elif '/' is i:
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                return False  # print('%d/%d分子不能为0' % (b, a))
            else:
                stack.push(b / a)
    return stack.pop()


class F4Test(unittest.TestCase):
    def test_f4(self):
        pass

    def test01_create_equation(self):  # 测试顺序按函数名字字典顺序进行
        print("create_equation函数单元测试开始：")
        self.assertIsNotNone(create_equation())
        print("OK")
        print("create_equation函数单元测试结束。\n")

    def test02_reverse_polish(self):
        eq = []
        print("reverse_polish函数单元测试开始：")
        equation = input("输入一个四则运算（括号请使用英文版的括号）：")
        _eq_ans = input("输入正确的逆波兰表达式：")
        list(equation)  # 输入的表达式是str类型，该函数处理的是含有整型和字符型的list类型
        for temp in equation:
            if '0' <= temp <= '9':
                eq.append(int(temp))
            else:
                eq.append(temp)
        re_equation = reverse_polish(eq)
        str_equation = "".join('%s' % id for id in re_equation)
        self.assertEqual(_eq_ans, str_equation)
        print("OK")
        print("reverse_polish函数单元测试结束。\n")



    def test03_calculate(self):
        eq = []
        print("calculate函数单元测试开始：")
        equation = input("输入一个可计算的逆波兰表达式：")
        _eq_ans = input("输入该表达式的正确结果：")
        list(equation)  # 输入的表达式是str类型，该函数处理的是含有整型和字符型的list类型
        for temp in equation:
            if '0' <= temp <= '9':
                eq.append(int(temp))
            else:
                eq.append(temp)
        result = calculate(eq)
        self.assertEqual(float(_eq_ans), result)
        print("OK")
        print("calculate函数单元测试结束。\n")


if __name__ == "__main__":
    unittest.main()
