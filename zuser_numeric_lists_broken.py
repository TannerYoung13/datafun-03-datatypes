# Import some helpful modules from the Python Standard Library
import logging
import pathlib
import platform
import sys
import os
import datetime
import util_datafun_logger
import util_logger

"""
Modify this docstring.

"""

# import some standard modules first - how many can you make use of?
import math
import statistics

# TODO: import from local util_datafun_logger.py 
from util_datafun_logger import setup_logger
# TODO: Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

# TODO: Create some shared data lists if you like - or just create them in your functions
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 50, 51, 52, 53, 54, 98, 88, 101, 121, 151, 201, 55]
listx = list(range(10))
listy = [100, 200, 301, 402, 500, 605, 702, 811, 915, 1017]

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

    logger.info(f"listx: {listx}")
    logger.info(f"listy: {listy}")

    # Descriptive: Measures of correlation
    # Use two numerical lists of the same size
    # Use statisttics module to get correlation between list1 and list2

    correlationxy = statistics.correlation(listx, listy)
    logger.info(f"correlation between x and y: {correlationxy}")

    # Predictive: Machine Learning - Linear Regression
    # If the corrlation is close to 1.0, then the data is linearly related
    # If so, use statistics module to get linear regression for list1 and list2
    # This is a form of supervised machine learning - it uses all known data
    # Use the slope and intercept and an unknown (future) x to predict a y value
    # Python functions can return multiple values

    slope, intercept = statistics.linear_regression(listx, listy)
    logger.info(f"The equation of the best fit line is: y = {slope}x + {intercept}")

    # Once we have learned the slope and intercept
    # of the best-fit straight line through the data,
    # we can use it to make predictions

    # Predict the y value for a given x value outside the range of the data

    x_max = max(listx)
    newx = x_max * 1.5  # predict for a future x value

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

    unique_values_setx = set(list1)
    logger.info(f"Set of unique values: {unique_values_setx}")

    logger.info(f"Given score list: {list1}")
    # Return a new list soreted in ascending order
    asc_scores = sorted(list1)
    logger.info(f"Using the built-it function sorted(lst) gives: {asc_scores}")

    # Return a new list soreted in descending order
    desc_scores = sorted(list1, reverse=True)
    logger.info(
        f"Using the built-in function sorted(lst,reverse=True) gives: {desc_scores}"
    )
def list_methods():
    # Create a new list named 'lst'
    lst = [3, 6, 1, 8, 2, 5]

    # Append a single value to the list
    lst.append(7)
    logger.info(f"\nAfter appending 7:", lst)

    # Extend the list with a new list
    lst.extend([9, 10])
    logger.info(f"After extending with [9, 10]:", lst)

    # Insert a value at an index
    lst.insert(2, 4)
    logger.info(f"After inserting 4 at index 2:", lst)

    # Remove the number 5 from the list, if found
    if 5 in lst:
        lst.remove(5)
    logger.info(f"After removing 5 (if found):", lst)

    # Count how many times 2 appears in the list
    count_2 = lst.count(2)
    logger.info(f"Count of 2 in the list:", count_2)

    # Sort the list in ascending order
    lst.sort()
    logger.info(f"Sorted list (ascending):", lst)

    # Sort the list in descending order
    lst.sort(reverse=True)
    logger.info(f"Sorted list (descending):", lst)

    # Create a copy of the list
    lst_copy = lst.copy()
    logger.info(f"Copy of the list:", lst_copy)

    # Pop the first item off the top of the list (index 0)
    first_item = lst.pop(0)
    logger.info(f"Popped first item ({first_item}) from the list:", lst)

    # Pop the last item off the bottom of the list
    last_item = lst.pop()
    logger.info(f"Popped last item ({last_item}) from the list:", lst)

def list_transformations():
    lst = [3, 6, 1, 8, 2, 5]
    # Use filter() to keep values less than 4
    filtered_values = filter(lambda x: x < 4, lst)

    # Use map() to calculate the cube root of each value
    cube_roots = map(lambda x: x ** (1/3), lst)

    # Use map() to calculate the volume of a cube with a side equal to each value
    cube_volumes = map(lambda x: x ** 3, lst)

    # Convert the results to lists for logger.infoing
    filtered_values_list = list(filtered_values)
    cube_roots_list = list(cube_roots)
    cube_volumes_list = list(cube_volumes)

    # logger.info the results
    logger.info(f"\nValues less than 4:", filtered_values_list)
    logger.info(f"Cube roots:", cube_roots_list)
    logger.info(f"Volumes of cubes:", cube_volumes_list)


    # Use a list comprehension to filter values less than 6
    filtered_values = [x for x in list1 if x < 6]

    # Use a list comprehension to triple each value
    tripled_values = [x * 3 for x in list1]

    # Use a list comprehension to transform the list using a custom transformation (e.g., squaring)
    transformed_values = [x ** 2 for x in list1]

    # logger.info the results
    logger.info(f"\nValues less than 6:", filtered_values)
    logger.info(f"Triple of each value:", tripled_values)
    logger.info(f"Squared values:", transformed_values)


# TODO: define some custom functions

def custom_function_1(param1, param2):
    result = param1 * param2
    logger.info("Custom Function 1 executed with params: {} and {}. Result: {}".format(param1, param2, result))
    return result

def custom_function_2(data_list):
    processed_data = [item.upper() for item in data_list]
    logger.info("Custom Function 2 processed data: {}".format(processed_data))
    return processed_data



# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here (see instructions)
    illustrate_list_statistics()
    illustrate_list_correlation_and_prediction()
    illustrate_list_built_in_functions()


    logger.info("Add more logging statements to the code to see what happens.")
    logger.info("Explore enough to understand.")
    logger.info("Apply these skills to your own topic domain.")

    