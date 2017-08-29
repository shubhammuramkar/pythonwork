sandwich_orders = ["pastrami","hot","pastrami","tuna","pastrami"]
finish_order1 = []
print("'Pastrami' is out of reach ")
while sandwich_orders:
    if "pastrami" in sandwich_orders:
        sandwich_orders.remove("pastrami")
    else :
        sand = sandwich_orders.pop()
        finish_order1.append(sand)
        print("Your "+ sand + " sandwitch is making ")
for san in finish_order1:
    print("your " + san + " is ready ")
print("Thankyou")