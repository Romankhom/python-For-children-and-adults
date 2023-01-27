#simple pizza cost calculator
#ask a man how much pizza he wants
# get number using function eval()
numberOfPizza = eval(input("Яку кількість піци ви бажаєте? "))
#acs cost of pizza in menu
costPerPizza = eval(input("Скільки коштує піца? "))
#calculate the total cost
subTotal = numberOfPizza * costPerPizza
#calculate tax 20%
taxRate = 0.2
salesTax = subTotal * taxRate
#tottal amount
totalAmount = subTotal + salesTax
print ("Загальна вартість замовлення $", totalAmount)
print ("В тому числі $", subTotal, "За піцу")
print ("$", salesTax, "податок на продаж")