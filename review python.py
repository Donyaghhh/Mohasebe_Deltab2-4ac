# mohasebe Delta b2-4ac
def delta (a,b,c):
    return (b**2) - (4*a*c)

a,b,c = 1 , 6 , 7
d = delta (a,b,c)
print ('Delta =' , d)

if d < 0 :
    print ('It has no root')

elif d == 0 :
    x = -b /(2*a)
    print ('It has a root')

else:
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    print ('It has two roots' , (round(x1)) ,'and' , (round(x2)))
    # print (f"{x1:.2f}, {x2:.3f}")

# mohasebe logaritm
import math

def log_aritm10(number):
    result= math.log10(number)
    return round (result , 2)

number = 100000
print (log_aritm10 (number))