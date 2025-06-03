from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

isRunning = True

while isRunning:
    direction = input("Type 'encode' to encrypt, or 'decode' to decrypt\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def en_or_decrypt(shift_direction, original_text, shift_amount):
        message = ""
        
        if shift_direction == "decode":
            shift_amount = shift_amount*-1
        
        for letter in original_text:
            if letter in alphabet:
                current_position = alphabet.index(letter)
                new_position = (current_position + shift_amount) % len(alphabet)
                message += alphabet[new_position]
            else:
                message += letter
        print(message)

    en_or_decrypt(direction, text, shift)
    
    continue_query = ""
    
    while continue_query != "y" and continue_query != "n":
        continue_query = input("Do you wish to continue? (y/n): ").lower()
        if continue_query == "n":
            isRunning = False
        elif continue_query != "y":
            print("Please enter a valid input.")
        

