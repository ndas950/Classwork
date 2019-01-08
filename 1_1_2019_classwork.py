#1_8_2019 if then else



# == is similar to the = sign in math
# to compare two types we use the ==  comparison operator
# 3==4  returns False
#3==3 returns True
# and   for an and statement to be True both sides of it needs to be True
# or    for an or statement to be True only one side needs to be True
# 3!=4  => 3 is not equal to 4
#>= means greater than or equal to 



def iffyProgram():
    n,m=eval(input("ENter two numbers separated by a comma:"))

    if n>m:
        print(n,"is greater than", m)
    else:
        if m>n:
            print(m,"is greater than",n)
        else:
            print(m, "is equal to",n)




#iffyProgram()
def iffyProgram2():
    n,m=eval(input("ENter two numbers separated by a comma:"))

    if n>m:
        print(n,"is greater than", m)
    elif m>n:
        print(m,"is greater than",n)
    else:
        print(m, "is equal to",n)




iffyProgram2()




