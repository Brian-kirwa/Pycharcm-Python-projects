#Banking program
def show_balance(balance):
    print(f"Your current balance is ${balance}")
def deposit(balance):
    amount=float(input("Enter amount to deposit: "))
    if amount<0:
        print("You cannot deposit less than Zero")
        return 0

    elif amount>balance:
        print(f"You have successfully deposited ${amount}")
        return amount
    else:
        print("Invalid value")
        return 0



def withdraw():
    amount=float(input("Enter amount to withdraw: "))
    if amount<0:
        print("Invalid Amount")
        return 0
    else:
        return amount

def main():
    balance=0
    is_running=True
    while is_running:
        print("BANKING PROGRAMME")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice=input("Enter your choice(1-4): ")
        if choice=="1":
            show_balance(balance)
        elif choice=="2":
            balance+=deposit(balance)
        elif choice=="3":
            balance-=withdraw()
        elif choice=="4":
            is_running=False
if __name__=="__main__":
    main()
import random
import string

chars=" "+string.ascii_letters+string.digits+string.punctuation
chars=list(chars)
keys=chars.copy()
random.shuffle(keys)
#print(keys)
#ENCRYPTION
plain_text=input("Enter your text to encrypt: ")
cipher_text=""
for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=keys[index]
print(f"Original text: {plain_text}")
print(f"Encrypted Message: {cipher_text}")
#DECRYPTION
cipher_text=input("Enter your text to decrypt: ")
plain_text=""
for letter in cipher_text:
    index=keys.index(letter)
    plain_text+=chars[index]
print(f"Decrypted text: {cipher_text}")
print(f"Original Message: {plain_text}")
