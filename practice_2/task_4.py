# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9

"""
abcd = int(input())
a = abcd//1000
b = abcd%1000//100
c = abcd%100//10
d = abcd%10

print(a+b+c+d)