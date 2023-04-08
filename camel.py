string=input("Enter string in camel case: ")#prompts user to enter string in camel case

string=string[0].lower()+ string[1:]#converts first letter of string to lowercase followed by the rest of the string

#in the code below,using loop to iterate over each character in string. for each character, if an uppercase is found, it replaces it with an underscore followed by the lowercase version of the same letter

for i in string:
    
    if i.isupper():
        string=string.replace(i,"_" + str(i.lower()))
print(string)
