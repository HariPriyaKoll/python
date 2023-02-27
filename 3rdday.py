'''
Write a program that works out whether if a given number is an odd or even number.
'''
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("even")
else:
    print("odd")    

'''
t should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
'''    

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight /(height * height))
print(bmi)
if bmi <= 18.5:
    print("underweight")
elif bmi <= 25:
    print("normal weight")
elif bmi <= 30:
    print("slightly overweight")
elif bmi <= 35:
    print("obese")    
else:
    print("clinically obese.")

'''
Write a program that works out whether if a given year is a leap year.
on every year that is evenly divisible by 4 

**except** every year that is evenly divisible by 100 

**unless** the year is also evenly divisible by 400
'''    
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
           print("leap year.")
        else:
           print("not leap year")    
    else:
        print("leap year")        
else:
    print("not leap year")