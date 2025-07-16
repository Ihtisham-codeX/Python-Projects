Menu = {
    "espresso" : {
        "ingredients":{
            "water" : 50,
            "coffee": 18,
            "milk":0,
        },
        "cost" : 1.5,
    },
    "latte" : {
            "ingredients" : {
                "water" : 200,
                "coffee" : 150,
                "milk" :24,
            },
            "cost" : 2.5,
    },
    "cappuccino" : {
            "ingredients" : {
                "water" : 250,
                "coffee" : 100,
                "milk" :24,
            },
            "cost" : 3.0,
    },

}
Resources = {
    "water" : 300,
    "coffee": 200,
    "milk": 100,
    "money": 0,
}
# Conerting all the money in dollars
def Convert_To_Dollars(quarters , dimes , nickels , pennies):
    return (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

# Check if the entered amount is greater or equal to the price of coffee in menu
def Amount_Is_Sfficient(amount , coffee):
        return amount >= Menu[coffee]["cost"]

# Check if there are sufficient ingredients for that particular coffee in Resources
def Ingredients_Are_Sufficient(coffee):
    ingredients_required = Menu[coffee]["ingredients"]
    for item in ingredients_required:
        if ingredients_required[item] > Resources[item]:
            return False
    return True

# Showing The Stock Left
def Report():
    print("\n----Resources----\n")
    for item,amount in Resources.items():
        print( str(item) + " -> " + str(amount))

# Subtracting the ingredients from the resources to make the coffee
def Make_And_Serve_Coffee(amount,coffee):
    ingredients_required = Menu[coffee]["ingredients"]
    Resources["money"] =     Resources["money"] + Menu[coffee]["cost"]
    for item in ingredients_required:
        Resources[item] = Resources[item] - ingredients_required[item]
    if amount > 0:
        print(f"Here is your Change : {round(amount,2)} $")
    print(f"Here you go with your {coffee} --> ☕\n Enjoy 😊")

# Main
while True:

    order = str(input("What would you like cappuccino / latte / espresso : \n"))
    if order.lower() == "off" :
        exit()
    if order.lower() == "report":
        Report()
        continue
    print("Enter Your Amount")
    quarters = int(input("Quarter : "))
    dimes = int(input("Dimes : "))
    nickels = int(input("Nickels : "))
    pennies = int(input("Pennies : "))
    Amount_in_Dollars = Convert_To_Dollars(quarters, dimes, nickels, pennies)

    if Amount_Is_Sfficient(Amount_in_Dollars, order):
        change = Amount_in_Dollars -  Menu[order]["cost"]
        if Ingredients_Are_Sufficient(order):
            Make_And_Serve_Coffee(change , order)
        else:
            print("Ingredients Not Enough")
    else:
        print("Not Enough Amount")

