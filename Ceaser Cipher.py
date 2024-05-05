alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        for char in start_text:
            position = alphabet.index(char)
            new_position = position - shift_amount
            if new_position < 0:
                new_letter = alphabet [new_position % 26]
            else:
                new_letter = alphabet[new_position]
            end_text += new_letter
          
    else:
       for char in start_text:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position > 25:
                new_letter = alphabet [new_position % 26]
            else:
                new_letter = alphabet[new_position]
            end_text += new_letter
    print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)


should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))


  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    


