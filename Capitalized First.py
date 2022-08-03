# Capitalized First
'''
Write a program with a function that accepts a string as an argument and
returns a newOutput of the string with the first character of each sentence
capitalized. The program should let the user enter a string and then pass
it to the function, printing out the modified string.
***example***
input: hello. my name is Joe. what is your name?
output:Hello. My name is Joe. What is your name? 
'''

getInput = input("Enter sentence to be capitalized: ")

newOutput = []
i = 0

for ch in getInput:

    if i != len(getInput)-1:
        if getInput[i] == '.' or getInput[i] == '?' or getInput[i] == '!':
            newOutput.append(getInput[i])
            newOutput.append(getInput[i+1])
            up = getInput[i+2].upper()
            newOutput.append(up)
            i += 3

        else:
            if i == 0:
               newOutput.append(getInput[i].upper())
            else:
                newOutput.append(getInput[i])
            i += 1
            
newOutput.append(getInput[i])

j=0
for len in newOutput:
    print(newOutput[j], end="")
    j+=1
