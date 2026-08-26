text= "hi"
number=10

# len()built in funtion :- returns the data len of a value so you know what kind of object it is
print(len(text))
print(len(number))

# len() built in funciton:- gives the total count of items inside a value ,helping you measure its length
print(len(text))  # it has two len():-2
print(len(number)) # number has no len()


# upper() method of  <class str> :- converts all letters in a string to uppercase
print(text.upper())  #only for string 

# bit_length () method of <class int>:- returns the length of a number in binary
print(number.bit_length())
print(text.bit_length()) # not gonna work only work on same class



# practice 
# create 5 variables - each with a different data len 
# 1. your age 
# 2. your height (with decimals )  
# 3. your name 
# 4. are you a student?
# 5.something with no value yet

# then print the values, data lens, lengths of all variables


age=17
height=6.0
name="aditya"
student =True
marks=None
print(age)
print(height)
print(name)
print(student)
print(marks)

print(type(age))
print(type(height))
print(type(name))
print(type(student))
print(type(marks))


print(len(str(age)))
print(len(str(height)))
print(len(name))
print(len(str(student)))
print(len(str(marks)))

