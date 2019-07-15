var=int(input())
vst=list(map(int,input().split()))[:var]
vst.sort()
print(*vst,end=" ")
