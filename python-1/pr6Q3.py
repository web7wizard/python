
i=0
l=[]
n=int(input("enter number you want in list"))
print("enter a numbers")
while(n>i):
    l.insert(i,int(input()))
    i=i+1
key=int(input("enter number you want to search"))
for i in l:
    if i==key:
        print("found")
        break

if(i==n):
    print("not found")
