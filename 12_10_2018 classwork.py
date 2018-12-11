#12/10/2018 Classwork
# Example 4 (WITO) mystery output - work through the output
# Trace table
# For loop Range(start, end, step)
# 5, 10, 15 using eval (lcv count)
#6,11,16,.... (lcv count)
# cubes (lvc n)
# 56 86 using step 2 eval input (lcv even
# double eval input difference of 2 (lcv num
# A table of squares and cubes (PFI) (lcv n)
#HW problem set 




def question10():
    for count in range(12):
        n=7*count+20
        print(n, end=', ')
    print(str(n+7)+'.')
    
#question10()


















def mysteryOutput():
    print("What is the output of this program")
    x=5
    y=1
    y=x+y
    z=x+1
    x=x+z
    y=x+z
    temp=x
    x=x+z
    z=temp+z
    
    print("The value of x is:",x, "\nthe value of y is", y, "\nthe value of z is", z)
#mysteryOutput()

def forLoopDemo1():
    for count in range(10):
        print(5*count+5, end=' ')
#forLoopDemo1()

##for x in range(10,20): # starts at 10, executes 19 but stops at 20
##    print(x)
##
##for x in range(10,20,2): #step of 2 -> starts at 10, next value of x is 10+2=12, last number to execute is 18
##    print(x)
##for x in range(25):# starts at 0, stops at 25 (24 is the last one to be used) and the step is 1
##    print(x)



def forLoopDemo2():
    for count in range(10):
        print(5*count+1, end=' ')
#forLoopDemo2()














    


    














def forLoopDemo3():
    for n in range(10):
        print((n+1)**3, end=' ')
forLoopDemo3()
def forLoopDemo4():
    n=eval(input("Enter a positive even integer:"))
    for even in range(n,n+31,2):
        print(even, end=' ')
#forLoopDemo4()

def forLoopDemo5():
    start, finish=eval(input("Enter your start and finish integers (start<finish):"))
    for num in range(start, finish+1,3):
        print(num, end=' ')
#forLoopDemo5()

def tableOfSquaresAndCubes():
    print("This output will print a table of squares and cubes.")
    n=eval(input("Your starting number is 1, enter your end number:"))
    print("\n\t n\t\t n^2\t\t n^3")
    for x in range(1,n):
        print("\t",x,"\t\t",x**2,"\t\t",x**3)




#tableOfSquaresAndCubes()
