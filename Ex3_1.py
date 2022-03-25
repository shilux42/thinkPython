"""Write a function named rightJustify that takes a string names s as a parameter and prints the string with
enough leading space so that the last letter of the string is in column 70 of the display."""

def rightJustify(s):
    print(" " * (70 - len(s)) + s)

rightJustify('monty')
