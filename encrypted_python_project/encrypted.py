from cryptography.fernet import Fernet as f

def get_key():

    n_or_o = input("(N)ew or (O)ld key").strip().lower()

    if n_or_o == "n":
        key = f.generate_key()
        print_key= key.decode("ASCII")
        print(print_key)
    elif n_or_o == "o":
        key= input("Paste Key: \n").encode("ASCII") 
    else:
        print("check entry")
        return None
    return key
    

def read(key):
    paste = input("Paste message: \n")
    paste = paste.encode("ASCII")
    paste = f(key).decrypt(paste)
    print(paste.decode("ASCII"))

def write(key):
    message = input("Enter message:\n")
    message = message.encode("ASCII")
    message = f(key).encrypt(message)
    print(message.decode("ASCII"))

def main():
    key = get_key()
    if key==None:
        return
    while True:
        R_W_Q=input("(R)ead or (W)rite or (Q)uit? \n").strip().lower()

        if R_W_Q == "r":
            read(key)
        elif R_W_Q =="w":
            write(key)
        elif R_W_Q== "q":
            break
        else:
            print("check entry")
    
main()
