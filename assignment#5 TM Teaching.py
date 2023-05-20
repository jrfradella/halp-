user_input = "300"
print(user_input, type(user_input))
# this returns a float but does not change the user_input variable to a float
float(user_input)
# user_input variable is still a string
print(user_input, type(user_input))
# since strings are iterable, you can print each carachter of the string
for char in user_input:
    print(char, type(char))
# you can also convert strings to lists
print(list(user_input))
# actually change the user_input variable to a float
user_input = float(user_input)
print(user_input, type(user_input))
# floats are not iterables.
# but we'll try to iterate over the float anyway with a for loop
try:
    for i in user_input:
        # the code wont make it this far since the type is a float
        print(i)
except Exception as e:
    # this exception will occur because we are trying to iter over a float
    # should print 'float' object is not iterable
    print(user_input, type(user_input), e)


# just add the float into a set
# sets are like lists, but faster and auto remove duplicates
all_the_floats = set()
all_the_floats.add(user_input)
# add two more floats to the set
all_the_floats.add(100.0)
all_the_floats.add(255.8)

# print the set
print(all_the_floats)
# get the max value in the set
largest = max(all_the_floats)
# get the min value in the set
smallest = min(all_the_floats)
# get the sum of all values in the set
total = sum(all_the_floats)
# get the average value of the set
average = total / len(all_the_floats)
# print it out
print(f"SML:{smallest}, LRG:{largest}, SUM:{total}, AVG:{average}")
