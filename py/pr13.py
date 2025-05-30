l1=[10,20.30]
while true:
    print("enter 1:add 2:delete 3:search 4:sort 5:length 6:min 7:max 8:none")
    ch=(input("your choice")
    if ch=="1":
        n=int(input("number you want to insert"))
        l1.append(n)
           break
    if ch==2:
           n=int(input("number you want to delete"))
           l1.remove(n)
           break
    if ch==3:
           n=int(input("number you want to search"))
          if n in l1:
              print("found")
          else:
              print("not found")
          break
    if ch==4:
        print("sorted list",l1.sort())
        break
    if ch==5:
        print("length ",l1.__len__())
        break
    if ch==6:
        print("minimum ",l1.min())
        break
    if ch==7:
        print("maximum ",l1.max())
        break
           
     
