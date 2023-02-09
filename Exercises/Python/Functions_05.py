import random

def random_list_summer(numbers = []):
    while len(numbers) <= 15:
        numbers.append(random.randint(-100, 100))
    print(f"The random list is {numbers} and the sum of its values is {sum(numbers)}")

random_list_summer()