#Input - Takes in the item as well as its price

import time
numbers = ["1","2","3","4","4","5","6","7","8","9","0"]
symbols = ["`","~","!","@","$","%","^","&","*","(",")","_","+","=","/","{","}","|",":",",","<",">","?","'",'"',"[","]"," ","-"]
exitOrAdd = False
amountPaid = 0
       
#Symbolchecker - checks for symbols in an input
def symbol(word):
    for characters in word:
        if (characters in symbols)==True:
            return True
    return False

#Numberchecker - checks for numbers in an input
def number(word):
    for characters in word:
        if (characters in numbers)==True:
            return True
    return False

#Denomination amount - Tells you the amount of each bill/coin that needs to be given for change
def denominationAmounts():
    l = len(bills)
    print("\nHere is the change that is due by denomination:")
    for index in range(l):
        print("Number of "+str(bills[index])+": "+str(perBill[index]))
    return

#Decimal checker - checks for decimals in argument
def decimal(word):
    for characters in str(word):
        if (characters in ".")==True:
            return True
    return False

#Rounder - Makes sure that all monetary amounts have two decimal values to represent the cents.
def rounder(number):
    for characters in str(number):
        if (characters in ".")==True:
            decimals = len(str(number).split(".",1)[1])
            if decimals==1:
                return str(number)+"0"
            else:
                return number
    return number    
        
#Total - Adds the total amount
def total():
    totalPrice = 0
    for i in prices:
        totalPrice = totalPrice + float(i)
    taxes = round(totalPrice*0.13,2)
    print("Taxes: $"+str(rounder(float(taxes))))
    totalPrice = str(rounder(round(totalPrice+taxes,2)))
    if cash != True:
        print("\nTotal amount: $"+str(totalPrice)+"\n")
    else: 
        if totalPrice[-1]=="0":
            print("\nTotal amount: $"+str(totalPrice)+"\n")
        elif totalPrice[-1]=="1" or totalPrice[-1]=="2":
            totalPrice = rounder(round(float(totalPrice[:-1]+"0"),2))
            print("\nRounded total amount: $"+str(totalPrice)+"\n")
        elif totalPrice[-1]=="4" or totalPrice[-1]=="3" or totalPrice[-1]=="6" or totalPrice[-1]=="7":
            totalPrice = rounder(round(float(totalPrice[:-1]+"5"),2))
            print("\nRounded total amount: $"+str(totalPrice)+"\n")
        elif totalPrice[-1]=="8" or totalPrice[-1]=="9":
            totalPrice = totalPrice[:-1]+"0"
            totalPrice = round(float(totalPrice),2)
            totalPrice = rounder(round(totalPrice+0.10,2))
            print("\nRounded total amount: $"+str(totalPrice)+"\n")
        else:
            print("\nTotal amount: $"+str(totalPrice)+"\n")
    return 

#itemPrinter - prints items with their respective pricesat the end of the program.
def itemPrinter():
    l = len(items)
    print("\nHere is your current reciept:")
    for index in range(l):
        number = index+1
        print(str(number)+". "+str(items[index])+": $"+str(rounder(prices[index])))
        #print(str(number)+". "+str(quantities[index])+" "+str(items[index])+": $"+str(prices[index]))
    total()
    return


print("Welcome to Shehraan's NoFrills!\n")

while True:
    if exitOrAdd != True:
        cash = False
        bills = []
        perBill = []
        result = False
        prices = []
        items = []
        quantities = []
        menu = False
        change = 0
        taxes = 0
    redo = "y"
    correct = "n"
    cash = False
    buyMethod = "r"
    
    while correct == "n" and exitOrAdd != True:
        item = input("Please enter the name of the item you would like to add to the cart: ")
        while symbol(item)==True or any(i.isalpha() for i in item)==True or number(item)==True:
            if symbol(item)==True:
                print("\nError, you entered a symbol which is an invalid input. Please only enter numbers.")
                item = input("Please enter the name of the item you would like to add to the cart: ")
            elif number(item)==True:
                print("\nError, you entered a number which is an invalid input. Please only enter the name of the item.")
                item = input("Please enter the name of the item you would like to add to the cart: ")
            elif any(i.isalpha() for i in item)==True:
                item = item[0].upper()+item[1:].lower()
                items.append(item)
                break
        price = input("Please enter the cost of "+item+" in dollars: ")
        while (symbol(price)==True or any(i.isalpha() for i in price)==True or number(price)==True) and menu !=True:
            if symbol(price)==True:
                print("\nError, you entered a symbol which is an invalid input. Please only enter a positive number.")
                price = input("Please enter the cost of "+item+" in dollars: ")
            elif any(i.isalpha() for i in price)==True:
                print("\nError, you entered a letter which is an invalid input. Please only enter a positive number.")
                price = input("Please enter the cost of "+item+" in dollars: ")
            elif number(price)==True:
                if float(price)<0:
                    print("\nError, you have entered a negative price which is not possible. Please enter a positive number.")
                    price = input("Please enter the cost of "+item+" in dollars: ")
                elif float(price)==0:
                    print("\nError, you have entered 0 which is not possible. Please enter the true cost.")
                    price = input("Please enter the cost of "+item+" in dollars: ")
                else:
                    prices.append(round(float(price),2))
                    correct = input("\nYou've entered: "+item+" at a cost of $"+str(rounder(price))+"\n\nIs this information correct?\nEnter 'y' if it is correct\nEnter 'n' if it is incorrect: ").lower()
                    while correct!="y" and correct!="n":
                        print("\nError, please enter one of the given options")
                        correct = input("\nYou've entered: "+item+" at a cost of $"+str(rounder(price))+"\n\nIs this information correct?\nEnter 'y' if it is correct\nEnter 'n' if it is incorrect: ").lower()
                    if correct=="n":
                        print("\nPlease try again\n")
                        del items[-1]
                        del prices[-1]
                        break
                    else:
                        if (str(items[-1][-1])) != "s" and (str(items[-1][-1])) != "y":
                            itemPlural = items[-1]+"s"
                        elif (str(items[-1][-1])) == "y":
                            itemPlural = items[-1][:-1]+"ies"
                        else:
                            itemPlural = items[-1]
                        quantity = input("How many "+str(itemPlural)+" would you like to buy?: ")  
                        while symbol(quantity)==True or any(i.isalpha() for i in quantity)==True or number(quantity)==True:
                            if symbol(quantity)==True:
                                print("\nError, you entered a symbol which is an invalid input. Please only enter a positive number.")
                                quantity = input("How many "+str(itemPlural)+" would you like to buy?: ")
                            elif any(i.isalpha() for i in quantity)==True:
                                print("\nError, you entered a letter which is an invalid input. Please only enter a positive number.")
                                quantity = input("How many "+str(itemPlural)+" would you like to buy?: ")
                            elif number(quantity)==True:
                                if float(quantity)<0:
                                    print("\nError, you have entered a negative price which is not possible. Please enter a positive number.")
                                    quantity = input("How many "+str(itemPlural)+" would you like to buy?: ")
                                elif float(quantity)==0:
                                    confirmation = input("\nYou have entered 0. Are you sure you would like to buy none of this item?\nEnter 'y' if you are sure. \nEnter 'n' if you would like to re-enter the quantity: ").lower()
                                    while confirmation!="n" and confirmation!="y":
                                        print("\nError, please enter one of the given options\n")
                                        confirmation = input("\nYou have entered 0. Are you sure you would like to buy none of this item?\nEnter 'y' if you are sure. \nEnter 'n' if you would like to re-enter the quantity: ").lower()
                                    if confirmation=="y":
                                        menu = True
                                        del items[-1]
                                        del prices[-1]
                                        break
                                    else:
                                        print("\nPlease try again\n")
                                        quantity = input("How many "+str(itemPlural)+" would you like to buy?: ")
                                elif float(quantity)%1!=0:
                                        print("\nError, you have entered a decimal number which is invalid. Please enter a whole number.")
                                        quantity = input("How many "+str(itemPlural)+" would you like to buy?: ") 
                                else:
                                    quantities.append(quantity)
                                    del items[-1]
                                    del prices[-1]
                                    for i in range(int(quantity)):
                                        items.append(item)
                                        prices.append(round(float(price),2))
                                    redo = "y"
                                    menu = True
                                    break
    menu = True
    while result == False or exitOrAdd == True:
        correct="y"
        checkout = "n"
        while menu == True:
            print("\nMain Menu:")
            choice = input("\nIf you would like to add more items to cart, please enter '1'\nIf you would like to delete items from cart, please enter '2' \nIf you would like to view your shopping cart, please enter '3' \nIf you would like to checkout, please enter '4' \nIf you would like to exit, please enter '5': ")
            while (symbol(choice)==True or any(i.isalpha() for i in choice)==True or number(choice)==True):
                if symbol(choice)==True:
                    print("Error, you entered a symbol which is an invalid input. Please only enter numbers.")
                    choice = input("\nIf you would like to add more items to cart, please enter '1'\nIf you would like to delete items from cart, please enter '2' \nIf you would like to view your shopping cart, please enter '3' \nIf you would like to checkout, please enter '4' \nIf you would like to exit, please enter '5': ")
                elif any(i.isalpha() for i in choice)==True:
                    print("Error, you entered a letter which is an invalid input. Please only enter numbers.")
                    choice = input("\nIf you would like to add more items to cart, please enter '1'\nIf you would like to delete items from cart, please enter '2' \nIf you would like to view your shopping cart, please enter '3' \nIf you would like to checkout, please enter '4' \nIf you would like to exit, please enter '5': ")
                elif number(choice)==True:
                    if choice == "1":
                        menu = False
                        break
                    elif choice == "2" and redo != "n":
                        itemPrinter()
                        remove = input("If you would like to remove an item from the list, please enter its number on the list: \nOtherwise enter 'n' if the list looks good and you would like to continue: ")
                        while symbol(remove)==True or any(i.isalpha() for i in remove)==True or number(remove)==True:
                            if symbol(remove)==True:
                                print("\nError, you entered a symbol which is an invalid input. Please only enter a positive number.")
                                remove = input("If you would like to remove an item from the list, please enter its number on the list: ")
                            elif any(i.isalpha() for i in remove)==True and remove.lower()!="n":
                                print("\nError, you entered a letter which is an invalid input. Please only enter a positive number.")
                                remove = input("If you would like to remove an item from the list, please enter its number on the list: ")
                            elif remove.lower()=="n":
                                break
                            elif number(remove)==True:
                                if float(remove)<0:
                                    print("\nError, you have entered a negative number which is not possible. Please enter a positive number.")
                                    remove = input("If you would like to remove an item from the list, please enter its number on the list: ")
                                elif float(remove)==0:
                                    print("\nError, you have entered 0 which is not possible. Please enter a real number on the list.")
                                    remove = input("If you would like to remove an item from the list, please enter its number on the list: ")
                                elif float(remove)%1!=0:
                                    print("\nError, you have entered a decimal number which is not possible. Please enter a whole number.")
                                    remove = input("If you would like to remove an item from the list, please enter its number on the list: ")
                                elif float(remove)>len(items):
                                    print("\nError, you have entered a number which is not on the list. Please enter a number that can be found there.")
                                    remove = input("If you would like to remove an item from the list, please enter its number on the list: ")
                                else:
                                    del items[int(remove)-1]
                                    del prices[int(remove)-1]
                                    print("\nThe selected item has been successfully removed from your cart\n")
                                    time.sleep(1)
                                    itemPrinter()
                                    remove = input("If you would like to remove another item from the list, please enter its number on the list: \nOtherwise enter 'n' if the list looks good and you would like to continue: ")
                        l = len(items)
                        if l == 0:
                            print("You now have no items in your cart. Please add more items to your cart or exit.")
                            redo = "n"
                        break
                    elif choice == "2":
                        print("You have no items in your cart to check. Please add more items to your cart or exit.")
                        break
                    elif choice == "3":
                        l = len(items)
                        itemPrinter()
                        input("Are you ready to continue? Enter any character to proceed: ")
                        break
                    elif choice == "4":
                        result = True
                        menu = False
                        checkout = "y"
                        break
                    elif choice == "5":
                        result = True
                        menu = False
                        exitOrAdd = False
                        correct = "n"
                        checkout = "y"
                        break
                    else:
                        print("Please only enter one of the given number options.")
                        choice = input("\nIf you would like to add more items to cart, please enter '1'\nIf you would like to delete items from cart, please enter '2' \nIf you would like to view your shopping cart, please enter '3' \nIf you would like to checkout, please enter '4' \nIf you would like to exit, please enter '5': ")
         
        if checkout != "y" and menu != True:
            item = input("\nPlease enter the name of the item you would like to add to the cart: ")
            while (symbol(item)==True or any(i.isalpha() for i in item)==True or number(item)==True) and result == False:
                if symbol(item)==True:
                    print("\nError, you entered a symbol which is an invalid input. Please only enter the name of your item.")
                    item = input("\nPlease enter the name of the item you would like to add to the cart: ")
                elif number(item)==True:
                    print("\nError, you entered a number which is an invalid input. Please only enter the name of your item.")
                    item = input("\nPlease enter the name of the item you would like to add to the cart: ")
                elif any(i.isalpha() for i in item)==True:
                    item = item[0].upper()+item[1:].lower()
                    items.append(item)
                    break

            price = input("Please enter the cost of "+item+" in dollars: ")
            while (symbol(price)==True or any(i.isalpha() for i in price)==True or number(price)==True) and menu!=True:
                if symbol(price)==True:
                    print("\nError, you entered a symbol which is an invalid input. Please only enter a positive number.")
                    price = input("Please enter the cost of "+item+" in dollars: ")
                elif any(i.isalpha() for i in price)==True:
                    print("\nError, you entered a letter which is an invalid input. Please only enter a positive number.")
                    price = input("Please enter the cost of "+item+" in dollars: ")
                elif number(price)==True:
                    if float(price)<0:
                        print("\nError, you have entered a negative price which is not possible. Please enter a positive number.")
                        price = input("Please enter the cost of "+item+" in dollars: ")
                    elif float(price)==0:
                        print("\nError, you have entered 0 which is not possible. Please enter the true cost.")
                        price = input("Please enter the cost of "+item+" in dollars: ")
                    else:
                        prices.append(round(float(price),2))
                        correct = input("\nYou've entered: "+item+" at a cost of $"+str(rounder(price))+"\n\nIs this information correct?\nEnter 'y' if it is correct\nEnter 'n' if it is incorrect: ").lower()
                        while correct!="y" and correct!="n":
                            print("\nError, please enter one of the given options")
                            correct = input("\nYou've entered: "+item+" at a cost of $"+str(rounder(price))+"\n\nIs this information correct?\nEnter 'y' if it is correct\nEnter 'n' if it is incorrect: ").lower()
                        if correct=="n":
                            print("\nPlease try again\n")
                            del items[-1]
                            del prices[-1]
                            break
                        else:
                            if (str(items[-1][-1])) != "s" and (str(items[-1][-1])) != "y":
                                itemPlural = items[-1]+"s"
                            elif (str(items[-1][-1])) == "y":
                                itemPlural = items[-1][:-1]+"ies"
                            else:
                                itemPlural = items[-1]
                            quantity = input("How many "+str(itemPlural)+" would you like to buy?: ") 
                            while symbol(quantity)==True or any(i.isalpha() for i in quantity)==True or number(quantity)==True:
                                if symbol(quantity)==True:
                                    print("\nError, you entered a symbol which is an invalid input. Please only enter a positive number.")
                                    quantity = input("How many "+str(itemPlural)+" would you like to buy?: ")
                                elif any(i.isalpha() for i in quantity)==True:
                                    print("\nError, you entered a letter which is an invalid input. Please only enter a positive number.")
                                    quantity = input("How many "+str(itemPlural)+" would you like to buy?: ")
                                elif number(quantity)==True:
                                    if float(quantity)<0:
                                        print("\nError, you have entered a negative price which is not possible. Please enter a positive number.")
                                        quantity = input("How many "+str(itemPlural)+" would you like to buy?: ")
                                    elif float(quantity)==0:
                                        confirmation = input("\nYou have entered 0. Are you sure you would like to buy none of this item?\nEnter 'y' if you are sure. \nEnter 'n' if you would like to re-enter the quantity: ").lower()
                                        while confirmation!="n" and confirmation!="y":
                                            print("\nError, please enter one of the given options\n")
                                            confirmation = input("\nYou have entered 0. Are you sure you would like to buy none of this item?\nEnter 'y' if you are sure. \nEnter 'n' if you would like to re-enter the quantity: ").lower()
                                        if confirmation=="y":
                                            menu = True
                                            break
                                        else:
                                            print("\nPlease try again\n")
                                            quantity = input("How many "+str(itemPlural)+" would you like to buy?: ")
                                    elif float(quantity)%1!=0:
                                        print("\nError, you have entered a decimal number which is invalid. Please enter a whole number.")
                                        quantity = input("How many "+str(itemPlural)+" would you like to buy?: ")                                        
                                    else:
                                        quantities.append(quantity)
                                        del items[-1]
                                        del prices[-1]
                                        for i in range(int(quantity)):
                                            items.append(item)
                                            prices.append(round(float(price),2))
                                        redo = "y"
                                        menu = True
                                        break
                                
    exitOrAdd = False  
    #Process - Processes user's selected buying method and calculates the numbers  
    while correct!="n":
        if buyMethod != "B":
            buyMethod = input("\nDo you want to check out with cash or with card?\nEnter 'A' to check out with cash\nEnter 'B' to check out with card: ").upper() 
        while buyMethod!="A" and buyMethod!="B":
            print("\nError, please enter one of the given options\n")
            buyMethod = input("\nDo you want to check out with cash or with card?\nEnter 'A' for cash\nEnter 'B' for card: ").upper()
        #Output - Gives the user their reciept and then calls for the next customer
        if buyMethod=="B":
            cash = False
            itemPrinter()
            time.sleep(3)
            print("Your card was accepted!")
            break
        else:
            cash = True
            retry = 0
            itemPrinter()
            amountPaid = input("Please enter the total amount paid (please only enter the exact number amount): ")
            while (symbol(amountPaid)==True or any(i.isalpha() for i in amountPaid)==True or number(amountPaid)==True) and correct!="n":
                if symbol(amountPaid)==True:
                    print("\nError, you entered a symbol which is an invalid input. Please only enter a positive number.")
                    amountPaid = input("Please enter the total amount paid (please only enter the exact number amount): ")
                elif any(i.isalpha() for i in amountPaid)==True:
                    print("\nError, you entered a letter which is an invalid input. Please only enter a positive number.")
                    amountPaid = input("Please enter the total amount paid (please only enter the exact number amount): ")
                elif number(amountPaid)==True:
                    totalPrice = 0
                    for i in prices:
                        totalPrice = totalPrice + float(i)
                    taxes = round(totalPrice*0.13,2)
                    totalPrice = str(round(totalPrice+taxes,2))
                    totalPrice = float(totalPrice)
                    if float(amountPaid)<0:
                        print("\nError, you have entered a negative amount which is not possible. Please enter a positive number.")
                        amountPaid = input("Please enter the total amount paid (please only enter the exact number amount): ")
                    elif float(amountPaid)==0:
                        print("\nError, you have entered $0 which is not enough to pay off your items.")
                        retry = input("If you would like to switch to paying with card, please enter 'A'. \nOtherwise, if you would like to try entering the amount paid again, enter 'B': ").upper()
                        while retry!="A" and retry!="B":
                            print("\nError, please enter one of the given options\n")
                            retry = input("If you would like to switch to paying with card, please enter 'A'. \nOtherwise, if you would like to try entering the amount paid again, enter 'B': ").upper()
                        if retry=="A":
                            buyMethod="B"
                            break
                        else:
                            amountPaid = input("Please enter the total amount paid (please only enter the exact number amount): ")
                          
                    elif float(amountPaid)<totalPrice:
                        print("The amount paid is less than the total price of your items. Please pay the full amount or remove some items.\n")
                        retry = input("If you would like to switch to paying with card, please enter 'A'. \nIf you would like to remove an item from your cart, please enter 'B'. \nOtherwise, if you would like to try entering the amount paid again, enter 'C': ").upper()
                        while retry!="A" and retry!="B" and retry!="C":
                            print("\nError, please enter one of the given options\n")
                            retry = input("If you would like to switch to paying with card, please enter 'A'. \nIf you would like to remove an item from your cart, please enter 'B'. \nOtherwise, if you would like to try entering the amount paid again, enter 'C': ").upper()
                        if retry=="A":
                            buyMethod="B"
                            break
                        elif retry == "C":
                            amountPaid = input("Please enter the total amount paid (please only enter the exact number amount): ")
                        elif retry == "B":
                            itemPrinter()
                            remove = input("If you would like to remove an item from the list, please enter its number on the list: \nOtherwise enter 'n' if the list looks good and you would like to continue: ")
                            while symbol(remove)==True or any(i.isalpha() for i in remove)==True or number(remove)==True:
                                if symbol(remove)==True:
                                    print("\nError, you entered a symbol which is an invalid input. Please only enter a positive number.")
                                    remove = input("If you would like to remove an item from the list, please enter its number on the list: ")
                                elif any(i.isalpha() for i in remove)==True and remove.lower()!="n" and remove.lower()=="N":
                                    print("\nError, you entered a letter which is an invalid input. Please only enter a positive number or 'n'.")
                                    remove = input("If you would like to remove an item from the list, please enter its number on the list: ")
                                elif remove.lower()=="n" or remove.lower()=="N":
                                    break
                                elif number(remove)==True:
                                    if float(remove)<0:
                                        print("\nError, you have entered a negative number which is not possible. Please enter a positive number.")
                                        remove = input("If you would like to remove an item from the list, please enter its number on the list: ")
                                    elif float(remove)==0:
                                        print("\nError, you have entered 0 which is not possible. Please enter a real number on the list.")
                                        remove = input("If you would like to remove an item from the list, please enter its number on the list: ")
                                    elif float(remove)%1!=0:
                                        print("\nError, you have entered a decimal number which is not possible. Please enter a whole number.")
                                        remove = input("If you would like to remove an item from the list, please enter its number on the list: ")
                                    elif float(remove)>len(items):
                                        print("\nError, you have entered a number which is not on the list. Please enter a number that can be found there.")
                                        remove = input("If you would like to remove an item from the list, please enter its number on the list: ")
                                    else:
                                        del items[int(remove)-1]
                                        del prices[int(remove)-1]
                                        break
                            if len(items) == 0:
                                print("You now have no items in your cart. Please add more items to your cart or exit.")
                                exitOrAdd = True
                                correct = "n"
                                time.sleep(3)
                                break
                        if float(amountPaid)<totalPrice:
                            
                            print("\nThe total cost is still more than the amount paid. Please remove more items, or pay the full amount.")

                    elif float(amountPaid)==totalPrice:
                        print("Change: None\nThank you for paying in exact change!")
                        correct="n"
                        break
                    else:
                        change = float(amountPaid) - totalPrice
                        finalChange = str(round(change,2))
                        if change//100>=1:
                            hundreds = change//100
                            perBill.append(int(hundreds))
                            bills.append("$100 bills")
                            change = change%100
                        if change//50>=1:
                            fifties = change//50
                            perBill.append(int(fifties))
                            bills.append("$50 bills")
                        change = change%50
                        if change//20>=1:
                            twenties = change//20
                            perBill.append(int(twenties))
                            bills.append("$20 bills")
                        change = change%20
                        if change//10>=1:
                            tens = change//10
                            perBill.append(int(tens))
                            bills.append("$10 bills")
                        change = change%10
                        if change//5>=1:
                            fifties = change//5
                            perBill.append(int(fifties))
                            bills.append("$5 bills")
                        change = change%5
                        if change//2>=1:
                            toonies = change//2
                            perBill.append(int(toonies))
                            bills.append("toonies")
                        change = change%2
                        if change//1>=1:
                            loonies = change//1
                            perBill.append(int(loonies))
                            bills.append("loonies")
                        change = change%1
                        if change//0.25>=1:
                            quarters = change//0.25
                            perBill.append(int(quarters))
                            bills.append("quarters")
                        change = change%0.25
                        if change//0.10>=1:
                            dimes = change//0.10
                            perBill.append(int(dimes))
                            bills.append("dimes")
                        change = change%0.10
                        if change//0.05>=1:
                            nickels = change//0.05
                            perBill.append(int(nickels))
                            bills.append("nickels")
                        change = change%0.05
                        if change>=0:
                            if change<=0.02:
                                change = 0
                            else:
                                change = 0.05
                                #Checks if bill has already been inputted
                                if bills[-1]!="nickels":
                                    nickels = change//0.05
                                    perBill.append(int(nickels))
                                    bills.append("nickels")
                                else:
                                    perBill[-1] = perBill[-1] + 1
                        itemPrinter()
                        if finalChange != "0.01" and finalChange != "0.02":
                            print("Total change: $"+rounder(finalChange))
                            denominationAmounts()
                        elif finalChange == "0.01":
                            print("You paid an extra penny above the price. Please take your penny back.")
                            time.sleep(3)
                        elif finalChange == "0.02":
                            print("You paid two extra pennies above the price. Please take your pennies back.")
                            time.sleep(3)
                        correct="n"
                        break
    if exitOrAdd!=True:
        print("\nThanks for using this program to handle your shopping needs! Have a great day!")
        time.sleep(4)
        print("\nNext customer please!\n")
        time.sleep(5)