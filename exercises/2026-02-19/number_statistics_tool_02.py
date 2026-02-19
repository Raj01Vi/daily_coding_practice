# Organised with the help of Chatgpt

"""
numbers = []

for _ in range(5):
    number = int(input("Enter a Number: "))
    numbers.append(number)

largest = numbers[0]
smallest = numbers[0]
total = 0
even_count = 0

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    total += num
    if num % 2 == 0:
        even_count += 1

average = total / len(numbers)

print("List is: ", numbers)
print("Largest: ", largest)
print("Smallest: ", smallest)
print(f"Average: {average:.2f}")
print("Count of even numbers: ", even_count)
"""

def get_numbers():
    numbers = []
    for _ in range(5):
        num = int(input("Enter a number: "))
        numbers.append(num)
    return numbers

def calculate_stats(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    total = 0
    even_count = 0

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

        total += num

        if num % 2 == 0:
            even_count += 1

    average = total / len(numbers)

    return largest, smallest, average, even_count

numbers = get_numbers()

largest, smallest, average, even_count = calculate_stats(numbers)

print("List:", numbers)
print("Largest:", largest)
print("Smallest:", smallest)
print(f"Average: {average:.2f}")
print("Even count:", even_count)