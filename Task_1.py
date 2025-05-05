# Task 1: Working with Variables in Python

# 1. Create a variable named pi and store the value 22/7 in it
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))

# 2. Attempt to create a variable called 'for' and assign it a value of 4
print("\nAttempting to assign a value to 'for' (a reserved keyword)...")
try:
    exec("for = 4")  # This simulates using 'for' as a variable (will raise SyntaxError)
except SyntaxError:
    print("Error: 'for' is a reserved keyword in Python and cannot be used as a variable name.")

# 3. Calculate Simple Interest
# Formula: SI = (P × R × T) / 100
principal = 10000     # Principal amount in rupees
rate_of_interest = 5  # Annual rate of interest in %
time = 3              # Time in years

simple_interest = (principal * rate_of_interest * time) / 100
print("\nSimple Interest Calculation:")
print("Principal:", principal)
print("Rate of Interest:", rate_of_interest)
print("Time (years):", time)
print("Simple Interest:", simple_interest)
