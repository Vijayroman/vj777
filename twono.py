a,e=map(int,input().split())
l=[]
for i in range(a+1,e):
  if(i%2!=0):
    l.append(i)
for i in l:
  print(i,end=' ')
