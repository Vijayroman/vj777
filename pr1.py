s=int(input())
n=[]
l=[]
n1=[]
for i in range (s):
    n.append(input())
    
for i in range (0,s):
    l.append( len(n[i]))
k=min(l)
if(k!=1):
    i=0
    for j in range(0,k):
        if((n[i][j]==n[i+1][j]) ):
            n1.append(n[i][j])
print(*n1,sep='')
