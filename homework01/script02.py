# Script 2: printing five names that are exactly 8 characters long

#importing the names library
import names

#initializing a counter variable
counter = 0

#once the counter hits 5, stops the loop
while counter != 5:
    #pulls a random name
    name = names.get_full_name()

    #if the name is 8 characters long, then print and increase the counter
    if (len(name) == 9):
        print(name)
        counter = counter + 1;
