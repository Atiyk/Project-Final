import random
import array
def status(pw_length , user_choice): 
    pass_length = int(pw_length)
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',   '*', '(', ')', '<']
    Combined_list=LOCASE_CHARACTERS+UPCASE_CHARACTERS+SYMBOLS+DIGITS
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)
    password = ""
    password = password.join(random.sample(Combined_list, pass_length))
    # encryption stuff
    decrypted = b"abcdefghijklmnopqrstuvwxyz"
    encrypted = b"qwertyuiopasdfghjklzxcvbnm"
    encrypt_table = bytes.maketrans(decrypted, encrypted)
    decrypt_table= bytes.maketrans(encrypted, decrypted)
    encrypt = password.translate(encrypt_table)
    decrypt = password.translate(decrypt_table)
    if user_choice == "1" :
        return "The generated encrypted password is " + encrypt
    elif user_choice == "2" :
        return "The generated decrypted password is " + decrypt
    else: 
        return "Error, choose either 1 or 2"

