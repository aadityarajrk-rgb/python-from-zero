# f-string 
# modern , super-easy way to format and buil strings "f" stands for "formatted"

name="aadi"
age=16
is_student=True
print("my name is",name,", i am",age)
print("my name "+name+", i am "+str(age)+" years old, and student status is "+str(is_student)+".")
print(f"my name is {name},i am {age} years old, and student status is {is_student}.")
# f-string: shorter , cleaner , easier to read!

print(f"2+3={2+3}")

print(f"{{this is me}}")

# Data transformation -split()
# split(separator) str method, output: list of strings
# breaks a st ring into smaller parts
stamp="2026-08-26 20:49"
print(stamp.split(" "))  #result =['2026-08-26', '20:49']

stamp="2026-08-26"
print(stamp.split("-"))  #result = ['2026', '08', '26']


# String Repetition
# 'string'*number ,opertor , output: string
# repeats the string multiple times

print("ha"*3)  # result=hahaha
# use case- style yours logs 
# use repeated charact ers to create clear sections in output
print("="*30)

# Data extraction- Indexing and slicing
text= "python"

# 'string'[index] operator, output: sting
# indexing:extract one character by position
# Extract the first chacacter
print(text[0])
print(text[-6])

#  extract the last character
print(text[5])
print(text[-1])
#  extract "h"
print(text[3])
print(text[-3])

# 'string'[start:end:step], output:string
# sicing: extract a part of the string
date="2026-09-20"
# extract the year
print(date[0:4])
#open ended slicing- if you leave the start index empty, python starts from index0
print(date[:4])
#Extract the month
print(date[5:7])
# Extaract the date
print(date[8:])
print (date[-2:])
#  Use positive indexes- if you want to extract part from the left side(start)of a string
#  Use negative indexes - if you want to extract part from the right side(end)of a string
