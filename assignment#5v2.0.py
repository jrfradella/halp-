largest = None
smallest = None

while True:
    num = input('Enter a number, type "done" to exit: ')
    if num == 'done':
        break
    try:
        num=float(num)
    except:
        print('Invalid input')
        continue

    
    if largest is None:
        largest = num 
    elif num > largest:
        largest = num
            
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
 
print ('Maximium is', largest)
print ('Minimium is', smallest)
