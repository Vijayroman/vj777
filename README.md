num,si=input().split()
vj=0
if len(num)>len(si):
  num,si=si,num
p=0
while p<len(num):
  vj+=(ord(si[p])-ord(num[p]))
  p+=1
for p in range(p,len(si)):
  vj+=ord(si[p])-ord('a')+1
print(vj)
