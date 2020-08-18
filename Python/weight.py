print("This is a simple weight converter app")
print('*' * 100)

print("In what unit would you want to check your weight in: ")
options = int(input("Press (1) for lb(pounds) \nPress (2) for kg(kilogram): \n"))
print('*' * 100)
if options == 1 :
    weight = input('Please input your weight in lb (pounds): ')
    convert = float(weight) *  0.45
    print(f"Your weight in kg(kilograms) is: {convert}")
elif options == 2 :
    weight = input('Please input your weight in kilograms: ')
    convert = float(weight) /  0.45
    print(f"Your weight in lb(pounds) is: {convert}")
else:
    print("Please restart the program and input a valid response")
