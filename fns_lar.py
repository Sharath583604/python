arr=[]
n=int(input("Enter the value of n: "))
print("Enter the values of array")
for i in range(n):
    arr.append(int(input()))
arr.sort()
print("result:",arr[n-2])
for i in range(0,n+1):
    if(i==(n-2)):
        print(arr[i])
    
