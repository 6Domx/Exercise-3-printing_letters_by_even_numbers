# Pseudocode
# 1. Ask the user to input any character
# 2. Evaluate the characters inputed by the user
# 3. Break the code if the number of characters is less than 2
# 4. Print the characters in an even index number pattern.


character_input = input("Please enter any character: ")
character_length = len(character_input)

print("Your word: ", character_input)
print("------------------------------")
print("Your new word: ")

for i in range(0, character_length -1, 2):
    print("Number {", i, "}:", character_input[i])