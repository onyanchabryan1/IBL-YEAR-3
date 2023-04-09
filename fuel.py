while True:
    fuel = input("Enter the fraction:") # prompt user for input
    try: # testing code for error
        numerator, denominator = fuel.split("/") # splitting the input fraction into numerator and denominator
        the_numerator = int(numerator) # converting numerator into int
        the_denominator = int(denominator) # converting denominator into integer
        f = the_numerator / the_denominator
        if f <= 1:
            break
    except (ValueError, ZeroDivisionError):#takes care of errors
        pass

p = int(f * 100) # percentage variable
if p <= 1:#print e if percentage less than one
    print("E")
elif p >= 99:#condition to print f if percentage greater than 99
    print("F")
else:
    print(p,"%")#condition to print actual percentage
