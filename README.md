# Python Bug: TypeError in calculate_average function

This repository demonstrates a common error in Python: a `TypeError` occurring when a function expects numeric input but receives a list containing non-numeric elements. The `calculate_average` function is designed to compute the average of a list of numbers. However, it fails when the list includes strings or other non-numeric data types.

## Bug Description

The `calculate_average` function does not explicitly check the data type of elements within the input list.  If a non-numeric element is present, the `sum()` function will raise a `TypeError` during execution. The bug is present in `bug.py`. The solution is in `bugSolution.py`

## Bug Solution

The solution involves adding error handling using a `try-except` block to gracefully handle potential `TypeError` exceptions. This approach prevents the program from crashing and allows for more robust error handling.