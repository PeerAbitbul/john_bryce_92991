import pprint

# #############################################################################
# --- Section 1: Python pprint (Pretty Print) Comprehensive Guide ---
# #############################################################################

my_dic = {
    "name": "peer",
    "age": 30,
    "skills": ["python", "SQL", "JS"]
}

# 1. Standard pprint (Default)
print("1. Standard pprint:")
pprint.pprint(my_dic)

# 2. width=1 (Forces each element into its own line)
print("\n2. width=1 (Forces new lines):")
pprint.pprint(my_dic, width=1)

# 3. compact=True (Attempts to fit multiple elements per line)
print("\n3. compact=True:")
pprint.pprint(my_dic, compact=True)

# 4. indent=4 (Adds leading spaces to nested levels)
print("\n4. indent=4:")
pprint.pprint(my_dic, indent=4)

# 5. sort_dicts (Controls alphabetical sorting of keys)
print("\n5. sort_dicts=False (Keep original insertion order):")
pprint.pprint(my_dic, sort_dicts=False)

print("\n6. sort_dicts=True (Alphabetical order):")
pprint.pprint(my_dic, sort_dicts=True)

# 6. Combined Examples
print("\n7. Combined (width=20, indent=4, compact=True, sort_dicts=False):")
pprint.pprint(my_dic, width=20, indent=4, compact=True, sort_dicts=False)

# --- Pro Tip: Why pprint is essential for DBAs? ---
# 1. Inspecting Results: When fetching rows as dictionaries, pprint 
#    makes column-value mapping instantly readable.
# 2. Log Analysis: Great for printing out status objects or server health 
#    dictionaries in a way that’s easy to scan visually.


#############################################################################
# --- Section 2: Python Functions Comprehensive Guide ---
#############################################################################

# 1. Basic Function (No arguments)
def my_functionone():
    """Simple function that just performs an action."""
    print("this is my first function")

my_functionone()

# 2. Function with Required Arguments (Positional)
def my_functiontwo(name, age):
    """Must be called with exactly two values."""
    print(f"this is my name {name} and my age is {age}")
    return name, age

my_functiontwo("peer", 30)

# 3. Function with Default Arguments
def my_functionthree(name="peer", age=30):
    """If values are missing, it uses 'peer' and 30."""
    print(f"this is my name {name} and my age is {age}")
    return name, age

my_functionthree()               # Uses defaults
my_functionthree("abitbul", 25) # Overwrites both
my_functionthree(age=28, name="david") # Keyword call

# 4. *args (Variable Number of Positional Arguments)
def my_functionfour(*args):
    """Captures any number of arguments into a Tuple."""
    print(f"this is my args {args}")
    for i in args:
        print(i)
    return args

my_functionfour("peer", 30, "python", "SQL")

# 5. **kwargs (Variable Number of Keyword Arguments)
def my_functionfive(**kwargs):
    """Captures any number of key=value arguments into a Dictionary."""
    print(f"this is my kwargs {kwargs}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    return kwargs

my_functionfive(name="peer", age=30, skills=["python", "SQL", "JS"])



# --- Pro Tip: Functions in Data Engineering Workflows ---
# 1. Reusability: Use *args when writing a function that clears caches for 
#    multiple databases at once (e.g., clear_cache('DB1', 'DB2', 'DB3')).
# 2. Dynamic Configs: Use **kwargs for DB connection strings. It allows 
#    you to pass different parameters (port, timeout) without changing the code.