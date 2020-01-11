# Python program showing how to 
# multiple input using split 

# taking two inputs at a time 
print("taking two inputs at a time")
x, y = input("Enter a two value: ").split() 
print("Number 1: ", x) 
print("Number 2: ", y) 
print() 
print("__________________________________________________")
print() 

# taking two inputs at a time 
print("taking two inputs at a time ")
a, b = input("Enter a two value: ").split() 
print("First number is {} and second number is {}".format(a, b)) 
print() 
print("__________________________________________________")
print() 

# taking multiple inputs at a time 
# and type casting using list() function
print("taking multiple inputs at a time\nand type casting using list() function")
x = list(input("Enter a multiple value: ").split()) #list(map(int, input("Enter a multiple value: ").split()))
print("List of number: ", x) 
print() 
print("__________________________________________________")
print() 
#========================================================================

# Python program showing 
# how to take multiple input 
# using List comprehension 

# taking three input at a time 
print("taking three input at a time")
x, y, z = [ x for x in input("Enter three value: ").split()] #int(x) before for
print("First Number is: ", x) 
print("Second Number is: ", y) 
print("Third Number is: ", z) 
print() 
print() 
print("__________________________________________________")
print() 

# taking two inputs at a time 
print("taking two inputs at a time")
x, y = [ x for x in input("Enter two value: ").split()] #int(x) before for
print("First number is {} and second number is {}".format(x, y)) 
print() 
print() 
print("__________________________________________________")
print()

# taking multiple inputs at a time 
print("taking multiple inputs at a time ")
x = [ x for x in input("Enter multiple value: ").split()] #int(x) before for
print("Number of list is: ", x) 
print() 
print("__________________________________________________")
print() 