from Crypto.Cipher import AES 
from Crypto.Util.Padding import pad, unpad 
import random
secretkey = random.randbytes(16)
iv = random.randbytes(16)
FLAG=b""
def encrypt(msg):
    padded = pad(msg, 16) 
    cipher = AES.new(secretkey, AES.MODE_CBC, iv)
    return cipher.encrypt(padded)

def try2decrypt(ciphertext):
    cipher = AES.new(secretkey, AES.MODE_CBC, iv)
    dec = cipher.decrypt(ciphertext)
    try:
        msg = unpad(dec, 16)
        return True 
    except:
        return False


def menu():
    print("1. Encrypt the message")
    print("2. Decrypt ciphertext")
    print("3. Check message")
    print("4. Exit")

def checkflag():
    global FLAG
    print("Enter your message (in hex)")
    try:
        flag = bytes.fromhex(input(">> ").strip())
    except:
        print("Invalid flag")
    if flag == FLAG:
        print("You have decrypt the message successfully")
        exit(0)
    else:
        print("Wrong. You're failed :). Try again next time.")
        exit(0)

def encrypted_flag():
    enc = encrypt(FLAG)
    print("The IV is :")
    print(iv.hex())
    print("The encrypt message is :")
    print(enc.hex())

def server_side():
    global FLAG
    while True:
        menu()
        cmd = int(input(">> "))
        if cmd == 1:
            print("Read your input: ",end='')
            FLAG = bytes(str(input()),'utf-8')
            encrypted_flag()
        elif cmd == 2:
            print("Enter ciphertext (in hex) with size is multiple of 16")
            ciphertext = input(">> ").strip()
            try:
                ciphertext = bytes.fromhex(ciphertext)
            except:
                print("invalid ciphertext")
                continue
            if len(ciphertext) % 16 != 0:
                print("Invalid length!")
                continue
            if try2decrypt(ciphertext):
                print("Message has been decrypted successfully!")
            else:
                print("Failed to decrypt message(invalid padding)")
        elif cmd == 4:
            print("Good Bye!")
            break
        elif cmd == 3:
            checkflag()
        else:
            print("Invalid command!")

server_side()