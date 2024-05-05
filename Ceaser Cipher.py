alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


should_continue = True
def encrypt(plain_text, shift_ammount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_ammount
        if new_position > 25:
            new_letters = alphabet[new_position % 26]
        else:
            new_letters = alphabet[new_position]
        cipher_text += new_letters
    print(f"The encoded text is {cipher_text}")
def decrypt (new_text, new_shift):
    original_text = ""
    for letter in new_text:
        positions = alphabet.index(letter)
        new_positions = positions - new_shift
        if new_positions < 0:
            new_letter = alphabet [new_positions % 26]
        else:
            new_letter = alphabet[new_positions]
        original_text += new_letter
    print(f"The decoded text is {original_text}")



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == "encode":
    encrypt(plain_text=text, shift_ammount=shift)
elif direction == "decode":
    decrypt(new_text=text, new_shift=shift)
