"""
Modify this docstring.

""" 
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

sales_rep_info = ("John Doe", 35, "Team A", "Senior Sales Rep")
customer_info = ("Company XYZ", "Retail", "New York", "contact@companyxyz.com")
product_info = ("Product A", "Electronics", "High-end smartphone", 599.99)

# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Get the intersection of the sets
intersection = set1.intersection(set2)

# Get the union of the sets
union = set1.union(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Intersection of Set 1 and Set 2:", intersection)
print("Union of Set 1 and Set 2:", union)


# Initialize an empty dictionary to store word counts
word_count_dict = {}

# Open and read the text file
with open("text_simple.txt", "r") as file:
    text = file.read()

# Split the text into words
words = text.split()

# Iterate through the words and count them
for word in words:
    # Remove punctuation and convert to lowercase for consistency
    word = word.strip('.,!?"\'').lower()
    
    # Update the word count in the dictionary
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

# Display the word count dictionary
for word, count in word_count_dict.items():
    print(f"\n{word}: {count}")
