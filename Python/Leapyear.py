#This software checks if the inputted year is a leap year or not

response= str(input("Do you want to run the program? "))
while (response == 'Yes' or 'Y' or 'y' or 'YES' or 'yes'):
    year = int(input("Input year: "))
           
    if (year %4)==0 :
        if(year % 100) == 0:
            if( year % 400) == 0 :
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
        break

else:
    print("Bye!")