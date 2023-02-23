# data types
print("vamsi"[2])
'''
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
'''

two_digit_number = input("Type a two digit number: ")
number1 = two_digit_number[0]
number2 = two_digit_number[1]
number3 = int(number1)
number4 = int(number2)
print (number3 + number4)

'''
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
'''

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(type(height))
bmi = int(weight) / float(height) ** 2
print(int(bmi))

'''
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
'''

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
rmage = 90 - int(age)
days = rmage * 365
weeks = rmage * 52
months = rmage * 12
print(f"you have {days} days,{weeks} weeks,and {months} months left")
