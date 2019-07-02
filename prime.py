now=int(input())
if now>1:
  for i in range(2,now):
    if now%i == 0:
      print("no")
      break
  else:
      print("yes")
else:
    print("no")
