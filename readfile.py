"""
r stands for read, w stands for write, a stands for append
"""
# This code is reading the contents of a file named "name.txt" and printing out each line with the
# word "Hello" before it. The `with` statement is used to open the file and automatically close it
# when the block of code is finished. The `readlines()` method is used to read all the lines of the
# file and return them as a list of strings. The `rstrip()` method is used to remove any trailing
# whitespace characters from each line before printing it.

with open("name.txt", "r")as file:
    lines=file.readlines()


for line in lines:
    print("Hello", line.rstrip())



