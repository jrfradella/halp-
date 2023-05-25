file = open(input('Enter a file name: '))
count = 0
num = 0
for line in file:    
    if 'X-DSPAM-Confidence:' in line:
        count = (count + 1)
        var = line.find(' ')
        num = float(line[var:]) + num
print('Average spam confidence:', num/count)