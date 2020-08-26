#Python program to print out the runner up score
'''
The first line contains "n". The second line contains an array  A[] of  "n" integers each separated by a space.

'''
n = int(input("How many scores: "))
arr = list(map(int, input("Enter score while seperating them with a space: ").split()))

z = max(arr) 
while z == max(arr):
    arr.remove(max(arr))
    
print(max(arr))