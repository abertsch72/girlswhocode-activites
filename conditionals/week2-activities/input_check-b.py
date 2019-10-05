"""
Sometimes, when we ask for input from the user, we want to make sure they
give us the right thing. We can check if conditions we set are satisfied
with conditionals.

Let's ask the user for a name and impose some conditions on that.
"""

print("This program asks you for a first name.")
print("The name must start with a capital letter")
print("The name must be between 2 and 20 characters")
print("The name must not be Bill")
# add some more conditions here!

name = input("Enter a first name: ")

if(name[0].capitalize() != name[0]):
    print("The name does not start with a capital letter!")
# fill this line in with a conditional statement!
    print("The name must be between 2 and 20 characters!")
# fill this line in with a conditional statement!
    print("The name must not be Bill!")

else:
    print("The name is valid!")