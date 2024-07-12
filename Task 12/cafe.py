#***cafe***

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
finished = input("Do you have any menu items to input?    ")
finished = check_yes_no(finished)

# While there are still menu items to be inputted, ask for the item name
# price and how much the user has in stock
while finished == "yes":
    # ask for the name of the stock item
    menu_item = input("What is the name of the menu item?    ")
    menu_item_check = check_repeat(menu_item,stock)

    # if the user has repeated a stock item name and does not want to
    # overwrite the data then move on to next iteration
    if menu_item_check == 'no':
        finished = input("Do you have more menu items to input?    ")
        finished = check_yes_no(finished)
        continue

    # if the user wants to overwrite previous data the stock_amount *
    # price_input from data with the same name is removed from total_stock
    elif menu_item_check == "yes":
        total_stock -= stock.get(menu_item) * stock.get(menu_item)


    stock_amount = input("How much do you have in stock:    ")
    stock_amount = check_number(stock_amount)

    price_input = input("How much does it cost (in £)?     ")
    price_input = check_number(price_input)

    #add menu_item to menu, {menu_item:stock_amount} to stock and {menu_item
    # , price_input}
    menu.append(menu_item)
    stock[menu_item] = stock_amount
    price[menu_item] = price_input
    total_stock  += stock_amount * price_input



    finished = input("Do you have more menu items to input?    ")
    finished = check_yes_no(finished)


print(stock)
print(price)
print(f"The total stock value is {total_stock}")




