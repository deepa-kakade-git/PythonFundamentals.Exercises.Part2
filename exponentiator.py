#a = 4
#b = 2

def exponent_fun(a, b): 
    """Function returns exponent of a to the power b"""
    return a ** b

# Call the function and print the result
#print(exponent_fun(a, b))

def raise_to_fourth_power(c):
    """function to raise the given number to the fourth power"""
    return exponent_fun(c, 4)

square = lambda x: exponent_fun(x, 2)
cube = lambda x: exponent_fun(x, 3)

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))


