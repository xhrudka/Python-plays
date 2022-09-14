# A list contains a list
menus={"Breakfast":["Egg", "Bagel", "Coffee"],"Lunch":["Burger", "Pizza", "Steak"], "Dinner":["salat", "soup","wine"]}

for name, menu in menus.items():
    print(name, ":", menu)
