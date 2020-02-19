# 
# Example file for variables
#

# Declare a variable and initialize it
f=10
g=[1,210,5,7]

# # re-declaring the variable works
f=11
print(f,g)

# # ERROR: variables of different types cannot be combined


# Global vs. local variables in functions
def function():
    global f
    # line 18 changed the scope of f here in this function to global
    f="ABC"
    global g
    print(f,g)
function()
#function() will print ABC since f here will be inside the function i.e local variable
print(f)
#this print(f) will print the value of globally defined f variable at line 6

del f
print(f)
