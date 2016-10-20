__author__ = 'Evan FO'

#the charge for all desks is minimum $200
minimum = 200

#If a desk has a surface area of 750 square inches of above 
#than it is considered a large desk and the cost increases by $50
largeSurfaceSize = 750
largeSurfaceCost = 50

#If the desk is made of Mahogany than there is a $150 premium added
mahoganyCost = 150
#If it's Oak than there is a $125 premium added
oakCost = 125
#Pine is no additional cost
pineCost = 0

#If the customer wants drawers they are $30 each
drawerCost = 30


#input section
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
#for every drawer in the desk, there is an additional $30 charge
totalDrawerCost = drawers * drawerCost
total += totalDrawerCost


#output
#total cost
print("Total cost is : ${0:.2f}".format(total))