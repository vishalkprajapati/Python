import datetime

name=input("Enter your name:")
age=int(input("Enter your age:"))
now=datetime.datetime.now()
print(name," will turn 95 in ",(95-age)+now.year)
input("Press enter to exit") #To hold the screen