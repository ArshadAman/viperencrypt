from colorama import init
from termcolor import colored


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode" or cipher_direction == "d":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(colored(f"Here's the result: {end_text}", 'green'))
  print()

from art import logo,logo_text
print(colored(logo, 'green'))
print(colored(logo_text,'yellow'))
print()

should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
  print()
  if direction == 'e' or direction == 'encode' or direction == 'd' or direction == "decode":
    val = ""
    if direction == "e" or direction == "encode":
      val = "encrypt"
    else:
      val = "decrypt"
    text = input(f"Type your message to {val}: ").lower()
    print()
    key = int(input(f"Enter the Key (Please use minimum 4 digits and max of 6 digits):"))
    str_key = str(key)
    count = len(str_key)
    print()

    if count >= 4 and count <= 6:
      key = (key % 25) + 4
      caesar(start_text=text, shift_amount=key, cipher_direction=direction)

    else:
      print("Invalid Key Format!!!")
      print()
  else:
    print("Invalid Input!!! Bye Bye Crap 😡")
    print()

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no' : ")
  print()
  if restart == "no" or restart == "n":
    should_end = True
    print("Goodbye 😉")
    print()
    


