
# import from standard library
import statistics
import math

# import from local files
from util_datafun_logger import setup_logger

# Set up logging .............................................

# Call the setup_logger function
logger, logname = setup_logger(__file__)

# Define shared data ..........................................

# define a variable with some univariant data
# (one varabile, many readings)
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 50, 51, 52, 53, 54, 98, 88, 101, 121, 151, 201, 55]

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
xtimes_list = list(range(10))
yvalues_list = [100, 200, 301, 402, 500, 605, 702, 811, 915, 1017]

# Define functions ........................................


def illustrate_list_statistics():
    """This function illustrates descriptive statistics for a numric list."""

    logger.info(f"list1: {list1}")

    # Descriptive: Averages and measures of central tendency
    # Use statisttics module to get mean, median, mode
    # for a values list

    mean = statistics.mean(list1)
    median = statistics.median(list1)
    mode = statistics.mode(list1)

    logger.info(f"mean: {mean}")
    logger.info(f"median: {median}")
    logger.info(f"mode: {mode}")

    stdev = statistics.stdev(list1)
    variance = statistics.variance(list1)

    logger.info(f"stdev: {stdev}")
    logger.info(f"variance: {variance}")


def illustrate_list_correlation_and_prediction():
    """This function illustrates correlation and prediction for a numric list."""

    logger.info(f"xtimes_list: {xtimes_list}")
    logger.info(f"yvalues_list: {yvalues_list}")

    # Descriptive: Measures of correlation
    # Use two numerical lists of the same size
    # Use statisttics module to get correlation between list1 and list2

    correlationxy = statistics.correlation(xtimes_list, yvalues_list)
    logger.info(f"correlation between x and y: {correlationxy}")

    # Predictive: Machine Learning - Linear Regression
    # If the corrlation is close to 1.0, then the data is linearly related
    # If so, use statistics module to get linear regression for list1 and list2
    # This is a form of supervised machine learning - it uses all known data
    # Use the slope and intercept and an unknown (future) x to predict a y value
    # Python functions can return multiple values

    slope, intercept = statistics.linear_regression(xtimes_list, yvalues_list)
    logger.info(f"The equation of the best fit line is: y = {slope}x + {intercept}")

    # Once we have learned the slope and intercept
    # of the best-fit straight line through the data,
    # we can use it to make predictions

    # Predict the y value for a given x value outside the range of the data

    x_max = max(xtimes_list)
    newx = x_max * 15  # predict for a future x value

    # Use the slope and intercept to predict a y value for the future x value
    # y = mx + b

    newy = slope * newx + intercept

    logger.info("We predict that when x = {newx}, y will be about {newy}")


def illustrate_list_built_in_functions():
    # BUILT-IN FUNCTIONS ......................................
    # Many built-in functions work on lists
    # try min(), max(), len(), sum(), sorted(), reversed()

    # Using the score list provided above, do the following:
    # Calcuate the max and min scores
    max_value = max(list1)
    min_value = min(list1)

    logger.info(f"Given score list: {list1}")
    logger.info(f"The max() is {max_value}")
    logger.info(f"The min() is {min_value}")

    # Calculate the length of the list
    len_list = len(list1)
    logger.info(f"The len() is {len_list}")

    # Calculate the sum of the list
    sum_list = sum(list1)
    logger.info(f"The sum() is {sum_list}")

    # Calculate the average of the list
    avg_list = sum_list / len_list
    logger.info(f"The average is {avg_list}")

    logger.info(f"Given score list: {list1}")
    # Return a new list soreted in ascending order
    asc_scores = sorted(list1)
    logger.info(f"Using the built-it function sorted(lst) gives: {asc_scores}")

    # Return a new list soreted in descending order
    desc_scores = sorted(list1, reverse=True)
    logger.info(
        f"Using the built-in function sorted(lst,reverse=True) gives: {desc_scores}"
    )


def illustrate_list_methods():
    """This function illustrates methods that can be called on a list"""

    """

     LIST METHODS ............................................... 

     Here are some common methods that operate on an instance of a list.

     append(x): Add an item to the end of the list.
     extend(iterable): Add all the items from an iterable (such as another list)
          to the end of the list.
     insert(i, x): Insert an item at a given position.
     remove(x): Remove the first occurrence of an item.
     pop([i]): Remove the item at the given position in the list, 
     and return it. If no index is specified, 
     removes and returns the last item in the list.
     clear(): Remove all items from the list.
     index(x[, start[, end]]): Return the index of the first occurrence of
          an item.
     count(x): Return the number of occurrences of an item.
     sort(key=None, reverse=False): Sort the items in the list 
          in ascending order.
     reverse(): Reverse the order of the items in the list.
     copy(): Return a shallow copy of the list.

     """

    # append an item to the end of the list
    lst = [3, 6, 1, 8, 2, 5]
    lst.append(7)

    # extend the list with another list
    lst.extend([9, 10, 11])

    # insert an item at a given position (0 = first item)
    i = 2
    newvalue = 4
    lst.insert(i, newvalue)

    # remove an item
    item_to_remove = 5
    lst.remove(item_to_remove)

    # Count how many times 2 appears in the list
    ct_of_111 = list1.count(2)

    # Sort the list in ascending order using the sort() method
    asc_scores2 = list1.sort()

    # Sort the list in descending order using the sort() method
    desc_scores2 = list1.sort(reverse=True)

    # Copy the list to a new list
    new_scores = list1.copy()
    logger.info(f"new_scores is: {new_scores}")

    # Remove the first item from the new list
    # The first item in a list is at index 0
    # Think of it as an offset from the beginning of the list
    first = new_scores.pop(0)
    logger.info(
        f"Popped the first (index=0): {first} and now, new_scores is: {new_scores}"
    )

    # Remove the last item from the new list
    # The last item in a list is at index -1
    last = new_scores.pop(-1)
    logger.info(
        f"Popped the last (index=-1): {last} and now, new_scores is: {new_scores}"
    )



def illustrate_list_transformations():
    """This function illustrates transformations that can be applied to a list"""

    logger.info("Score list: {list1}")

    # TRANFORMATIONS ............................

    # FILTER and MAP are critical tranformations in big data applications

    # Use the built-in function filter() anywhere you need to filter a list
    # Filter the new list to only include scores greater than 100
    # You could pass in a named function, but honestly this is easier
    # Say "KEEP x such that x > 100 is True" given list1
    # Cast the result using square brackets to get back a list
    scores_over_4 = [filter(lambda x: x < 4, list1)]
    logger.info(f"Scores over 100: {scores_over_4}")

    # Use the built-in function map() anywhere you need to transform a list

    # Map each element to its square
    # Say "map x to x squared" given list1
    # Cast the result using square brackets to get a list
    cube_roots = [map(lambda x: x ** (1/3), list1)]
    logger.info(f"Cube roots: {cube_roots}")

   #volume
    volume = map(lambda x: x** 3, list1)
    logger.info(f"Square root of scores: {volume}")


def illustrate_list_comprehensions():
    """This function illustrates list comprehensions"""

    logger.info("Score list: {list1}")

    # TRANFORMATIONS - Using List Comprehensions
    # List comprehensions are a concise way to create lists
    # They work like map and filter, but are more concise
    # They are the preferred "pythonic" way to do transformations
    # They are faster than map / filter - it's quite impressive when you master them!

    scores_under_6 = [x for x in list1 if x < 6]
    logger.info("Scores under 6 (using list comprehensions!): {scores_under_6}")

    triple_scores = [x * 3 for x in list1]
    logger.info("Tripled scores (using list comprehensions!): {triple_scores}")

    exponential_value = [math.exp(x) for x in list1]
    logger.info("Exponential scores (using list comprehensions!): {exponential_value}")







def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here (see instructions)
    illustrate_list_statistics()
    illustrate_list_correlation_and_prediction()
    illustrate_list_built_in_functions()
    illustrate_list_methods()
    illustrate_list_transformations()
    illustrate_list_comprehensions()

    logger.info("Add more logging statements to the code to see what happens.")
    logger.info("Explore enough to understand.")
    logger.info("Apply these skills to your own topic domain.")

    show_log()


# Why do we wrap parts of our code into functions?
# Because when you write good functions, you can reuse them in other scripts.
# Just like we import our logger and reuse the setup_logger() function.
# You can easily build a set of resuable functions to support your topic domain.

# For example, if your topic domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a lists of favorite artists.

# When you write reusable functions for your domain, you can
# import the module with your utility functions into other scripts
# and use them for free.
# This is excellent practice.
