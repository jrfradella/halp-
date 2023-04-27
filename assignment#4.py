def computepay(h, r):
    h = float(hrs)
    r = float(rate)
    pay = (h * r)
    otpay = (h*r) + (h-40)*(r*.5)
    if h<=40:
        return pay
    elif h>40:
        return otpay

hrs = input('Enter Your Hours:')
rate = input('Enter Your Hourly Rate:')
p = computepay(hrs, rate)
print ('Pay', p)