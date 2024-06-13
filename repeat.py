arr=[]
n=int(input("Enter the value of n: "))
print("Enter the values of array")
for i in range(n):
    arr.append(int(input()))
for i in range(0,n):
    for j in range(i+1,n):
        if(arr[i]==arr[j]):
            print("Repeted :",arr[i])
