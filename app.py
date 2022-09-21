#####################################################
# Ceasars Cipher Using Python
#####################################################

# step 1 - create list of alphabet

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
print('\n\n******************************************') 
print('Welcome to the Python Ceaser\'s Cipher:')
print('******************************************\n\n') 

def cipher_info():    
    # step 2 - take in direction to encode or decode
    # use .lower() to account for capitalisation mismatches
    user_msg = input("\nEnter your message to encode/decode:\n").lower()

    # step 3 - take in encode/decode and shift argument
    enc_dec = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    shift_arg = int(input("Type the shift number:\n"))
    return user_msg,enc_dec,shift_arg

# create cipher function
def cipher(text,enc,alph,shift):

    # check if function should encode or decode
    # if encode shift remains positive, if negative then shift becomes negative
    if enc == 'decode':
        shift = -shift
    
    new_message = []
    
    # change index and find new character
    for character in text:
        # can use index as each entry in alhabet list is unique
        # not encounter any errors by only finding the first character
        old_index = alphabet.index(character)
        new_index = old_index + shift
        # account for index > alpahbet list index
        if new_index > 25:
            new_index = new_index%26
                 
            
        new_message.append(alph[new_index])
        
    # return new message
    return "Your new message is: " + "".join(new_message)    



    
# create loop so user can encode or decode 
# multiple values before the program quits
while True:
    user_msg,enc_dec,shift_arg = cipher_info()
    message = cipher(text=user_msg,enc=enc_dec,alph=alphabet,shift=shift_arg)
    print('\n')
    print(message)
    repeat = input("\n\nWould you like to encode another message?\nY for Yes N for No:\n").upper()
    if repeat == 'N':
        break