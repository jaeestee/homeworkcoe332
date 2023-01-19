# Script 2: printing five names that are exactly 8 characters long

import names

continueCode = True
index = 1

while continueCode:
    name = names.get_full_name()
    
    if (name.len() == 9):
        print(name)
        index++;
