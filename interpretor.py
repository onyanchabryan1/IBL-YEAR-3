# interpreter.py

# Prompt user for arithmetic expression
expr = input("Please enter an arithmetic expression (in the format 'x y z'): ")

# Split the input into its components
x, op, z = expr.split()

# Convert x and z to integers
x = int(x)
z = int(z)

# Calculate the result based on the operator
if op == "+":
    result = x + z
elif op == "-":
    result = x - z
elif op == "*":
    result = x * z
else:
    result = x / z

# Output the result as a float with one decimal place
print("{:.1f}".format(result))
