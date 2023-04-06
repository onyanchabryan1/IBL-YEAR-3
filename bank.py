# bank.py

# Prompt user for greeting
greeting = input("Please enter a greeting: ").lstrip()

# Check the first letter of the greeting
if greeting.lower().startswith("hello"):
    print("$0")
elif greeting.lower().startswith("h"):
    print("$20")
else:
    print("$100")
