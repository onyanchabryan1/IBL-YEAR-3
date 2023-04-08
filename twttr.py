word=input("Enter a word:  ")#prompt the user to enter a word

for i in word:#iterate every character in word variable
    if not i in ['a','e','i','o','u']:#using logical not to chech whether iterated characters are available
        print(i, end="")