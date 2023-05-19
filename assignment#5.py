largest = None
smallest = None

while True:
    num = input('Enter a number, type "done" to exit: ')
    if num == 'done':
        break
    try:
        float(num)
        for i in num:
            if largest is None:
                largest = i 
            elif i > largest:
                largest = i
            
        for p in num:
            if smallest is None:
                smallest = p
            elif p < smallest:
                smallest = p
    except:
        print('Invalid input')
 
print ('Maximium is', largest)
print ('Minimium is', smallest)
