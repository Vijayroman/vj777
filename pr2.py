from itertools import combinations
s,y=input().split()
m=int(m)
saw=[]
c=len(s)-m
f=combinations(s,c)
for i in list(f):
  saw.append("".join(i))
print(min(saw))
