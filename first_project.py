'''
Name-Rahul Pandey
Role:AI/ML Data Science Trainee
Project 1:Fundamental Booster
'''
print("Welcome to the Interactive Personal Data  Collector!")
name=input("Please Enter your name: ")
age=int(input("Please Enter your age: "))
print("Conversion message:User input for age  is converterd from string into integer")
height=float(input("Please Enter your height in meters: "))
print("Conversion message:User input for age  is converterd from string into float")
favourite_num=int(input("Please Enter your favourite Number:"))
print("-"*50)
print("Thanks you for sharing your information")
print("-"*50)
print("Here your information you shared")
print("-"*50)
print(f"{name}(Type:{type(name)},Memory Address:{id(name)}")
print(f"{age}(Type:{type(age)},Memory Address:{id(age)}")
print(f"{height} meter(Type:{type(height)},Memory Address:{id(height)}")
print(f"{favourite_num}(Type:{type(favourite_num)},Memory Address:{id(favourite_num)}")
birth_year=2026-age
height_in_foot=height*3.28084
print(f"Your birth year is :{birth_year}(based on your age {age})")
print(f"Your age in in height_in_foot: {round(height_in_foot,2)}(based on your height {height})")
print("Thank you  for using  the Personal Data Collector.See You again!")
