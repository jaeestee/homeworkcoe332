# Script 3: Generates a list of 5 different names and contains a function that prints the length of each name.

#importing the names library
import names

#function to determine the length of the given name
def lenOfName(name):
    return(len(name) - 1)

#for loop to print 5 names and their corresponding lengths
for i in range(1, 6):
    name = names.get_full_name()
    print(f'Name {i}: {name}\nLength: {lenOfName(name)}')
