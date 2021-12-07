from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
run_again = True
while run_again is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        shift_amount %= 25
        for char in start_text:
            if char in alphabet:
                ini_pos = alphabet.index(char)
                if cipher_direction == "encode":
                    enc_pos = ini_pos + shift_amount
                    if enc_pos > 25:
                        enc_pos -= 26
                    end_text += alphabet[enc_pos]
                elif cipher_direction == "decode":
                    dec_pos = ini_pos - shift_amount
                    if dec_pos < 0:
                        dec_pos += 26
                    end_text += alphabet[dec_pos]
                else:
                    end_text = "You have entered the wrong command"
            else:
                end_text += char
        if cipher_direction == "encode":
            print(f"The encoded text is '{end_text}'")
        elif cipher_direction == "decode":
            print(f"The decoded text is '{end_text}'")
        else:
            print(end_text)





    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    prompt = input("Do you want to run again?\nYes or No\n").lower()
    if prompt == "yes":
        run_again =True
    elif prompt == "no":
        print("Program has ended.")
        run_again = False





