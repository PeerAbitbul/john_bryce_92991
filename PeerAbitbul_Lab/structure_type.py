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

# Negative Indexing (Very useful to get the last item without knowing length)
print(f"Last element: {my_list[-1]}") # Abitbul

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

# Sorting
unsorted_list = [10, 2, 8, 1]
unsorted_list.sort()
print(f"Sorted list: {unsorted_list}")

# --- Pro Tip: Why Lists are the "Workhorse" of Data Engineering? ---
# 1. Dynamic Sizing: Unlike arrays in other languages, Lists grow automatically. 
#    Great for collecting data from a stream/loop when you don't know the size.
# 2. Data Cleaning: Lists are Mutable. You can load a raw dataset row, 
#    clean specific values (replace nulls, strip spaces), and keep the structure.
# 3. Stacks/Queues: Lists can easily act as a buffer (using append() and pop()) 
#    to manage tasks or data logs in order.


#############################################################################


# --- Python Tuples Comprehensive Guide ---

# 1. Create a Tuple (Uses parentheses () instead of brackets [])
# Can store different data types
my_tuple = (1, 2, 3, 4, 'Five', False)

# 2. Accessing Elements
print(f"Full tuple: {my_tuple}")
print(f"Element at index 4: {my_tuple[4]}")  # Five

# Negative Indexing (Starts from the end)
print(f"Second from the end: {my_tuple[-2]}") # False

# 3. Slicing [start:stop] - Note: 'stop' index is exclusive!
# Takes index 0, 1, 2, 3 (Stops before index 4)
print(f"Slicing [0:4]: {my_tuple[0:4]}") # (1, 2, 3, 4)



# 4. Tuple Unpacking
# "Unpack" the tuple into individual variables
a, b, c, d, e, f = my_tuple
print(f"Unpacked variables: a={a}, b={b}, e={e}")

# 5. Immutability - WHY we use Tuples
# Unlike Lists, you CANNOT change a tuple's elements.
# The code below would cause a TypeError:
# my_tuple[2] = 3.1  <-- This will fail!

# 6. Useful Tuple Methods
# Tuples have only 2 built-in methods because they can't be changed:

test_tuple = (1, 2, 3, 2, 2, 4)

# count() - How many times a value appears
print(f"How many times 2 appears: {test_tuple.count(2)}") # 3

# index() - Find the first index of a value
print(f"First index of value 3: {test_tuple.index(3)}")    # 2

# 7. Tuple Operations
T1 = (1, 2, 3)
T2 = (4, 5, 6)

print(f"Concatenation: {T1 + T2}") # Combines into a new tuple
print(f"Length of tuple: {len(T1)}") # 3
print(f"Membership: {2 in T1}")     # True

# --- Pro Tip: When to use a Tuple over a List? ---
# 1. Performance: Tuples are slightly faster than lists.
# 2. Safety: Use tuples for data that should NEVER change (e.g., (IP, Port) of a server).
# 3. Dictionary Keys: Tuples can be used as keys in a dictionary, Lists cannot.

#################################
# --- Python Dictionaries Comprehensive Guide ---

# 1. Create a Dictionary (Key-Value pairs)
# Uses curly braces {} and colon : to separate key from value
my_dict = {"name": "peer", "age": 30}

# 2. Accessing Elements
print(f"Full dictionary: {my_dict}")
print(f"Access by key 'name': {my_dict['name']}")
print(f"Access by key 'age': {my_dict['age']}")

# Note: Accessing a non-existent key directly causes an error:
# print(my_dict["phone"]) # KeyError!

# 3. Adding and Modifying Elements
# Add new key-value pair
my_dict["phone"] = "0523456789"
print(f"After adding 'phone': {my_dict}")

# Modify existing value
my_dict["name"] = "peer abitbul"
print(f"After modifying 'name': {my_dict}")

# 4. Removing Elements
# del - Removes a specific key completely
del my_dict["phone"]
print(f"After del 'phone': {my_dict}")

# pop() - Removes the key AND returns its value (Great for processing queues)
my_dict["phone"] = "0523456789" # Adding it back just to pop it
removed_value = my_dict.pop("phone")
print(f"Popped value: {removed_value}, Current dict: {my_dict}")

# 5. Safe Access with get()
# Useful when you are not sure if the key exists (avoids crashes)
print(f"Get 'age': {my_dict.get('age')}")

# If key doesn't exist, it returns None (instead of crashing)
print(f"Get 'phone' (not exists): {my_dict.get('phone')}")

# You can provide a custom default value if key is missing
print(f"Get with default: {my_dict.get('phone', 'No Phone Number Available')}")

# 6. Dictionary Methods (Keys, Values, Items)
# Useful for loops and data analysis
print(f"Keys: {my_dict.keys()}")     # Returns a list-like view of all keys
print(f"Values: {my_dict.values()}") # Returns a list-like view of all values
print(f"Items: {my_dict.items()}")   # Returns list of tuples (key, value)

# --- Pro Tip: Why Dictionaries are Crucial for Big Data/Cloud? ---
# 1. JSON Structure: Dictionaries are almost identical to JSON format,
#    which is the standard for API responses and NoSQL databases (like MongoDB).
# 2. Performance: Finding a value by Key (Lookup) is extremely fast (O(1)),
#    much faster than searching through a List.

##################################

# --- Python Sets Comprehensive Guide ---

# 1. Create a Set (Unordered, Unique elements)
# Uses curly braces {}, just like dictionaries, but without Key-Value pairs.
my_set = {1, 2, 3, 4, 5, 6, 7}
print(f"Original Set: {my_set}")

# Note: Sets do NOT allow duplicates. 
# If you try: {1, 2, 2, 3}, Python will automatically save it as {1, 2, 3}.

# 2. Accessing Elements
# Sets are UNORDERED. You cannot access items by index.
# print(my_set[1]) # TypeError: 'set' object is not subscriptable

# How to access? Iterate through it with a loop.
print("Iterating through set:")
for item in my_set:
    print(item)

# 3. Adding Elements
my_set.add(8)
print(f"After add(8): {my_set}")

# 4. Removing Elements
# method A: remove() - Raises Error if item doesn't exist
my_set.remove(7)
print(f"After remove(7): {my_set}")
# my_set.remove(99) # KeyError! 99 is not in the set.

# method B: discard() - Safe remove. NO Error if item doesn't exist.
my_set.discard(6)
print(f"After discard(6): {my_set}")

my_set.discard(99) # No error, simply does nothing.
print(f"After discard(99) (Safe): {my_set}")

# method C: pop() - Removes a RANDOM element (because sets are unordered)
removed_value = my_set.pop()
print(f"Popped value: {removed_value}, Current set: {my_set}")

# method D: clear() - Removes all elements
my_set.clear()
print(f"After clear(): {my_set}")

# 5. Set Operations (Mathematical Operations)
set1 = {1, 2, 3, 4, 5}
set2 = {5, 6, 7, 8, 9}

# Union (|) - Combines both sets (Removes duplicates automatically)
# Notice '5' appears only once.
print(f"Union (set1 | set2): {set1 | set2}") 

# Intersection (&) - Returns ONLY elements present in BOTH sets
print(f"Intersection (set1 & set2): {set1 & set2}") # {5}

# Difference (-) - Elements in Set1 that are NOT in Set2
print(f"Difference (set1 - set2): {set1 - set2}") # {1, 2, 3, 4}


# --- Pro Tip: When to use Sets in Data Engineering? ---

# 1. Removing Duplicates (Deduplication): 
#    The fastest way to clean a list with duplicates is: list(set(my_raw_list)).
# 2. Performance (Membership Test):
#    Checking "if x in my_set" is O(1) (Instant).
#    Checking "if x in my_list" is O(n) (Scans the whole list).
#    If you have millions of items (like Blacklisted IPs), ALWAYS use a Set for lookups.
# 3. Comparing Datasets:
#    Easily find missing records between two tables (e.g., ID_Set_TableA - ID_Set_TableB).

##################################

# --- Python Strings Comprehensive Guide ---

# 1. Create a String
# You can use single '' or double "" quotes (Result is the same)
my_string_single_quoted = "Hello, Peer Abitbul!"
my_string_double_quoted = "Hello, Peer Abitbul!"
print(f"This is single quoted: {my_string_single_quoted}")
print(f"This is double quoted: {my_string_double_quoted}")

# 2. Accessing & Slicing
# Strings are sequences, just like Lists.
print(f"Length of string: {len(my_string_single_quoted)}")
print(f"First character: {my_string_single_quoted[0]}")
print(f"Last character: {my_string_single_quoted[-1]}")

# Slicing [start:stop] (Stop is exclusive)
print(f"Slicing [7:11]: {my_string_single_quoted[7:11]}")  # Peer
print(f"Slicing [0:5]: {my_string_single_quoted[0:5]}")    # Hello
print(f"Slicing [::-1] (Reversed): {my_string_single_quoted[::-1]}")  # !lubitA reeP ,olleH

# 3. String Operations
connecting_strings = "Hello, " + "Peer!"
print(f"Concatenated string: {connecting_strings}")

repeated_string = "Ha" * 3
print(f"Repeated string: {repeated_string}")

# Membership Test (in / not in)
print(f"Is 'Peer' in string? {'Peer' in my_string_single_quoted}")
print(f"Is 'Python' not in string? {'Python' not in my_string_single_quoted}")

# 4. Useful Methods (Data Cleaning)
# Changing Case
upper_string = my_string_single_quoted.upper()
lower_string = my_string_single_quoted.lower()
print(f"Uppercase: {upper_string}")
print(f"Lowercase: {lower_string}")

# Replace & Strip (Trimming whitespace)
replace_string = my_string_single_quoted.replace("Peer", "Python")
print(f"Replaced string: {replace_string}")

trimmed_string = "   Hello, Peer!   ".strip()
print(f"Trimmed string: '{trimmed_string}'")

# 5. Analysis & Splitting
# split() turns String -> List
split_string = my_string_single_quoted.split(", ")
print(f"Split string: {split_string}") # ['Hello', 'Peer Abitbul!']

# find() & count()
find_index = my_string_single_quoted.find("Abitbul")
print(f"Index of 'Abitbul': {find_index}")

count_substring = my_string_single_quoted.count("e")
print(f"Count of 'e': {count_substring}")

# 6. Special String Types

# Multiline String (""") - Great for Documentation or SQL
multi_line_string = """This is a multi-line string.
It can span multiple lines.
Useful for documentation or large text blocks."""
print("Multi-line string:")
print(multi_line_string)

# Escaping (\)
# \n = New Line, \t = Tab, \" = Quote inside quote
string_with_quotes = 'He said, "Hello, Peer!" and didn\'t stop.'
print(f"String with quotes: {string_with_quotes}")

string_with_escape = "First Line\nSecond Line\tTabbed"
print("String with escape sequences:")
print(string_with_escape)

# Raw String (r"") - Ignores escape characters
raw_string = r"C:\Users\Peer\Documents"
print(f"Raw string: {raw_string}")


# --- Pro Tip: Strings for DBAs & Data Engineers ---

# 1. Raw Strings (r"path"): 
#    ALWAYS use r"C:\Path\To\File" for Windows file paths. 
#    Without 'r', Python thinks "\U" in "\Users" is a unicode escape and will crash.
# 2. Multiline for SQL:
#    Use triple quotes (""") to write clean SQL queries inside Python:
#    query = """
#    SELECT * FROM Users
#    WHERE Age > 30
#    """
# 3. f-strings:
#    The fastest and most readable way to inject variables into strings.
#    Instead of: "Hello " + name + ", age: " + str(age)
#    Use: f"Hello {name}, age: {age}"