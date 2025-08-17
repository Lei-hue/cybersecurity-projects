import random
import string
import pyperclip

while True:
    while True:
        try:
            password_length = int(input("What is your desired password length? ").strip())
            if password_length < 4:
                print ("Minimum password length is 4")
            else:
                break
        except ValueError:
            print ("Numerics Only: ")
            
    char_pool = ""

    password_upper = input("Include Uppercase? y/n " ).strip() .lower()
    if password_upper == "y":
        char_pool += string.ascii_uppercase
            
    password_lower = input("Include Lowercase? y/n " ).strip() .lower()
    if password_lower == "y":
        char_pool += string.ascii_lowercase
        
    password_numeric = input("Include Numerics? y/n " ).strip() .lower()
    if password_numeric == "y":
        char_pool += string.digits

    password_special = input("Include Special Characters? y/n " ).strip() .lower()
    if password_special == "y":
        char_pool += string.punctuation
        
    if not char_pool:
        print("At least one selection must be made... ")
        continue
        
    password = ''.join(random.choices(char_pool, k=password_length))
    print ("Your Requested Password is: ", password)
    
    print ("\nGenerated Password: ", password)
    print ("-" * 30)
    
    pyperclip.copy(password)
    print ("Password copied to clipboard! ")

    regenerate = input("Would you like to generate another password? y/n ").strip() .lower()
    if regenerate != "y":
        print ("Thank you & Stay Safe!")
        break
    
    
    
