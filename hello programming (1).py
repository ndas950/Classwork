#this is a comment- name - Nishad Das



##print("Hello, Nishad. Welcome to the python programming class! ")
##
##def greet(person):
##	print("Hello ", person) #make a comment here about person
##	print("How are you?")
##
##name="Caroline"
###greet(name)
##name="Jonah"
##greet(name)


def main():
	print("This program illustrates a chaotic function!")
	x=eval(input("Enter a number between 0 and 1:"))
	for count in range(10):
		x=3.9*x*(1-x)
		print(x)
		
main()
