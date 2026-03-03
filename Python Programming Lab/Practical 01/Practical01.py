for i in range(1, 6):
    print("---------PROFIT & LOSS CALCULATION---------")
    print(f"Item:{i}")

    cost_price = float(input("Enter the cost price: "))
    selling_price = float(input("Enter the selling price: "))
    if selling_price>cost_price:
        profit = selling_price - cost_price
        print(f"Yayyyyyyyyy!!!!!!!!your profit is {profit}")
    elif cost_price >selling_price:
        loss = cost_price - selling_price
        print(f"OHHH NOOOOOO!!!! you are in loss & loss is {loss}")
    else:
        print("No profit,No loss")
