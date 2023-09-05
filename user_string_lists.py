"""
Modify this docstring.

"""

# imports first
import random
from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

product_categories = ["Electronics", "Clothing", "Home Appliances", "Furniture", "Sports Equipment"]
sales_team_names = ["Team A", "Team B", "Team C", "Team D", "Team E"]
sales_performance_terms = ["Conversion Rate", "Revenue Growth", "Customer Acquisition", "Sales Funnel", "Lead Generation"]
customer_segments = ["Retail", "B2B", "E-commerce", "Small Business", "Enterprise"]
sales_strategies = ["Cold Calling", "Social Selling", "Inbound Marketing", "Upselling", "Cross-selling"]

# reusable functions next
length = len(product_categories)

# Check the length of the lists
length = len(product_categories)

# Use zip to combine the lists into tuples
combined_tuples = list(zip(product_categories, sales_performance_terms, sales_team_names))

# Display the combined tuples
for i, tpl in enumerate(combined_tuples):
    print(f"Tuple {i + 1}: {tpl}")

# Use set() to create a set of unique tuples
unique_tuples = set(combined_tuples)

# Display the unique tuples
logger.info("\nUnique Tuples:")
for i, tpl in enumerate(unique_tuples):
    print(f"Unique Tuple {i + 1}: {tpl}")

# Generate a random sentence
def generate_random_sentence():
    category = random.choice(product_categories)
    team_name = random.choice(sales_team_names)
    performance_term = random.choice(sales_performance_terms)
    segment = random.choice(customer_segments)
    strategy = random.choice(sales_strategies)

    sentence = f"In the {category} category, {team_name} achieved impressive {performance_term} in the {segment} segment using {strategy}."
    return sentence

# Generate and print random sentences
for _ in range(5):  # Generate 5 random sentences
    random_sentence = generate_random_sentence()
    print(random_sentence)

# Open and read the text file
with open("text_simple.txt", "r") as file:
    text = file.read()

# Split the text into words and convert them to lowercase
words = text.lower().split()

# Use set to get unique words
unique_words = set(words)

# Sort the list of unique words
sorted_unique_words = sorted(unique_words)

# Get the length of the list
word_count = len(sorted_unique_words)

# Display the length and the sorted list of unique words
print(f"Number of unique words: {word_count}")
print("Sorted list of unique words:")
for word in sorted_unique_words:
    print(word)

# call functions and execute code
# use if __name__ == "__main__":
