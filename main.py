# #import tensorflow
# #from tensorflow import keras
# import fullName
# from age import findAge

# year = int(input("Enter current year:"))
# yob = int(input("Enter date of birth:"))
# age = findAge.find_age(year, yob)

# name= input("Enter first name: ")
# surname= input("Enter surname: ")
# full_name= fullName.get_name(name, surname)

# print("Name:", full_name)
# print("Age: ", age)


import keras
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

