# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
def hello ():
    print("Hi Hello")

# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
def pack(A1, A2, A3):
    return [A1, A2, A3]

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list),
# and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.

def eat_lunch(F_list):
    if not F_list:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {F_list[0]}")
        for item in F_list[1:]:
            print(f"Next I eat {item}")