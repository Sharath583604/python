from array import array
n = int(input("Enter the number of elements: "))
arr = array('i', (int(i) for i in input("Enter elements: ").split()))
x=int(input("enter the number to count\n"))
for i in range(n):
    if arr[i]==x:
        count+=1
    print(count)