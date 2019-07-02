no1,nu2=input().split()
sam=abs(len(no1)-len(nu2))
for v in range(len(no1)):
    if len(nu2)==1 and nu2[v] in no1:
        break
    if no1[v]!=nu2[v]:
        t+=1
print(sam)
