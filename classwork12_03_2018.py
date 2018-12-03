#12/03/2018
# Classwork a conversion program
# single input


def convert():
    celsius=eval(input("Enter a temperature in celsius:"))# eval is used when we want to change
    #our input to some math type (integer, real, etc.)
    fahrenheit=9/5*celsius+32  # note the good naming convention
    print(celsius,"C = ", fahrenheit,"F")
    print("Type celsius:", type(celsius))
    print("Type fahrenheit:", type(fahrenheit))
    

#convert()

def avg2():
    score1,score2=eval(input("Enter two exam scores separated by a comma:"))
    average=(score1+score2)/2
    print("The average of the two exam scores is ",average)
    print("Type score1:", type(score1))
    print("Type average:", type(average))
#avg2()

def greeting():
    #create a program that uses one input to collect a user's firstname and lastname
    #print Hello [firstname] [lastname]
    firstname=input("Enter your firstname :")
    lastname=input("Enter your lastname :")
    print("Hello", firstname, lastname)

greeting()


    
    
