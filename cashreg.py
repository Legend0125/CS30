#######################################################
# JANREI
# Computer Science 30
# sept. 16, 2024
#
#Write a "cash register" program. Have the user input the price of a product, and the quantity of
#that product. Display a running total at all times. When the user enters a price of zero, that will
#indicate that there are no more items. When all items are entered, display the sub-total,
#calculate and display taxes, and then display the total. Have the
#user enter the amount of cash tendered, and display the amount of change to be returned. Then
#have the computer calculate the number of $20, $10, $5, $1 bills and quarters,
#dimes, nickels, and pennies to be returned as change.
# calculate tax
# display total
# ask for cash
# make sure cash is > total
# calculate change
#######################################################
import os

items = ["hat", "Jordans", "chrome hearts chain", 'cargo pants'] # list of items
prices = [35.00, 400.37, 799.99, 26.75] # list of prices
quantities = [0] * len(items) # list to store quantities of each item

tax = int(input("Enter the tax rate (in percentage): "))

sub_total = 0 # initialize subtotal to 0

print("Menu:")  # display menu items and their prices in the terminal
for i, (item, price) in enumerate(zip(items, prices), start=1): # display menu
    print(f"{i}. {item} - ${price}") # display prices in the terminal

while True: # loop until user enters a price of 0
    item = str(input("Enter the item # (0 to stop): "))
    if item not in [str(i) for i in range(len(items) + 1)]:
        print("Invalid choice. Please enter a valid item number.")
    elif item == "0":
        break
    else:
        item_index = int(item) - 1
        price = prices[item_index]
        amnt = int(input("Enter the quantity of the item: "))
        quantities[item_index] += amnt
        sub_total += price * amnt
        os.system('cls' if os.name == 'nt' else 'clear') # clear terminal
        print("Menu:")  # display menu items and their prices in the terminal
        for i, (item, price) in enumerate(zip(items, prices), start=1): # display menu
            print(f"{i}. {item} - ${price}") # display prices in the terminal
        print(f'Your total so far is ${sub_total}')

print("Items and their quantities:")  # display items and their quantities
for i, (item, price, quantity) in enumerate(zip(items, prices, quantities), start=1):
    print(f"Item: {item}, Price: ${price}, Quantity: {quantity}")

taxes = (sub_total * tax / 100)
total = sub_total + taxes # calculate total with tax

print(f'Your taxes are ${taxes}')
print(f'Your total is ${total}')

cash_tendered = float(input("Enter the amount of cash tendered: "))

while cash_tendered < total:
    print("If you're broke just say so. Please enter more cash.")
    cash_tendered = float(input("Enter the amount of cash tendered: "))

change = cash_tendered - total

change = round(change, 2)

print(f'Your change is ${change}')

# calculate change in $20, $10, $5, $1, quarters, dimes, nickels, and pennies
change_in_cents = int(change * 100)

bills = {2000: 0, 1000: 0, 500: 0, 100: 0, 25: 0, 10: 0, 5: 0, 1: 0} # convert change to cents

for bill in sorted(bills.keys(), reverse=True): # sort by bill
    bills[bill] = change_in_cents // bill 
    change_in_cents %= bill
    if bills[bill] > 0:
        print(f"{bills[bill]} x ${bill/100}")
        if bill == 2000:
            print("twenties")
        elif bill == 1000:
            print("tens")
        elif bill == 500:
            print("fives")
        elif bill == 100:
            print("ones")
        elif bill == 25:
            print("quarters")
        elif bill == 10:
            print("dimes")
        elif bill == 5:
            print("nickels")
        elif bill == 1:
            print("pennies")