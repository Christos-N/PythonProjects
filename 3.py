prices = {"cucumber": 2,"tomato": 2.5,"carrot": 3.4,"lettuce": 6.5,"onion":3.2}
print("Prices of vegetables:",prices)
def shop():
    sum = 0
    basket = []
    item = input("Type the vegetable you wish to buy:")
    while item !="":
        if item == "cucumber" or item == "tomato" or item == "carrot" or item == "lettuce" or item == "onion":
            basket.append(item)
        else:
            print("Wrong input! We sell cucumbers, tomatos, carrots, lettuces and onions.")
        item=input("Type the vegetable you wish to buy or press enter to stop shopping:")
    for i in range(0,len(basket)):
        sum += prices[basket[-1]]
        del basket[-1]
    sum += 0.24*sum #sum after tax
    print("Cost:",round(sum, 2),"€")
shop()
