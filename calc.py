print("python3-calculator")
print("function: sum(+), substract(-), product(*), quotient(/)")
x = None  #1st variable
y = None  #2nd variable
opr = None  #operator
while (True):  # get input values
    x = input("Enter the first number: ")
    opr = input("Enter the operation: ")
    y = input("Enter the second number: ")
    try:  #convert string to integer
        x = int(x)
        y = int(y)
    except ValueError:  #if value is not integer then error
        print ("Invalid number argument")
        op = None
    if (opr != None):  # decide function
        if (opr == "+"):  #addition
            print ("Sum: ", (x + y))
        elif (opr == "-"):  #substraction
            print ("Difference: ", (x - y))
        elif (opr == "*"):  #multiplication
            print( "Product: ", (x * y))
        elif (opr == "/"):  #division
            print ("Quotient: ", (x / y))
        else:  #if operator is not wiyhin (+,-,*,/) then error
            print( "Invalid operation")
    q = input("Quit? [y/n] ")  #discontinue loop (y/n)
    if (q == "y" or q == "Y"):
       break  #END
