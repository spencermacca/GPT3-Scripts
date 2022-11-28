import random
import time

# Constants
VIRUS_NAMES = ["Trojan", "Worm", "Virus", "Malware", "Spyware"]

# Scan for Viruses
virus_name = random.choice(VIRUS_NAMES)
num_viruses = random.randint(1, 10)
num_infected_files = random.randint(1, 10)
num_cleaned_files = random.randint(1, 10)
num_seconds = random.randint(20,50)

# Print the results
print('Scanning...')
time.sleep(num_seconds)
print("Scanning complete!")
time.sleep(2)
print("Found {} instances of {}".format(num_viruses, virus_name))
print("Cleaned {} infected files".format(num_cleaned_files))
print("{} files still infected".format(num_infected_files))
print("Scan took {} seconds".format(num_seconds))
