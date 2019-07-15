san=int(input())
ping=list(map(int,input().split()))
ping.sort()
print(*ping,end=' ')
