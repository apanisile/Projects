#Simple python program to compare different numbers
num1 = float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))
num3= float(input("Enter the third number:"))


#Check the largest of the three
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and ( num2 >= num3):
    largest = num2
else:
    largest = num3
    
print("The largest number is: ", largest)