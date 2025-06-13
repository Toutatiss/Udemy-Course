#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# Get a list of names
with open("/Users/felka/Documents/Python/Udemy Course/Section 24 - Improved Snake/Mail Merge Project Start/Input/Names/invited_names.txt", "r") as name_file:
    name_list = name_file.readlines()
    
# print(name_list)
    
# Clean up name list
for i in range(len(name_list)):
    name_list[i] = name_list[i].strip()

# print(name_list)

# Letter text
with open("/Users/felka/Documents/Python/Udemy Course/Section 24 - Improved Snake/Mail Merge Project Start/Input/Letters/starting_letter.txt","r") as letter_file:
    letter_contents = letter_file.read()
    for name in name_list:
        custom_letter_text = letter_contents.replace("[name]",name)
        with open(f"/Users/felka/Documents/Python/Udemy Course/Section 24 - Improved Snake/Mail Merge Project Start/Output/ReadyToSend/Letter for {name}", "w") as new_letter:
            new_letter.write(custom_letter_text)

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp - Return all lines in the file, as a list where each line is an item in the list object:
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp - The replace() method replaces a specified phrase with another specified phrase.
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp - Remove spaces at the beginning and at the end of the string: