a=[]
n=int(input("Enter number of elements:"))

for i in range(1, n + 1):
    b = int(input("Enter element:"))
    a.append(b)

print(a)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print(even)
print(odd)
