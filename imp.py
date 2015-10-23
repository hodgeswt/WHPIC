'''
	
	Code by Will Hodges on 10/23/15
	
'''

from calc import *
import json

parser = calcParser()

print "\n\n     Will Hodges Python Interpreter Calculator 10/23/15"

print "\n\nWelcome to the WHPIC! Enter an expression (or series of expressions) below.\n\nSeperate each by a semicolon and nothing more!\n"

user_input = raw_input("Equation: ")

ast = parser.parse(user_input, rule_name='start')

def eval(expr):
	operator = expr[1][0]
	op1arr = expr[0][0]
	op1str = ''
	for num in op1arr:
		op1str = op1str + num
	op1 = int(op1str)
	
	op2arr = expr[2][0]
	op2str = ''
	for num in op2arr:
		op2str = op2str + num
	op2 = int(op2str)
	
	if operator == '+':
		print "\n" + str(op1) + " + " + str(op2) + " = " + str((op1 + op2))
	elif operator == '-':
		print "\n" + str(op1) + " - " + str(op2) + " = " + str((op1 - op2))
	elif operator == '/':
		print "\n" + str(op1) + " / " + str(op2) + " = " + str((op1 / op2))
	elif operator == '*':
		print "\n" + str(op1) + " * " + str(op2) + " = " + str((op1 * op2))

composite_list = [ast[x:x+4] for x in range(0, len(ast),4)]
for expr in composite_list:
	eval(expr)
print "\n"