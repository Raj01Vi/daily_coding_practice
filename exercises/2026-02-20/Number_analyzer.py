numbers = []

while True:
    user_input = input("Enter a number (or 'done' to exit): ")

    if user_input.lower() == "done":
        break

    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("This is not a valid number. Please try again.")

if len(numbers) == 0:
    print("No numbers were entered")
else:
    print("List is: ", numbers) # list
    print("Count is: ", len(numbers)) # total count of numbers
    print("Sum is: ", sum(numbers)) # sum of numbers
    print(f"Average is: {sum(numbers) / len(numbers):.2f}") # average of numbers
    print("Smallest is: ", min(numbers)) # smallest number   
    print("Largest is: ", max(numbers)) # largest number