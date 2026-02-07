"""
MB215 Lab — Lists, Tuples, Files, and Matplotlib (Activities 1–15)

How to use:
1) Run this script
2) Type an activity number (1–15)
3) Take a screenshot of the output
4) Repeat for each activity

Note:
- Activity 15 opens graphs (matplotlib). Take screenshots of the graphs too.
"""

import traceback


# -------------------------
# Activity 1: Define a list with different types of elements + tuple to list
# -------------------------
def activity1():
    my_list = [1, "two", 3.0, True]
    print("The entire list:", my_list)

    my_tuple = (4, "five", 6.0, False)
    tuple_to_list = list(my_tuple)
    print("Converted list from tuple:", tuple_to_list)


# -------------------------
# Activity 2: Repetitions over lists
# -------------------------
def activity2():
    simple_list = ['a', 'b', 'c']
    repeated_list = simple_list * 3
    print("Repeated list:", repeated_list)

    for element in repeated_list:
        print(element)


# -------------------------
# Activity 3: Index in lists
# -------------------------
def activity3():
    my_list = [10, 20, 30, 40, 50]
    element_to_find = 30

    if element_to_find in my_list:
        index = my_list.index(element_to_find)
        print(f"The element {element_to_find} is at index {index}.")
    else:
        print(f"The element {element_to_find} is not in the list.")

    print(f"The value at index 0 is {my_list[0]}.")
    print(f"The length of the list is {len(my_list)}.")

    my_list[0] = 999
    print("The new list after the change is:", my_list)


# -------------------------
# Activity 4: Concatenating lists using + and +=
# -------------------------
def activity4():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    concatenated_list = list1 + list2
    print("Concatenated list using + operator:", concatenated_list)

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list1 += list2
    print("Concatenated list using += operator:", list1)

    # Demonstrating the error safely
    list1 = [1, 2, 3]
    number = 4
    try:
        _ = list1 + number
    except TypeError as e:
        print("Attempting list + number causes TypeError:", e)


# -------------------------
# Activity 5: List slicing
# -------------------------
def activity5():
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    basic_slice = my_list[2:6]
    print("Basic slice (2:6):", basic_slice)

    start_not_specified = my_list[:4]
    print("Slice with start not specified (:4):", start_not_specified)

    end_not_specified = my_list[7:]
    print("Slice with end not specified (7:):", end_not_specified)

    step_slice = my_list[1:8:2]
    print("Slice with step value (1:8:2):", step_slice)

    negative_indexes = my_list[-5:-1]
    print("Slice with negative indexes (-5:-1):", negative_indexes)


# -------------------------
# Activity 6: Finding items in lists with in / not in
# -------------------------
def activity6():
    my_list = [10, 20, 30, 40, 50]

    item_to_check = 30
    if item_to_check in my_list:
        print(f"{item_to_check} is in the list.")
    else:
        print(f"{item_to_check} is not in the list.")

    item_to_check = 60
    if item_to_check not in my_list:
        print(f"{item_to_check} is not in the list.")
    else:
        print(f"{item_to_check} is in the list.")


# -------------------------
# Activity 7: List methods (append, count, index)
# -------------------------
def activity7():
    my_list = []
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(20)

    item_to_count = 20
    count_result = my_list.count(item_to_count)
    print(f"The item {item_to_count} appears {count_result} times in the list.")

    item_to_find = 20
    try:
        index_result = my_list.index(item_to_find)
        print(f"The first occurrence of {item_to_find} is at index {index_result}.")
    except ValueError:
        print(f"{item_to_find} is not in the list.")

    item_not_in_list = 40
    try:
        index_result = my_list.index(item_not_in_list)
        print(f"The first occurrence of {item_not_in_list} is at index {index_result}.")
    except ValueError:
        print(f"{item_not_in_list} is not in the list, and it raises a ValueError.")


# -------------------------
# Activity 8: insert, sort, remove, reverse, del, sum, min, max
# -------------------------
def activity8():
    my_list = [10, 30, 20, 40, 20]
    print("Initial list:", my_list)

    my_list.append(50)
    my_list.append(20)
    print("After appending 50 and 20:", my_list)

    my_list.insert(2, 25)
    print("After inserting 25 at index 2:", my_list)

    my_list.sort()
    print("After sorting:", my_list)

    item_to_count = 20
    print(f"The item {item_to_count} appears {my_list.count(item_to_count)} times in the list.")

    item_to_remove = 20
    my_list.remove(item_to_remove)
    print("After removing first 20:", my_list)

    my_list.reverse()
    print("After reversing:", my_list)

    index_to_delete = 2
    del my_list[index_to_delete]
    print("After deleting item at index 2:", my_list)

    list_sum = sum(my_list)
    list_min = min(my_list)
    list_max = max(my_list)

    print("Updated list:", my_list)
    print(f"Sum of elements: {list_sum}")
    print(f"Minimum value: {list_min}")
    print(f"Maximum value: {list_max}")


# -------------------------
# Activity 9: Copying lists + total + average
# -------------------------
def activity9():
    original_list = [1, 2, 3, 4, 5]

    copied_list1 = []
    for item in original_list:
        copied_list1.append(item)
    print("Method 1: Copied list using a for loop:", copied_list1)

    copied_list2 = [] + original_list
    print("Method 2: Copied list using concatenation:", copied_list2)

    copied_list = list(original_list)
    total = sum(copied_list)
    average = total / len(copied_list) if copied_list else 0

    print("Total of numeric values in the copied list:", total)
    print("Average of numeric values in the copied list:", average)


# -------------------------
# Activity 10: Save a list to a file + read it back
# -------------------------
def activity10():
    def save_list_to_file(file_name, input_list):
        try:
            with open(file_name, 'w', encoding="utf-8") as file:
                file.writelines(f"{item}\n" for item in input_list)
        except Exception:
            print("Error while writing to file.")
            traceback.print_exc()

    def read_list_from_file(file_name):
        try:
            with open(file_name, 'r', encoding="utf-8") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []
        except Exception:
            print("Error while reading from file.")
            traceback.print_exc()
            return []

    original_list = ['Apple', 'Banana', 'Cherry', 'Date']
    file_name = 'fruits.txt'

    save_list_to_file(file_name, original_list)
    read_data = read_list_from_file(file_name)
    print("Data read from the file:", read_data)


# -------------------------
# Activity 11: List comprehensions
# -------------------------
def activity11():
    list1 = [1, 2, 3, 4]
    list2 = [item ** 2 for item in list1]
    print("Previous list:", list1)
    print("New list (squares):", list2)

    str_list = ['Winken', 'Blinken', 'Nod']
    len_list = [len(s) for s in str_list]
    print("Number of chars in each string:", len_list)

    list1 = [1, 12, 2, 20, 3, 15, 4]
    list2 = [n for n in list1 if n < 10]
    print("Numbers less than 10:", list2)


# -------------------------
# Activity 12: Two-dimensional list
# -------------------------
def activity12():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Two-dimensional list (matrix):")
    for row in matrix:
        print(row)

    element_00 = matrix[0][0]
    element_12 = matrix[1][2]
    element_21 = matrix[2][1]

    print("\nAccessed elements:")
    print(f"Element at [0][0]: {element_00}")
    print(f"Element at [1][2]: {element_12}")
    print(f"Element at [2][1]: {element_21}")

    print("\nProcessed data:")
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()


# -------------------------
# Activity 13: Tuples in Python (mutable list inside a tuple)
# -------------------------
def activity13():
    t = (10, 20, [97, 98, 99])
    print("Original tuple:", t)

    t[2].append(100)
    print("Modified tuple:", t)


# -------------------------
# Activity 14: Convert tuple to list and list back to tuple
# -------------------------
def activity14():
    t = (10, 20, [97, 98, 99])
    print("Original tuple:", t)

    list_from_tuple = list(t)
    print("List from tuple:", list_from_tuple)

    list_from_tuple[2].append(100)
    tuple_from_list = tuple(list_from_tuple)

    print("Tuple from modified list:", tuple_from_list)


# -------------------------
# Activity 15: Plotting data with matplotlib (line, bar, pie)
# -------------------------
def activity15():
    import matplotlib.pyplot as plt

    # Line graph
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]
    plt.plot(x_coords, y_coords)
    plt.title("Activity 15: Line Graph")
    plt.show()

    # Bar chart
    left_edges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]
    plt.bar(left_edges, heights)
    plt.title("Activity 15: Bar Chart")
    plt.show()

    # Pie chart
    values = [20, 60, 80, 40]
    plt.pie(values)
    plt.title("Activity 15: Pie Chart")
    plt.show()


def main():
    activities = {
        "1": activity1,
        "2": activity2,
        "3": activity3,
        "4": activity4,
        "5": activity5,
        "6": activity6,
        "7": activity7,
        "8": activity8,
        "9": activity9,
        "10": activity10,
        "11": activity11,
        "12": activity12,
        "13": activity13,
        "14": activity14,
        "15": activity15
    }

    while True:
        print("\n--- MB215 Activities 1–15 ---")
        print("Type a number 1–15 to run an activity.")
        print("Type 'all' to run 1–14 (Activity 15 opens plots).")
        print("Type 'q' to quit.")

        choice = input("Your choice: ").strip().lower()

        if choice == "q":
            print("Good luck! ✅")
            break

        if choice == "all":
            for n in range(1, 15):
                print(f"\nRunning Activity {n}...\n")
                activities[str(n)]()
            print("\nDone Activities 1–14. Run Activity 15 separately for plots.")
            continue

        if choice in activities:
            print(f"\nRunning Activity {choice}...\n")
            activities[choice]()
        else:
            print("Invalid input. Please choose 1–15, 'all', or 'q'.")


if __name__ == "__main__":
    main()