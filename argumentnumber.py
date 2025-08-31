def order_food(min_order, *args):

    print(f"You have ordered: {min_order}")
    #print(args)
    for items in args:
        print(f"You have Ordered: {args}")
    print("Your junks will be delivered in 30 minutes")
    print("Enjoy the party")
order_food("salad","bear", "Pizza", "soup")
