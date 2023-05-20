largest = None
smallest = None
escape_word = "done"


while True:
    user_input = input('Enter a number, type "done" to exit: ')
    # quit the while loop if the user wants to
    if user_input == escape_word:
        break
    try:
        # convert the user_input to num
        num = float(user_input)
        # if the largest or smallest variables arent set, change them to num.
        # otherwise keep them the same
        largest = num if largest is None else largest
        smallest = num if smallest is None else smallest
        # if num is larger than the largest variable, change it to num
        largest = num if num > largest else largest
        # if num is smaller than the smallest variable, change it to num
        smallest = num if num < smallest else smallest
    except:
        print("Invalid input")

print("Maximium is", largest)
print("Minimium is", smallest)
