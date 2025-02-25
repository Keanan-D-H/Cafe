#***cafe***
# Keanan Hinchliffe
# A program to add up the total stock value for a cafe. 


# Function Definitions

def check_yes_no(answer):
    """
    check_yes_no function checks whether an input is either 'yes' or 'no'
    The function will repeatedly ask for an input until it is either 'yes'
    or 'no'
    
    Parameter    :      
                 answer : str
                 
     Returns    : 
                 answer : str    
                     either 'yes' or 'no'
    """
    while answer !='yes' and answer != 'no':
        answer = input ('Please only put in \'yes\' or \'no\'    ')
    return answer


def check_number(item): 
    """
    check_number tries to turn 'item' to a float, if it can not
    it will ask for a new input until a number is inputted. 
    
    Parameter    :    
                    item : str

    Returns      :
                    item : float
    """
    while type(item) != float:
        try:
            item = float(item)
        except:  
            item = input("That is not a number, please input again.   ")
    return item


def check_repeat (item, dictionary):
    """
    check_repeat function checks if the user has inputted a value previously
    if they have, the program will ask them if they want to overwrite the
    previously input data. 

    Parameters    : 
                    item : str    
                    dictionary : dict

    Returns        :
                    repeat : str
                        "yes" if a the user wishes to overwrite or "no" if they don't
                    "no repeat" : str
                        if item is not found in dictionary
    """
    if dictionary.get(item) != None:
        repeat = input(f"""Unfortunately, {item} is already in our recorded 
list.If we carry on with this item our previous record
will be overwritten. Would you like to carry on?    """)
        check_yes_no(repeat)
        
        return repeat
    else:
        return "no repeat"
    

# Variable Declarations
menu = []
stock = {}
price = {}
total_stock = 0

#asking the user if they want to input data
finished = input("\nDo you have any menu items to input?    ")
finished = check_yes_no(finished)

# While there are still menu items to be inputted, ask for the item name
# price and how much the user has in stock
while finished == "yes":
    # ask for the name of the stock item
    menu_entry = input("\nWhat is the name of the menu item?    ")
    menu_entry_check = check_repeat(menu_entry.lower(),stock)

    # If the user has repeated a stock item name and does not want to
    # overwrite the data then move on to next iteration.
    if menu_entry_check == 'no':
        finished = input("\nDo you have more menu items to input?    ")
        finished = check_yes_no(finished)
        continue

    # If the user wants to overwrite previous data the stock_amount *
    # price_input from data with the same name is removed from total_stock.
    elif menu_entry_check == "yes":
        total_stock -= stock.get(menu_entry) * stock.get(menu_entry)


    stock_amount = input("\nHow much do you have in stock:    ")
    stock_amount = check_number(stock_amount)

    price_input = input("\nHow much does it cost? (£)     ")
    price_input = check_number(price_input)

    # Add menu_entry to menu, {menu_entry:stock_amount} to stock and 
    # {menu_entry, price_input}
    menu.append(menu_entry.lower())
    stock[menu_entry] = stock_amount
    price[menu_entry] = price_input
    total_stock  += stock_amount * price_input

    finished = input("\n\nDo you have more menu items to input?    ")
    finished = check_yes_no(finished)


if len(stock) != 0 :
    # If stock has been inputted by the user present the inputted items 
    # to the user as a table.

    print()
    print('{:^20}|{:^20}|{:^20}'.format("Item name", "Quantity", "Cost (£)"))  
    dashes = '-' * 62                                        
    print(dashes)

    for key in stock:
        # For each menu item print the items name, stock quantity and cost.
        print('{:^20}|{:^20}|{:^20}'.format(key, stock[key], price[key]))

    print(f"\nThe total stock value is £{"%.2f" % total_stock}.")


print("\n\nGoodbye!")


