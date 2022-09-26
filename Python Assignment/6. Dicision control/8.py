from calendar import c


a=int(input("Enter a , b  and c value"))
b=int(input())
c=int(input())
d=b*b-4*a*c
if d>0:
    print("Two distinct root")
elif d<0:
    print("Imaginary root")
else:
    print("Equar root")