

# Task 2: Explore more about Python variables

# 1. Assigning different data types to variables
name = "Rudra"             # String
age = 18                   # Integer
height = 5.8               # Float
is_student = True          # Boolean

# Print values and their types
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Is Student:", is_student, "| Type:", type(is_student))

print("\n---")

# 2. Dynamic typing in Python: changing data types of a variable
value = 10
print("Initial value:", value, "| Type:", type(value))

value = "Ten"
print("After reassignment:", value, "| Type:", type(value))

print("\n---")

# 3. Invalid variable names: using a number at the beginning
try:
    exec("1name = 'Invalid'")  # Variable names can't start with a number
except SyntaxError:
    print("Error: Variable names cannot start with a digit.")

# 4. Invalid variable names: using special characters
try:
    exec("user-name = 'Invalid'")  # Hyphens are not allowed in variable names
except SyntaxError:
    print("Error: Variable names cannot contain special characters like '-'.")

# 5. Using underscore (_) and camelCase
user_name = "valid_name"
userName = "alsoValid"
print("user_name:", user_name)
print("userName:", userName)
