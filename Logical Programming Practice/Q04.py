code = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    }
decode = {'.-':"A", '-...':'B',
                    '-.-.':'C', '-..':"D", '.':'E',
                    '..-.':'F', '--.':'G', '....':'H',
                    '..':'I', '.---':'J', '-.-':'K',
                    '.-..':'L', '--':'M', '-.':'N',
                    '---':'O', '.--.':'P', '--.-':'Q',
                    '.-.':'R', '...':'S', '-':'T',
                    '..-':'U', '...-':'V', '.--':'W',
                    '-..-':'X', '-.--':'Y', '--..':"Z"
                    }

def encryption(encrypt):
    encrypt = encrypt.upper()
    encrypted = ""
    for i in encrypt:
        encrypted += code[i]
    return encrypted
def decryption(decrypt):
    for i in decrypt.split(' '):
        return [decode.get(i) for i in decrypt.split(' ')]
        
Q=input("Do u want to encrypt or decrypt : ")
Q=Q.lower()
if Q=='encrypt':
    text=input("Enter message to be encrypted : ")
    morse= encryption(text)
    print(morse)
elif Q=='decrypt':
    text=input("Enter message to be decrypted : ")
    morse= decryption(text)
    print(morse)
else:
    print('ERROR OCCURED')