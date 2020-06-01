cp=int(input("Enter the cost Price\n"))
sp=int(input("Enter the selling price\n"))
profit=sp-cp

profit_5 = profit + (profit*5)/100 +cp

print("Profit from this cell:",profit,"\nSelling price after increase 5% profit:",profit_5)
