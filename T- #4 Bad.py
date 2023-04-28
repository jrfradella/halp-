def computepay1(h, r):
    return (
        float(h) * float(r)
        if float(h) <= 40
        else (float(h) * float(r)) + (float(h) - 40) * (float(r) * 0.5)
    )


print(
    f"Pay: {computepay1(input('Enter Your Hours:'), input('Enter Your Hourly Rate:'))}"
)
