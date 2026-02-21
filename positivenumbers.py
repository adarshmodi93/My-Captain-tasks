# Program to print all positive numbers in a range/list

# The input lists provided in the task
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

# --- Process list1 ---
positive_list1 = []
for num in list1:
    # Check if the number is positive
    if num > 0:
        positive_list1.append(num)

print("Input: list1 =", list1, " Output:", positive_list1)


# --- Process list2 ---
positive_list2 = []
for num in list2:
    # Check if the number is positive
    if num > 0:
        positive_list2.append(num)

print("Input: list2 =", list2, " Output:", positive_list2)