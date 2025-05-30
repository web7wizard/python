t=(1,2,3,4,4)
print("max= ",max(t))
print("min=  ",min(t))
p=()
print(p)

flag=0
print("common data")
for i in t:
    if(t.count(i)>1):
        print(i)
        flag=flag+1
    
print("apperance =  ",flag)

tt=("zero","one","two","three","four")
s=" "
n=1234
while(n>0):
    i=n%10
    n=n//10
    s=tt[i]+"  "+s
print(s)
    


    
