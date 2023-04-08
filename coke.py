print("amount due: 50")#shows on the screen price of coke
amount_due=50#variable containing value of the coke
coins_added=0

while True:  #using a loop that breaks only when  the amoung coins added are more than 50
    insert_coin=int(input("Enter a coin"))#prompts user to enter coin
    if insert_coin==25 or insert_coin==10 or insert_coin==5:  #checks if coin entered are accepted
        amount_due=amount_due-insert_coin#calculates amoint due after inserting a coin
        coins_added+=insert_coin#keeping track of the coins added

    else:
        print( "amount due: " ,amount_due)

    if coins_added>=50:#conditional statement if coins added are more than 50 to end the code
        print("change owed:", coins_added-50)
        break

    else:#if not the code continues
        print( "amount due: ",amount_due)
