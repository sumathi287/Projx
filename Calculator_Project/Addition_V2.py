num = 0  #global variable

num_mul = 1

num_div = 1

count = 1 #global variable

count_1 = 0 #global variable

num_result = [] #global variable

mode = ""

#temp = 0

def division_fun(temp):
    global count
    global num_div
    global num
    global mode
    try:

        if count == 1:
            num_div = temp
        else:
            num_div = num_div / temp

            num = num_div
    except ZeroDivisionError:
        print("Zero cannot be divisor")
        mode = 'Q'


def multiply_fun(temp):
    global num_mul

    global num

    num_mul = num_mul * temp

    num = num_mul

    #print("thye num value is", num)

def subtraction_fun(temp):
    '''function for performing subtraction operation mode'''
    global num  #declare global variable

    global count #declare gloable variable
    
    #logic to subtraction operation

    if count == 1: #condition to checking whether it is first input from user or not and if it is first input then change the sign of the first input get from user
        temp = (-(temp))

    num = num - temp


def addition_fun(temp):
    '''function for performing addition mode operation mode'''
    global num #declare global variable

    #logic for addition operation

    num = num + temp


def calculator_fun():
    '''this function block hold the code block for called the required function to perform the selected mode'''
    global count

    global sub_var1

    global sub_var2

    global num_result


    global count_1

    global num_result

    global num
    global mode

    #global temp

    if mode == 'Q':
        return
    var = input(f"number {count}:\n")  # get a input from user

    var = var.replace(" ","")

    # logic to abort the process while press the enter key insted of press a  numbers

    if var == "":
        return
    
    #checking the whether input is valid or not and perform the calling function for required operation mode

    try:

        if str(var) != "Q":
            if mode == 1:
                if '.' in var:
                    var = float(var)
                else:
                    var = int(var)
                if var >= 0: # the code present in the if block have be  executed ,if input data is positive int
                    #logic to insert the input data (+Ve) inside the list
                    num_result.append(var) 
                    num_result.append('+') 
                else: # the code present in the else block have be  executed ,if input data is negative int
                    #logic to insert the input data (-Ve) inside the list
                    num_result.append('(') 
                    num_result.append(var) 
                    num_result.append(')') 
                    num_result.append('+') 
                addition_fun(var) #called the function to perform addition opertaion
                count += 1 #increment the count of global variable 
                count_1 += 1 #increment the count of global variable 
                calculator_fun()
            elif mode == 2:
                if '.' in var:
                    var = float(var)
                else:
                    var = int(var)
                if var >= 0:
                    num_result.append(var) 
                    num_result.append('-') 
                else:
                    num_result.append('(') 
                    num_result.append(var) 
                    num_result.append(')') 
                    num_result.append('-') 
                subtraction_fun(var)
                count += 1 #increment the count of global variable 
                count_1 += 1 #increment the count of global variable 
                calculator_fun()
            elif mode == 3:
                if '.' in var:
                    var = float(var)
                else:
                    var = int(var)
                if var >= 0: # the code present in the if block have be  executed ,if input data is positive int
                    #logic to insert the input data (+Ve) inside the list
                    num_result.append(var) 
                    num_result.append('*') 
                else: # the code present in the else block have be  executed ,if input data is negative int
                    #logic to insert the input data (-Ve) inside the list
                    num_result.append('(') 
                    num_result.append(var) 
                    num_result.append(')') 
                    num_result.append('*') 

                multiply_fun(var)
                count += 1 #increment the count of global variable 
                count_1 += 1 #increment the count of global variable 
                calculator_fun()


            elif mode == 4:
                if '.' in var:
                    var = float(var)
                else:
                    var = int(var)
                if var >= 0: # the code present in the if block have be  executed ,if input data is positive int
                    #logic to insert the input data (+Ve) inside the list
                    num_result.append(var) 
                    num_result.append('/') 
                else: # the code present in the else block have be  executed ,if input data is negative int
                    #logic to insert the input data (-Ve) inside the list
                    num_result.append('(') 
                    num_result.append(var) 
                    num_result.append(')') 
                    num_result.append('/') 

                division_fun(var)
                count += 1 #increment the count of global variable 
                count_1 += 1 #increment the count of global variable 
                calculator_fun()

        elif str(var) == "Q" and count != 1: #the block of code executed after user enter the 'Q' to and the process and get result
             # Logic to For a list of numbers, convert each element to a string first  
             delimiter = "" # Define a delimiter
             num_result_1 = map(str, num_result) # Convert each element into a string first
             
             final_result = delimiter.join(num_result_1)

             final_result = final_result[:-1] #to remove the last element in the string-->purpose-->to remove '+' present in the end of the string
             print(f"the result is\n{final_result} = {num}") #print the result n the console screen

    except ValueError:
        print("invalid expression") #print the statement on the console screen if user enter the invalid expression


prompt = ""

'''code block to select a select a mode of operation and called the function inside the block to perform the selected operation'''
while prompt == "":
    # mode = input(
    # "select the mode to operation\n1. Add\n2. Subtract\n3. Multiply\n4. Devide\nQ .For quit the operation\n")
    mode = input(
        "select the mode to operation\n1. Add\n2. Subtract\n3. Multiply\n4. Devide\nQ .For quit the operation\n")
    
    if mode == "Q":
        break
    # logic to find the input is valid or not

    try:
        mode = int(mode)

    except ValueError:
        print("enter a valid number like 1 , 2 , 3, 4 - do not use text")
        continue

    # Perform addition mode
    if mode == 1:
        print("enter the number to addition\n")
        calculator_fun()
        prompt = 'quit'
    elif mode == 2:
        print("enter the number to subtraction\n")
        calculator_fun()
        prompt = 'quit'
    elif mode == 3:
        print("enter the number to multiply\n")
        calculator_fun()
        prompt = 'quit'
    elif mode == 4:
        print("enter the number to divide\n")
        calculator_fun()
        prompt = 'quit'

    else:
        print("warning:\nyou are select wrong mode")
        print("press enter key to continue\npress 'Q'or any text to abort")
        prompt = input()
