print('''
 __        ___  __   __   ___  __      __     __        ___  __  
/  `  /\  |__  |__) /__` |__  |__)    /  ` | |__) |__| |__  |__) 
\__, /~~\ |___ |  \ .__/ |___ |  \    \__, | |    |  | |___ |  \ 
''')
def shifter(character , shifts ):
    if character == ' ':
        return character
    ascii_code = ord(character.upper()) # A is 65 and so on
    shifted = (ascii_code - 65 ) + shifts # it will give the ascii value
    mod = shifted % 26 # it will give the alphabet place
    final_value = mod + 65 # it will give the final ascii shifted value
    converted = chr(final_value) # Convert to alphabet
    return converted
def encrypter(string , shift):
    encrypted_string = ""
    for i in range(len(string)):
        string = list(string)
        encrypted_string = encrypted_string + shifter(string[i] , shift)
    encrypted_string = str(encrypted_string)
    return encrypted_string
choice = int(input("1. Encrypt\n2. Decrypt "))
string = input("Enter Text : \n ")
shift = int(input("Enter Shifts : \n"))
if choice == 1:
    print(encrypter(string, shift))
elif choice == 2:
    print(encrypter(string, -shift))
else:
    print("Invalid Input")



