class reverse:
    def rev_word(self,s):
        l=reversed(s.split())
        ans=""
        for k in l:
            ans=ans+k+" "
        return ans
obj=reverse()
s=input("enter a string")
ans=obj.rev_word(s)
print(ans)