hrs = input("Enter Hours:")
rate = input('enter hourly rate')

h = float(hrs)
r = float(rate)

pay = (r*h)
otpay = (pay) + (h - 40.0)*r * .5

if h<=40:
   print (pay)
elif h>40:
    print (otpay)