__author__ = 'w0174181'
#the charge for all desks is minimum $200
minimum = 200
largeSurfaceSize = 750
largeSurfaceCost = 50
mahoganyCost = 150
oakCost = 125
pineCost = 0
drawerCost = 30
#input
#Enter order number:
ordernumber = input("Enter order number: ")
#Enter length of desk (inches):
length = float(input("Enter length of desk (inches): "))
#Enter width of desk (inches):
width = float(input("Enter width of desk (inches): "))
#Enter type of wood (mahogany, oak, pine):
woodType = str(input("Enter type of wood (mahogany, oak, pine):"))
#Enter number of drawers:
drawers = int(input("Enter number of drawers: "))
#math time
#set total as minimum amount it will possibly be
total = minimum
surface = length * width
#if the surface (length * width) is over 750 square inches, add $50
if surface > largeSurfaceSize:
    total += largeSurfaceCost
#if the wood is "mahogany" add $150; for "oak" add $125. No charge is added for "pine"
if woodType.lower() == "mahogany":
    total += mahoganyCost

if woodType.lower() == "oak":
    total += oakCost

if woodType.lower() == "pine":
    total += pineCost
#for every drawer in the desk, ther is an additional $30 charge
totalDrawerCost = drawers * drawerCost
total += totalDrawerCost
#output
#total cost
print("Total cost is : ${0:.2f}".format(total))