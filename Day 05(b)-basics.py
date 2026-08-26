# Date transformation
    # replace(old,new) str method,output: string- swaps part of the text with something new
# use case- clean nemeric formats-replace commas with dot in european style decimal numbers

price="1234,56"
print(price.replace(",","."))
#  use case - change phone number format
# replace special characters with something else
phone="177-1234-56"
print(phone.replace("-","/"))
#replace() is not just for changing values you can also remove unwanted parts by replacing them with an empty string
# use case- clean phone numbers -remove special characwers from hone numbers 
print(phone.replace("-",""))

# use case- clean numberic formats
# remove symbols and commas to prepare for numeric conversion
Price="$1,299.99"
print(Price.replace("$","").replace(",",""))
# chained methods are executed in order from left to right each replace()runs on he result of the one before it.


# practice- convert the messy phone number into clean number format with only digits
number= "+49 (176) 123-4567"
print(number.replace("+","").replace(" ","").replace("(176)","176").replace("-",""))


# 2. 'string'+'string'->operator ,output:string
# joins(concatinates)two string into one 
first_name="Aditya" 
last_name="Raj"
last_name= first_name+" "+last_name
print(last_name)

# use case- build file paths ,buils dynamic paths using folder and file variables
folder= "c:/users/aditya/"
file="report.csv"
full_file_path=folder+file
print(full_file_path)