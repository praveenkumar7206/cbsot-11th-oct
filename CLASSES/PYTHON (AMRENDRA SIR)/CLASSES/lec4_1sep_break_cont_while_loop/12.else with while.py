i = 1
while i<=5:
    if i==3:
        break   # break sabko rook deta hai jo while ke sath aata hai and yaha else while ke sath hai soo else bhi act nhi karega
    print(i)
    i=i+1
else:
    print("loop executed")


i = 1
while i<=5:
    i=i+1
    if i==3:
        continue
    print(i)
    
else:
    print("loop executed")