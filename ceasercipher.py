def encrypt_text(plaintext,key):
    ans = ""
    
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch==" ":
            ans+=" "
        elif (ch.isupper()):
            ans += chr((ord(ch) + key-65) % 26 + 65)
        else:
            ans += chr((ord(ch) + key-97) % 26 + 97)
    
    return ans


def decrypt(encrypted_message,key):
    ans = ""
    for i in range(len(encrypted_message)):
        ch = encrypted_message[i]
        if ch==" ":
            ans+=" "
        elif (ch.isupper()):
            ans += chr((ord(ch) - key-65) % 26 + 65)
        else:
            ans += chr((ord(ch) - key-97) % 26 + 97)
    
    return ans


a=input("Enter the letter 'e' for encrption or lettr 'd' for decryption:")
if a=='e':
    plaintext =input("Enter the plaintext for encryption:").strip()
    key=int(input("Enetr the key value to shift:"))
    print("Plain Text is : " + plaintext)
    print("Shift pattern is : " + str(key))
    print("Cipher Text is : " + encrypt_text(plaintext,key))
elif a=='d':
    encrypted_message = input("Enter the encrypted text for decryption:")
    letters="abcdefghijklmnopqrstuvwxyz"
    key= int(input("Enter the key to decrypt: "))
    print("Shift pattern is : " + str(key))
    print("decrypted text:"+decrypt(encrypted_message,key))
