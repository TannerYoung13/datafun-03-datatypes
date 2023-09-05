# Import some helpful modules from the Python Standard Library

import logging
import pathlib
import platform
import sys
import os
import datetime

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

# Calculate mean, median, and mode for list1
mean_list1 = sum(list1) / len(list1)
median_list1 = statistics.median(list1)
mode_list1 = statistics.mode(list1)

# Calculate mean, median, and mode for listx
mean_listx = sum(listx) / len(listx)
median_listx = statistics.median(listx)
# Mode cannot be calculated for listx as it contains unique values

# Calculate mean, median, and mode for listy
mean_listy = sum(listy) / len(listy)
median_listy = statistics.median(listy)
# Mode cannot be calculated for listx as it contains unique values

# Display the results
logger.info(f"For list1:")
logger.info(f"Mean: {(mean_list1)}")
logger.info(f"Median: {median_list1}")
logger.info(f"Mode: {mode_list1}")

logger.info(f"\nFor listx:")
logger.info(f"Mean: {mean_listx}")
logger.info(f"Median: {median_listx}")

logger.info("\nFor listy:")
logger.info(f"Mean: {mean_listy}")
logger.info(f"Median: {median_listy}")

# Calculate standard deviation and variance for list1
std_deviation_list1 = statistics.stdev(list1)
variance_list1 = statistics.variance(list1)

# Calculate standard deviation and variance for listx
std_deviation_listx = statistics.stdev(listx)
variance_listx = statistics.variance(listx)

# Calculate standard deviation and variance for listy
std_deviation_listy = statistics.stdev(listy)
variance_listy = statistics.variance(listy)

# Display the results
logger.info(f"For list1:")
logger.info(f"Standard Deviation: {std_deviation_list1}")
logger.info(f"Variance: {variance_list1}")

logger.info("\nFor listx:")
logger.info(f"Standard Deviation: {std_deviation_listx}")
logger.info(f"Variance: {variance_listx}")

logger.info("\nFor listy:")
logger.info(f"Standard Deviation: {std_deviation_listy}")
logger.info(f"Variance: {variance_listy}")

# Calculate the numerator and denominators for the correlation formula
numerator = sum((x - mean_listx) * (y - mean_listy) for x, y in zip(listx, listy))
denominator_x = sum((x - mean_listx) ** 2 for x in listx)
denominator_y = sum((y - mean_listy) ** 2 for y in listy)

# Calculate the correlation coefficient
correlation = numerator / (denominator_x ** 0.5 * denominator_y ** 0.5)

# Display the correlation coefficient
logger.info(f"Correlation between listx and listy: {correlation}")

slope= 2.9
intercept = 15

# Future time for prediction
future_time = 15

# Predict the y-value at the future time using the linear equation y = mx + b
predicted_y = slope * future_time + intercept

# Display the predicted y-value
logger.info(f"Predicted y-value at future time {future_time}: {predicted_y}")

logger.info(f"\nThe following values are for list 1")
# Find the minimum value in list1
minimum_value1 = min(list1)
logger.info(f"Minimum value: {minimum_value1}")

# Find the maximum value in list1
maximum_value1 = max(list1)

logger.info(f"Maximum value: {maximum_value1}")

# Find the length (number of elements) of list1
length_of_list1 = len(list1)

logger.info(f"Length of the list: {length_of_list1}")

# Calculate the sum of all values in list1
sum_of_values1 = sum(list1)

logger.info(f"Sum of values: {sum_of_values1}")

# Calculate the average of the values
mean1 = sum_of_values1 / length_of_list1
logger.info(f"Average (Mean): {mean1}")

# Create a set from the list (removing duplicates)
unique_values_set1 = set(list1)

logger.info(f"Set of unique values: {unique_values_set1}")

# Sort list1 in ascending order
sorted_list1 = sorted(list1)

logger.info(f"Sorted list (ascending): {sorted_list1}")

# Sort list1 in descending order
reverse_sorted_list1 = sorted(list1, reverse=True)
logger.info(f"Sorted list (descending): {reverse_sorted_list1}")

logger.info(f"\nThe following values are for list x")
# Find the minimum value in listx
minimum_valuex = min(listx)
logger.info(f"Minimum value: {minimum_valuex}")

# Find the maximum value in listx
maximum_valuex = max(listx)

logger.info(f"Maximum value: {maximum_valuex}")

# Find the length (number of elements) of listx
length_of_listx = len(listx)

logger.info(f"Length of the list: {length_of_listx}")

# Calculate the sum of all values in listx
sum_of_valuesx = sum(listx)

logger.info(f"Sum of values: {sum_of_valuesx}")

# Calculate the average of the values
meanx = sum_of_valuesx / length_of_listx
logger.info(f"Average (Mean): {meanx}")

# Create a set from the listx (removing duplicates)
unique_values_setx = set(listx)

logger.info(f"Set of unique values: {unique_values_setx}")

# Sort listx in ascending order
sorted_listx = sorted(listx)

logger.info(f"Sorted list (ascending): {sorted_listx}")

# Sort listx in descending order
reverse_sorted_listx = sorted(listx, reverse=True)
logger.info(f"Sorted list (descending): {reverse_sorted_listx}")

logger.info(f"\nThe following values are for list y")
# Find the minimum value in listy
minimum_valuey = min(listy)
logger.info(f"Minimum value: {minimum_valuey}")

# Find the maximum value in listy
maximum_valuey = max(listy)

logger.info(f"Maximum value: {maximum_valuey}")

# Find the length (number of elements) of listy
length_of_listy = len(listy)

logger.info(f"Length of the list: {length_of_listy}")

# Calculate the sum of all values in listy
sum_of_valuesy = sum(listy)

logger.info(f"Sum of values: {sum_of_valuesy}")

# Calculate the average of the values
meany = sum_of_valuesy / length_of_listy
logger.info(f"Average (Mean): {meany}")

# Create a set from the listy (removing duplicates)
unique_values_sety = set(listy)

logger.info(f"Set of unique values: {unique_values_sety}")

# Sort listy in ascending order
sorted_listy = sorted(listy)

logger.info(f"Sorted list (ascending): {sorted_listy}")

# Sort listx in descending order
reverse_sorted_listy = sorted(listy, reverse=True)
logger.info(f"Sorted list (descending): {reverse_sorted_listy}")

# Create a new list named 'lst'
lst = [3, 6, 1, 8, 2, 5]

# Append a single value to the list
lst.append(7)
logger.info("\nAfter appending 7:", lst)

# Extend the list with a new list
lst.extend([9, 10])
logger.info("After extending with [9, 10]:", lst)

# Insert a value at an index
lst.insert(2, 4)
logger.info("After inserting 4 at index 2:", lst)

# Remove the number 5 from the list, if found
if 5 in lst:
    lst.remove(5)
logger.info("After removing 5 (if found):", lst)

# Count how many times 2 appears in the list
count_2 = lst.count(2)
logger.info("Count of 2 in the list:", count_2)

# Sort the list in ascending order
lst.sort()
logger.info("Sorted list (ascending):", lst)

# Sort the list in descending order
lst.sort(reverse=True)
logger.info("Sorted list (descending):", lst)

# Create a copy of the list
lst_copy = lst.copy()
logger.info("Copy of the list:", lst_copy)

# Pop the first item off the top of the list (index 0)
first_item = lst.pop(0)
logger.info(f"Popped first item ({first_item}) from the list:", lst)

# Pop the last item off the bottom of the list
last_item = lst.pop()
logger.info(f"Popped last item ({last_item}) from the list:", lst)


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
logger.info("\nValues less than 4:", filtered_values_list)
logger.info("Cube roots:", cube_roots_list)
logger.info("Volumes of cubes:", cube_volumes_list)


# Use a list comprehension to filter values less than 6
filtered_values = [x for x in list1 if x < 6]

# Use a list comprehension to triple each value
tripled_values = [x * 3 for x in list1]

# Use a list comprehension to transform the list using a custom transformation (e.g., squaring)
transformed_values = [x ** 2 for x in list1]

# logger.info the results
logger.info("\nValues less than 6:", filtered_values)
logger.info("Triple of each value:", tripled_values)
logger.info("Squared values:", transformed_values)


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

    # call your functions here (see instructions)
    logger.info("Replace this with calls to your functions." )



