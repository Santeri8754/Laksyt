import random
n=0
N=10000
kerrat=0
while kerrat<N:
    kerrat+=1
    x=float(random.randint(-1,1))
    y=float (random.randint(-1,1))
    if (x**2+y**2<1):
        n=n+1


pii= 4*n/N
print(pii)
