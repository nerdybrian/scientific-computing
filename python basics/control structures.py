def classify_number(num):
    """Classify a number as even or odd."""
    return "even" if num % 2 == 0 else "odd"

# 1. Asking the user for an integer input and checking if it's even or odd
try:
    user_input = int(input("Enter an integer: "))
    print(f"The number {user_input} is {classify_number(user_input)}.")
except ValueError:
    print("Invalid input. Please enter an integer.")

# 2. Using a for loop to generate even numbers from 1 to 50
even_numbers = [num for num in range(1, 51) if num % 2 == 0]
print("\nEven numbers from 1 to 50:", even_numbers)

# 3. Using a while loop to print numbers from 10 down to 1
print("\nCountdown from 10 to 1:")
count = 10
while count >= 1:
    print(count, end=" ")
    count -= 1
print()  # For a newline after countdown
