import math
l = [4,4,4,3,4,3,2,5]
f=-math.inf
s=-math.inf
for i in range(len(l)):
    if l[i]>f:
        s=f
        f=l[i]
    elif l[i]<f and l[i]>s:
        s=l[i]

print(f)
print(s)        
-math.inf