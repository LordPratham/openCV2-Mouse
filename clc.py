
import math as m

x= float(input("Enter a Number "))
# ans = x*(m.sqrt(x+1) - m.sqrt(x))
ans  = (1-m.cos(x))/pow(x,2)
print(round(ans,6))