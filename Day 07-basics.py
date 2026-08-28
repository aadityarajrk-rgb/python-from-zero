# Data Cleaning - Remove Space
text= "  Engineering".lstrip()  # lstrip()- str method, output: string = removes space from the left of a sting
print(text)

# rstrip()- str method, output : string = remove spaces from the right side of a string
text="Engineering ".rstrip()
print(text)

# strip()- removes spaces from both ends
text=" Engineering ".strip()
print (text)

# . best practice- trim spaces from user input= you never know where users might add spaces use.strip() to remove all extra spaces from both ends
# . it removes tabs and multiple spaces
# . only removes spaces at the start or end, not in the middle

#  it removes any characters you want from the start and end- not just spaces
text="###Abc###".strip("#")
print(text)

# use case - detect extra space
# check the length before and after strip() to find unwanted spaces
text="  Engineering"
print(len(text))
print(len(text.strip()))

print(len(text)-len(text.strip()))
print(len(text)==len(text.strip()))

nr_of_space=len(text)-len(text.strip())
is_clean = len(text)==len(text.strip())
print("nr_of_space:",nr_of_space)
print("is my data clean?:",is_clean)

# Data cleansing = Case Conversion
text="python PROGRAMMING"
# use case - standardize text case= make sure text is always  in lowercase
# lower() str medthod, output: string = makes all letter lowercase
print(text.lower())
print(text.upper())

# use case - clean data for matching  = lowercase all text to prevent case- based mismatches during search or comparison
search="Email ".lower().strip()
data =" emAil".lower().strip()
print(search==data)

#  best practice- clean before search = always trimm spaces and lowercase your data and search terms before matching


