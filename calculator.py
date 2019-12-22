import tkinter as tk

win = tk.Tk()

win.title("Calculator")
win.geometry("250x300")

#win.resizable(False, False)
vinp = False

#Functions for buttons to call
#NUMBERS
def insert1():
	clearInvalidInput()
	display.insert(tk.END, 1)
def insert2():
	clearInvalidInput()
	display.insert(tk.END, 2)
def insert3():
	clearInvalidInput()
	display.insert(tk.END, 3)
def insert4():
	clearInvalidInput()
	display.insert(tk.END, 4)
def insert5():
	clearInvalidInput()
	display.insert(tk.END, 5)
def insert6():
	clearInvalidInput()
	display.insert(tk.END, 6)
def insert7():
	clearInvalidInput()
	display.insert(tk.END, 7)
def insert8():
	clearInvalidInput()
	display.insert(tk.END, 8)
def insert9():
	clearInvalidInput()
	display.insert(tk.END, 9)
def insert0():
	clearInvalidInput()
	display.insert(tk.END, 0)

#Clean display after "Invalid input" message is shown
def clearInvalidInput():
	global vinp
	print(vinp)
	if(not(vinp)):
		clearDisplay()
		vinp=True
#DELETE EVERYTHING ON THE SCREEN
def clearDisplay():
	display.delete("1.0","end")

#DELETE LAST INPUT
def deleteLast():
	display.delete("%s-1c" % tk.INSERT, tk.INSERT)

#OPERATIONS
def plus():
	clearInvalidInput()
	display.insert(tk.END, "+")
def minus():
	clearInvalidInput()
	display.insert(tk.END, "-")
def multiply():
	clearInvalidInput()
	display.insert(tk.END, "*")
def divide():
	clearInvalidInput()
	display.insert(tk.END, "/")

#Parenthesis
def leftPar():
	clearInvalidInput()
	display.insert(tk.END, "(")
def rightPar():
	clearInvalidInput()
	display.insert(tk.END, ")")

#Decimal Point
def decimalPoint():
	display.insert(tk.END, ".")

#Result of the input
def result():
	global vinp
	input = display.get("1.0", "end-1c") #It is "end-1c" in order not to read the space at the end
	vinp = checkValidInput(input)
	if(vinp):
		print("To Calculate: " + input)
		toDisplay = calculate(input)
		clearDisplay()
		display.insert(tk.END, toDisplay)
		#display.insert(tk.END, "PICKLES, BISH")
		print("To display: " + toDisplay)
		#When the input is valid, calculate the result

	print("--------------------------------------------------------------------------------------")

def checkValidInput(input):
	global vinp
	#Check that the inputToCheck is valid
	print("input to be checked: " + input)
	if(input==""): return True #In case nothing is on the display, so as not to get an error

	valid = True
	for char in input:
		print("Char: " + char)
		#Check that the rest of characters are valid
		if(char in "0123456789+-*/()."):
			#Passed the test of character being valid
			pass
		else:
			clearDisplay()
			print(display.get("1.0","end"))
			display.insert(tk.END, "Invalid input. Incorrect characters.")
			vinp = False
			return False #Breaks when invalid input is found

	index = 0
	while index < len(input):
		#Eliminate spaces to not get errors when calculating
		if(input[index]==" "): input[index]=""
		if(input[index-1]==")" and input[index]=="(" and index!=0): 
			input = input[0:index] + "*" + input[index:] #Two parenthesis one beside the other is a multiplication
			print("Adjusted")
		if((input[index-1]==")" and input[index] in "0123456789" and index!=0) or (input[index-1] in "0123456789" and input[index]=="(") and index!=0): 
			input = input[0:index] + "*" + input[index:]
			print("Adjusted2")
		index+=1

	

	#Decimal Point check
	if(input[0]=="." or input[len(input)-1]=="."): 
		clearDisplay()
		display.insert(tk.END, "Invalid input. Decimal point placed incorrectly")
		vinp = False
		return False

	if(not(checkOps(input))): valid = False #Checks if operations are correctly placed
	if(not(checkParenthesis(input))): valid = False #Checks that parenthesis come in pairs
	if(valid):
		print("OK")
	else:
		clearDisplay()
		display.insert(tk.END, "Invalid input. Operations or Parenthesis incorrect")
		print("Invalid input")
	return valid

def checkOps(input):
	global vinp
	#Before anything, check that the input doesn't start or end in an operator
	if(input[0] in "*/" or input[len(input)-1] in "+-*/"):
		vinp = False
		return False

	prevCharIsOp=False
	index = 0
	for char in input:
		if(input[index-1] in "+-*/" and input[index]==")"): return False #Operation on the left of closing parenthesis is invalid
		if(input[index-1] in "*/" and input[index]=="-"): #This is valid, so we jump over this
			continue
		elif(char in "+-*/" and prevCharIsOp):
			vinp = False
			return False #Case that two continuous operators are found
		elif(char in "+-*/" and not(prevCharIsOp) and index!=0):
			prevCharIsOp=True #We just came across an operator on its own
		else:
			prevCharIsOp=False #We came across a non-operator
		index += 1

	return True #No flags triggered

def checkParenthesis(input):
	global vinp
	balance = 0
	lastCharWasLPar=False
	for char in input:
		if(char in "("):
			lastCharWasLPar=True
			balance +=1
		elif(char in ")"):
			if(lastCharWasLPar):
				vinp = False
				return False #Inmediately break when we get "()"
			lastCharWasLPar=False
			balance -=1
		else:
			lastCharWasLPar=False

	if(balance==0):
		return True
	else:
		vinp = False
		return False


#This display will show what has been inputted and the result of said input
display = tk.Text(win, height=1,font=(12))
display.grid(row=0, column=0, sticky="nsew")
win.grid_rowconfigure(0, weight=1)
win.grid_rowconfigure(1, weight=1)
win.grid_columnconfigure(0, weight=1)

#This frame allows us to have buttons right under the display, so it's like
#having a grid within a grid
buttons_frame = tk.Frame(win, bg="green")
buttons_frame.grid(row=1, column=0, sticky="nsew")
buttons_frame.grid_rowconfigure(0, weight=1)
buttons_frame.grid_rowconfigure(1, weight=1)
buttons_frame.grid_rowconfigure(2, weight=1)
buttons_frame.grid_rowconfigure(3, weight=1)
buttons_frame.grid_rowconfigure(4, weight=1)
buttons_frame.grid_columnconfigure(0, weight=1)
buttons_frame.grid_columnconfigure(1, weight=1)
buttons_frame.grid_columnconfigure(2, weight=1)
buttons_frame.grid_columnconfigure(3, weight=1)



#Now we can make buttons that insert numbers into the display
#First, the numbers
bwidth=8
bheight=3 #Dimensions of the number buttons
b1 = tk.Button(buttons_frame,text="1", command=insert1)
b1.grid(row=1, column=0, sticky="nsew")
b2 = tk.Button(buttons_frame,text="2", command=insert2)
b2.grid(row=1, column=1, sticky="nsew")
b3 = tk.Button(buttons_frame,text="3", command=insert3)
b3.grid(row=1, column=2, sticky="nsew")
b4 = tk.Button(buttons_frame,text="4", command=insert4)
b4.grid(row=2, column=0, sticky="nsew")
b5 = tk.Button(buttons_frame,text="5", command=insert5)
b5.grid(row=2, column=1, sticky="nsew")
b6 = tk.Button(buttons_frame,text="6", command=insert6)
b6.grid(row=2, column=2, sticky="nsew")
b7 = tk.Button(buttons_frame,text="7", command=insert7)
b7.grid(row=3, column=0, sticky="nsew")
b8 = tk.Button(buttons_frame,text="8", command=insert8)
b8.grid(row=3, column=1, sticky="nsew")
b9 = tk.Button(buttons_frame,text="9", command=insert9)
b9.grid(row=3, column=2, sticky="nsew")
b0 = tk.Button(buttons_frame,text="0", command=insert0)
b0.grid(row=4, column=0, sticky="nsew")

#Decimal point
bdecp = tk.Button(buttons_frame, text=".", command=decimalPoint)
bdecp.grid(row=0, column=0, sticky="nsew")

#Now a button to remove the last thing inserted
bdel = tk.Button(buttons_frame, text="DEL", command=deleteLast)
bdel.grid(row=1, column=3, sticky="nsew")

#We need to have operations
bplus = tk.Button(buttons_frame, text="+", command=plus)
bplus.grid(row=2, column=3, sticky="nsew")
bminus = tk.Button(buttons_frame, text="-", command=minus)
bminus.grid(row=3, column=3, sticky="nsew")
bmul = tk.Button(buttons_frame, text="*", command=multiply)
bmul.grid(row=4, column=1, sticky="nsew")
bdiv = tk.Button(buttons_frame, text="/", command=divide)
bdiv.grid(row=4, column=2, sticky="nsew")
#Equal sign is a little different, since it will change the display to the result
bequal = tk.Button(buttons_frame, text="=", command=result)
bequal.grid(row=4, column=3, sticky="nsew")

#Parenthesis
bLPar = tk.Button(buttons_frame, text="(", command=leftPar)
bLPar.grid(row=0, column=1, sticky="nsew")
bRPar = tk.Button(buttons_frame, text=")", command=rightPar)
bRPar.grid(row=0, column=2, sticky="nsew")

#Clear the display
bC = tk.Button(buttons_frame, text="C", command=clearDisplay)
bC.grid(row=0, column=3, sticky="nsew")


#-----------------------------------------------------------------------------------------------------------------
#CALCULATION SECTION
def calculate(input):
	
	allOpsCompleted = False
	noMorePar = False

	while (not(noMorePar)):
		prevPar = False #Boolean of whether we have crossed the opening parenthesis
		start = 0
		stop = 0
		index = 0
		beginning = "" #This will be at the front of the equation. It should end up being ""
		end = "" #This will be at the end of the equation. It should end up being ""

		#First, parenthesis are important
		#Search for parenthesis portions
		for char in input:
			if(char == ")" and prevPar):
				#Whatever is between these two parenthesis takes priority
				stop = index
				break #Breaks once we have found the matching closing parenthesis
			elif(char == "("):
				#We found the start of a parenthesis
				prevPar=True
				start = index+1 #Start at whatever comes after the first parenthesis
				index+=1
			else:
				stop = index #Minus 1 to compensate for the space
				index+=1

		if(not(prevPar)):
			stop = len(input) #No parenthesis, so content == input is True
			noMorePar = True #This will end the while loop, since no more parenthesis were found
		else: #If there is parenthesis, it will reattach whatever was in front and behind
			beginning = input[0:start-1] #Puts back the start of the equation and excludes the opening parenthesis
			print("BeginningN: " + beginning)
			end = input[stop+1:] #Gets rid of closing parenthesis
			print("EndN: " + end)

		#Now calculate the content inside the parenthesis
		content=input[start:stop] #Whatever is inside the parenthesis
		print("Content: " +str(content))
		reinsert = calculateWOPar(content) #Caculate the content and save it to be reinserted
		input = beginning + str(reinsert) + end #Reinsert value into original equation
		#start+1 to get rid of opening parenthesis.
		print("StartN: " + str(start))
		print("To be reinserted: " + str(reinsert))
		print("StopN: "+ str(stop))
		print("New input: " + input)

	if(float(input)==int(float(input))): input = str(int(float(input))) #Turns it into integer if there is no decimal section
	return (input)


def calculateWOPar(input): #input == content here
	start=0
	stop=0
	index=0
	opfound=False
	opIndex = 0
	#Multiplication or division comes first, left to right
	for n in input:
		#FINDING MULTIPLICATIONS AND DIVISIONS
		#Third condition in here is to account for negative numbers or positive numbers with a + in front
		if((n=="+" or n=="-") and not(opfound) and not(input[0]=="-" or input[0]=="+")): 
			start = index+1 
		elif(input[0]=="+"):
			input[0]=="" #Getting rid of plus sign at the start since it's unnecessary
		elif(input[0]=="-"):
			start = 0 #Makes sure that calculateBasic takes the negative sign and doesn't skip it

		if((n=="*" or n=="/") and (not(opfound))): #Finding a multiplication or division
			opfound=True #Triggers that we have found an operation to do
			opIndex = index	#Now we need to find the end of the following number
		elif((n in "*/+-()") and opfound and (index!=opIndex+1)): #Triggered when we come across another operator, marking the end of the number
			stop = index
			break #This stop = index and break is for when there are more operations later on
		elif(n in "0123456789"):
				stop = index+1
		index+=1

	#Addition and Subtraction come next
	if(not(opfound)): #Triggers when neither * or / was found
		start = 0
		stop = 0
		index = 0
		for n in input:
			if((n=="+" or n=="-") and (not(opfound)) and (not(index==0))): 
				print("	Triggered")
				opfound=True #Triggers that we have found an operation to do
							 #Now we need to find the end of the following number
			elif((n in "*/()") and (not(index==0))): #Triggered when we come across another operator, marking the end of the number
				stop = index
				break
			elif(n in "0123456789"):
				stop = index+1 #If the last input is a number, then stop will be the index of the
			index+=1

	if(not(opfound)): 
		print("No operation found")
		return input #If there are no operators left, return (BASE CASE OF RECURSION)

	print("	StartW: " + str(start))
	print("	StopW: " + str(stop))
	print("	Section for calculateBasic: "+input[start:stop])
	#The two numbers are taken away to calculateBasic and returned as their result back into the original operation
	beginning = input[0:start] #From beginning until opening parenthesis excluded
	end = input[stop:] #Skip parenthesis until end
	input = beginning + str(calculateBasic(input[start:stop])) + end
	print("	Result of this iterationW: " + str(input)) 
	input = calculateWOPar(input) #Recursion until all operations inside are done
	return input

def calculateBasic(input): #We assume input is just two numbers with the operator in between
	#We must be careful when we receive a negative number on it
	operation = -1 #0: mul, 1: div, 2: add, 3: sub, -1: no operation
	opIndex = 0
	firstNum = ""
	secondNum = ""

	#Find operation. Exits when found, and opIndex stores the index of this operator
	#No need to worry about finding an operation here (and consequently going out of bounds), it is checked in calculateWOPar
	for n in input:
		if(n in "*/+-" and opIndex!=0):
			break
		opIndex+=1
	print("OP Index: " + str(opIndex))

	if(input[opIndex]=="*"):
		operation = 0
	elif(input[opIndex]=="/"):
		operation = 1
	elif(input[opIndex]=="+"):
		operation = 2
	elif(input[opIndex]=="-"):
		operation = 3

	#Turn into actual numbers
	firstNum = float(input[0:opIndex])
	secondNum = float(input[opIndex+1:])

	opResult = 0
	if(operation==0):
		opResult = firstNum*secondNum
	elif(operation==1):
		opResult = firstNum/secondNum
	elif(operation==2):
		opResult = firstNum+secondNum
	elif(operation==3):
		opResult = firstNum-secondNum
	elif(operation==-1):
		opResult = opResult #No operator found

	print("		Basic part: " + str(opResult))
	return opResult


win.mainloop()