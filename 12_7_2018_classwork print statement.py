#12/7/2018 Classwork
#Escape Sequence| Description
#  \n           | Newline. Position the cursor at the beginning of the next lne
#  \t           | Horizontal tab. Moves the cursor to the next tab stop
#  \\           | Print a backslash character in a print statement
#  \"           | Print a double quote character in a print statement


# String concatenation
# Input versus eval
# Example 1(PFI) Enter your name and then greeting
# Exampe 2 (WITO) greeting with name as a parameter
# Example 3 (PFI) with fraction input output



#print("This" + " 3 " + "is a number" + 24)
#operator overloading
#The operator + can add depending on the type on either side of +
#It does different things depending on the type
# string + String  is okay
# int + int is okay
# float + int is okay
#float + float is okay
# int + string or float + string generates an error


x=5
#print("Hello" + x)# error
print("Hello" + str(x))
print(type(x))


x="3"
y="4"

print(x+y)
print(type(x), type(y))
print(int(x)+int(y))
print(type(x), type(y))

def greeting():
    name=input("Enter your name:")
    print(name, ", welcome to the computer science class!")
    print("Have a nice day!")
#greeting()

# for the next program you can either define the parameter name in
#the python shell after

def greeting2(name): #using a parameter
    print("hello "+ name, ", welcome to the computer science class!")
    print("Have a nice day!")



def fractionProgram():
    print("This program will ask you for a fraction.")
    numerator=input("Enter the numerator:")
    denominator=input("Enter the denominator:")
    print("The fraction you entered is", numerator+"/"+denominator)
fractionProgram()















           

    


        
