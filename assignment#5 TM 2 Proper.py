numbers = set()
escape_word = "done"
input_message = "Enter any number. (type 'done' to exit)"
running = True


def handle_input(user_input):
    """
    escape if the user wants to.
    try to convert the user_input to a float and add it to the number set.
    print the exception and return true if conversion fails
    """
    if user_input == escape_word:
        return False
    try:
        numbers.add(float(user_input))
        return True
    except Exception as e:
        print(e)
        return True


while running:
    user_input = input(input_message)
    running = handle_input(user_input)

if len(numbers) > 0:
    print(f"Max: {max(numbers)}, Min: {min(numbers)}")
