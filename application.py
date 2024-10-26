print("Welcome to the Sum Calculator!")
total = 0

while True:
    user_input = input("Enter a number (or type 'done' to finish): ")

    if user_input.lower() == 'done':
        break
        
    try:
        number = float(user_input)
        total += number
    except ValueError:
        print("Please enter a valid number.")

print(f"The total sum is: {total}")
