def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = 0
    count = 0
    for number in numbers:
        try:
            total += number
            count += 1
        except TypeError:
            print(f"Skipping non-numeric element: {number}")
    if count == 0:
        return 0 #Handle empty list after removing non numeric elements
    average = total / count
    return average

# Example usage
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Example of the bug
my_numbers_with_string = [10,20,'30',40,50]
average_bug = calculate_average(my_numbers_with_string)
print(f"The average is: {average_bug}")
