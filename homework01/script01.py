# Script 1: Find and print the 5 longest words in the words file.

#initializing the words and largest5 list
words = []
largest5 = []

#store the elements in the words file into the words list
with open('/usr/share/dict/words', 'r') as infile:
        words = infile.read().splitlines()

#loop 5 times to find 5 words
for x in range(5):
        #initialize the largest and lengthOfWord with the first element
        largest = words[0]
        lengthOfWord = len(words[0])

        #sort through the words list
        for i in range(len(words)):
                #if the next word is longer than the previous word, keep it
                if (len(words[i]) > lengthOfWord):
                        largest = words[i]
                        lengthOfWord = len(words[i])

        #add the longest word to the largest5 list and remove it from the words list
        largest5.append(largest)
        words.remove(largest)

#sort the list in alphabetical order
largest5.sort(key=str.lower)

#print the longest words
for a in range(5):
        print(largest5[a])
