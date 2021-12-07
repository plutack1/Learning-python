
#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
with open("Input/Names/invited_names.txt") as names:
    all_names = names.readlines()
for index, name in enumerate(all_names):
    all_names[index] = name.strip("\n")
#Replace the [name] placeholder with the actual name.
for name in all_names:
    with open("Input/Letters/starting_letter.txt") as letter:
        letter_content = letter.read()
        letter_content = letter_content.replace("[name]", name)
#Save the letters in the folder "ReadyToSend".
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(letter_content)
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp