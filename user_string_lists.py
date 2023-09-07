"""
Purpose: Illustrate string lists
"""

import random

from util_datafun_logger import setup_logger

# Set up logging .............................................

logger, logname = setup_logger(__file__)

# Define shared data ..........................................

product_categories = ["Electronics", "Clothing", "Home Appliances", "Furniture", "Sports Equipment"]
sales_team_names = ["Team A", "Team B", "Team C", "Team D", "Team E"]
sales_performance_terms = ["Conversion Rate", "Revenue Growth", "Customer Acquisition", "Sales Funnel", "Lead Generation"]
customer_segments = ["Retail", "B2B", "E-commerce", "Small Business", "Enterprise"]
sales_strategies = ["Cold Calling", "Social Selling", "Inbound Marketing", "Upselling", "Cross-selling"]


def built_ins():
    length = len(product_categories)
    logger.info("Length:{length}")

    set_sort = set(product_categories)
    logger.info("Combined tuples:{set_sort}")

    # Use zip to combine the lists into tuples
    combined_tuples = list(zip(product_categories, sales_performance_terms, sales_team_names))
    logger.info("Combined tuples:{combined_tuples}")


def random_choice():
    random_product_category = random.choice(product_categories)
    logger.info("Random Product Category:", random_product_category)

def generate_random_sent():
    product_word = random.choice(product_categories)
    logger.info("A {product_word} is really good with a {product_word}")

    
    with open("text_simple.txt", "r") as fileObject:
        text = fileObject.read()
        list_words = text.split()  # split on whitespace
        unique_words = set(list_words)  # remove duplicates by making a set

        # Get the count and list of words
        word_ct = len(list_words)

        logger.info(f"The list of words is: {list_words}")
        logger.info(f"There are {word_ct} words in the file.")

        # Print the count and list of unique words
        unique_word_ct = len(unique_words)

        logger.info(f"The set of unique words is: {unique_words}")
        logger.info(f"There are {unique_word_ct} unique words in the file.")


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!
# Remember, code blocks must be indented consistently after a colon.

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    built_ins()
    random_choice()
    generate_random_sent()

    show_log()
