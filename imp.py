'''
	
	Code by Will Hodges on 10/23/15
	
'''

from calc import * # Import the parser!

parser = calcParser() # Create an instance of the parser!

print "\n\n     Will Hodges Python Interpreter Calculator 10/23/15" # Greet the user

print "\n\nWelcome to the WHPIC! Enter an expression (or series of expressions) \
		below.\n\nSeperate each by a semicolon and nothing more!\n"  # Explain to the user

user_input = raw_input("Equation: ") # Get the equation from the user

ast = parser.parse(user_input, rule_name='start') # Parse the equation (easy, right?)

def eval(expr): # Create the evaluator of the expression
	operator = expr[1][0] # Get the operator
	op1arr = expr[0][0] # Get the first operand (multi-digit numbers are split into characters) 
	op1str = '' # Blank for now...
	for num in op1arr: # For each character
		op1str = op1str + num # Append it to op1str
	op1 = int(op1str) # convert op1str to an integer for use later
	
	op2arr = expr[2][0] # Get the second operand (multi-digit numbers are split into characters) 
	op2str = '' # Blank for now
	for num in op2arr: # For each character
		op2str = op2str + num # Append it to op2str
	op2 = int(op2str) # convert op2str to an integer for use later
	
	if operator == '+': # If addition 
		print "\n" + str(op1) + " + " + str(op2) + " = " + str((op1 + op2)) # Nicely print the problem and the answer
	elif operator == '-': # If subtraction
		print "\n" + str(op1) + " - " + str(op2) + " = " + str((op1 - op2)) # Nicely print the problem and the answer
	elif operator == '/': # If division
		print "\n" + str(op1) + " / " + str(op2) + " = " + str((op1 / op2)) # Nicely print the problem and the answer
	elif operator == '*': # If multiplication
		print "\n" + str(op1) + " * " + str(op2) + " = " + str((op1 * op2)) # Nicely print the problem and the answer

composite_list = [ast[x:x+4] for x in range(0, len(ast),4)] # Split the parsed info into separate equations
for expr in composite_list:	# For each expression			# (one equations contains: operand1, operator, operand2,
	eval(expr)				# Evaluate it!					# and a semicolon
print "\n" # Make a buffer between our info and the chatter from the terminal