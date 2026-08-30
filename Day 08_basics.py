Data="968-Maria, ( D@t@ Engineering );; 27y  "
print(Data.strip().replace("968","name") .replace("-",":") .replace(","," |").replace("(","role:").lower().replace("(","|").replace("@","a").replace(");;","| age:").replace("y","").rstrip())

# string function - searching
phone= "+49-176-12345"

# startswith(substring):str method, output:boolean= checks if the s tring begins with a specific word
print(phone.startswith("+49"))

# is the email from gmail? check the domain(gmail.com)
email="adityarajrk@gmail.com"
# endswith(substring):str  method, output:boolean = checks if the string ends with a specific words
print(email.endswith("gmail.com"))

file="data_backup.csv"
print(file.endswith(".csv"))

# 'substring'in'sring' = checks if a word exists in the string
email="adityarajrk@gmail.com"
print("@"in email)

url="https://api.company.com/v1/data"
print("/api"in url)

# find() is   great when combined with other methods to add dynamics
phone1= "+49-176-12345"
phone2= "49-654-16548"
# extract only phone number without country code
print(phone1[4:])
print(phone2[3:])

# hardcoding the start position doesn't work when the country code length changes
# find(substring)  str method, output:number= returns the starting position of a word in the string
print(phone1.find("-"))
print(phone1[phone1.find("-") +1:])
print(phone2[phone1.find("-")+1:])
# find () is great when combined with other mehhods to add dynamic
