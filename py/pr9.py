class fact:
    def fact_cal(self):
        n=5
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        print(fact)

f=fact()
f.fact_cal()
