#import tensorflow
#from tensorflow import keras
import function1
import function2

year = int(input("Enter current year:"))
yob = int(input("Enter date of birth:"))
age = function1.find_age(year, yob)

name= input("Enter first name: ")
surname= input("Enter surname: ")
full_name= function2.get_name(name, surname)

print("Name:", full_name)
print("Age: ", age)
