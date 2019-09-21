"""
For this program, let's ask the user for 10 inputs and then print them in sorted order.

Fill in the first TODO to get started and then play around with the program. There are
some suggestions at the bottom of activites to try!
"""

# get 10 inputs
# these are strings, but you can cast them to any type
print("Enter string inputs: ")
input1 = input("Enter a value: ")
input2 = input("Enter a value: ")
input3 = input("Enter a value: ")
input4 = input("Enter a value: ")
input5 = input("Enter a value: ")
input6 = input("Enter a value: ")
input7 = input("Enter a value: ")
input8 = input("Enter a value: ")
input9 = input("Enter a value: ")
input10 = input("Enter a value: ")

# we have to add all the inputs to one place to sort them.
# let's add them to a list!
inputs = []
inputs.append(input1) # append inserts at the end
inputs.append(input2)
# TODO: finish adding all the inputs!

print(inputs)
inputs.sort()
print(inputs)

# TODO: try different words, uppercase and lowercase. How does sort order the list?
# TODO: try inputting numbers (remember to cast to int!)
# TODO: when would it be useful to order a list?
# TODO: If you think of any ideas you want to try, a facilitator can help you make them happen!