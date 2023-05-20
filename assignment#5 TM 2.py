numbers = set()
escape_word = "done"

while True:
    user_input = input('Enter a number, type "done" to exit: ')
    # quit the while loop if the user wants to
    if user_input == escape_word:
        break
    try:
        # convert the user_input to num
        num = float(user_input)
        # add num to numbers
        numbers.add(num)
    except:
        print("Invalid input")

print("Maximium is", max(numbers))
print("Minimium is", min(numbers))
