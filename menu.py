#Yiming Zhong
#outputs a simple menu for user to choose
#tests user input and if statements

food = ["Sandwich", "Fondue", "Dango", "Curry"]
print (food)
print ("Welcome Annie! What would you like to eat today?")
n = input("Please choose from above list : ")
if n == "Sandwich":
    print ("To make a sandwich, use two breads and preferred fillings.")
elif n == "Fondue":
    print ("Unfortunately, Fondue cannot be located at the moment.")
elif n == "Dango":
    print ("Chocolate dangos are the only ones available at the moment.")
    dango = input("Would you like one? ")
    if dango == "yes" or dango == "Yes":
        print ("This is not the real Annie.")
    elif dango == "no" or dango == "No":
        print ("I thought so.")
    else:
        print ("Please answer the question properly.")
elif n == "Curry":
    print ("There are some restaurants near you which offer choice curry.")
    print ("Please locate them on Google Maps.")
else:
    print ("Please give a valid answer in proper spacing and capitalization.")
print ("Have a nice day!")
