name = input("What is your name? ") # Get name.
adj1 = input("Enter an adjective:") # get first descriptor
adj2 = input("Enter an adjective:") # get second descriptor
adj3 = input("Enter an adjective:") # get third descriptor

# setting ititial variables
oldstring = "%s is the %s!" % (name, adj1)
addstring = "Hey! Hey! Hey! Hey!"

# declare variable newstring initialize
newstring1 = oldstring.replace(adj1,adj2)
newstring2 = newstring1.replace(adj2, adj3)



#Validation
print (oldstring.upper())
print(newstring1.upper())
print(newstring2.upper())
print(addstring.upper())




