"""
Author: Surya Pratap Singh Chauhan
GitHub: https://github.com/brodante
Email: surya.pratap0038@gmail.com
Website: https://brodante.github.io/portfolio/

Description: final year college student stuck in an infinite loop.
"""
# main.py
import os
import identifyhash
import hashify
import time

ver = "0.04 beta"
def logo(): # https://patorjk.com/software/taag/#p=display&f=Big&t=KeyGuardian%20v0.04%20beta
    os.system("cls" if os.name == "nt" else "clear")
    #print("\n\n")
    print("\033[96m" + "{:^80}".format("KeyGuardian v"+ver) + "\033[0m")
    print("""\033[92m
  _  __           _____                     _ _                      ___   ___  _  _     _          _        
 | |/ /          / ____|                   | (_)                    / _ \ / _ \| || |   | |        | |       
 | ' / ___ _   _| |  __ _   _  __ _ _ __ __| |_  __ _ _ __   __   _| | | | | | | || |_  | |__   ___| |_ __ _ 
 |  < / _ \ | | | | |_ | | | |/ _` | '__/ _` | |/ _` | '_ \  \ \ / / | | | | | |__   _| | '_ \ / _ \ __/ _` |
 | . \  __/ |_| | |__| | |_| | (_| | | | (_| | | (_| | | | |  \ V /| |_| | |_| |  | |   | |_) |  __/ || (_| |
 |_|\_\___|\__, |\_____|\__,_|\__,_|_|  \__,_|_|\__,_|_| |_|   \_/  \___(_)___/   |_|   |_.__/ \___|\__\__,_|
            __/ |                                                                                   by:\033[91m D4NT3\033[0m\033[92m
           |___/                                                                                             
\033[0m""")

def identify_hash():
    identifyhash.identify_hash()
def encrypt():
    hashify.hashify()
    #print("Encryption function")

def decrypt():
    # Implement decryption logic here
    print("Decryption function")

def exit_program():
    print("\nByeBye...")
    exit()

def main():
    while True:
        try:
            logo()
            print("\nMenu:")
            print("1. Identify Hash")
            print("2. Encrypt")
            print("3. Decrypt")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                identify_hash()
            elif choice == "2":
                encrypt()
            elif choice == "3":
                decrypt()
            elif choice == "4":
                exit_program()
            else:
                print("Invalid choice! Please enter a valid option.")
                for remaining in range(3, 0, -1):
                    print(f"\033[91mReturning to main menu in {remaining}...\033[0m", end="\r")
                    time.sleep(1)  # Wait for 1 second
        except KeyboardInterrupt:
            print("\nByeBye...")
            exit()

if __name__ == "__main__":
    main()