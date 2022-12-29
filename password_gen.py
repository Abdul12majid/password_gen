# characters to get password from
import string
import random

digits = list(string.digits)
alphabets = list(string.ascii_letters)
spec_char = list("@#$&*%+£")
character = list(digits + alphabets + spec_char)

def psswrd():
    
    length = int(input("input length of password: "))
    digits_count = int(input("No of digits: "))
    alpha_count = int(input("No of alphabets: "))
    spec_char_count = int(input("No of special characters: "))
    char_count = digits_count + alpha_count + spec_char_count
    
    
    if char_count > length:
        print("Character greater than length")
        return
        
    password = []
    
    
    for i in range(digits_count):
        random.shuffle(digits)
        password.append(random.choice(digits))
    for i in range(alpha_count):
        random.shuffle(alphabets)
        password.append(random.choice(alphabets))
    for i in range(spec_char_count):
        random.shuffle(spec_char)
        password.append(random.choice(spec_char))
        
        
    if char_count < length:
        for i in range(length - char_count):
            random.shuffle(character)
            password.append(random.choice(character))
            
    random.shuffle(password)
    
    print("".join(password))
    

psswrd()