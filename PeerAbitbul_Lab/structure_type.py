# --- Python Lists Comprehensive Guide ---

# 1. Create a list (Can store different data types)
my_list = [1, 'peer', 1.3, "Abitbul"]

# 2. Accessing Elements
print(f"Full list: {my_list}")
print(f"Element at index 1: {my_list[1]}") # peer
print(f"Element at index 3: {my_list[3]}") # Abitbul

# 3. Slicing [start:stop] - Note: 'stop' index is exclusive!
# This will take index 1 and 2, but NOT 3.
print(f"Slicing [1:3]: {my_list[1:3]}") # ['peer', 1.3]



# 4. Modifying Elements
my_list[2] = 3.1
print(f"After changing index 2: {my_list}")

# 5. Adding Elements
my_list.append(True)      # Adds to the END of the list
my_list.insert(2, 99)    # Adds 99 at index 2, shifts others to the right
print(f"After append and insert: {my_list}")

# extend() vs append()
my_list.extend([7, 8]) # Adds multiple elements as individual items
print(f"After extend: {my_list}")

# 6. Removing Elements
my_list.remove(99)       # Removes the FIRST occurrence of the VALUE 99
print(f"After remove(99): {my_list}")

# pop() - Removes by index AND returns the value
removed_value = my_list.pop(2)
print(f"Popped value: {removed_value}, Current list: {my_list}")

# del - Removes by index without returning value
del my_list[2]
print(f"After del my_list[2]: {my_list}")

# 7. List Operations & Useful Methods
L1 = [1, 2, 3]
L2 = [4, 5, 6]

print(f"Concatenation: {L1 + L2}") # Combines lists
print(f"Repetition: {L1 * 3}")     # Repeats [1,2,3] three times
print(f"Length: {len(L1)}")        # Number of elements
print(f"Membership test: {2 in L1}") # True if 2 exists in L1

# --- Added Pro Tips for Big Data/Cloud ---

# Negative Indexing (Starts from the end)
print(f"Last element: {L1[-1]}") # 3


# Sorting
unsorted_list = [10, 2, 8, 1]
unsorted_list.sort()
print(f"Sorted list: {unsorted_list}")