mylist=[]
n = int(input("").strip())
for count in range(1, n+1):
    mylist.append(count)
    if count%3==0 and count%5==0 :
        print("FizzBuzz")
    elif count%3==0 and not count%5==0:
         print("Fizz")
    elif count%5==0 and not count%3==0:
        print("Buzz")
    else:
        print(count)
