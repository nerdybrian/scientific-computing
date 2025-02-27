# Creating variables of different data types
int_var = 10               # Integer
float_var = 3.14           # Float
complex_var = 2 + 3j       # Complex
list_var = [1, 2, 3, 4]    # List
tuple_var = (5, 6, 7, 8)   # Tuple
dict_var = {"name": "Alice", "age": 25}  # Dictionary
set_var = {1, 2, 3, 4}     # Set
bool_var = True           # Boolean

# Printing the type of each variable
print("Data Types:")
print(f"int_var: {type(int_var)}")
print(f"float_var: {type(float_var)}")
print(f"complex_var: {type(complex_var)}")
print(f"list_var: {type(list_var)}")
print(f"tuple_var: {type(tuple_var)}")
print(f"dict_var: {type(dict_var)}")
print(f"set_var: {type(set_var)}")
print(f"bool_var: {type(bool_var)}")

# Converting int to float and float to int
int_to_float = float(int_var)
float_to_int = int(float_var)

print("\nConversions:")
print(f"Integer to float: {int_to_float}")
print(f"Float to integer: {float_to_int}")
