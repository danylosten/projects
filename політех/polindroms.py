import random

random_numbers = [random.randint(1, 1000) for _ in range(5)]
print("Випадкові числа:", random_numbers)
def is_palindrome(number):
    return str(number) == str(number)[::-1]
palindromes = [num for num in random_numbers if is_palindrome(num)]
if palindromes:
    print("Числа-паліндроми:", palindromes)
else:
    print("Паліндромів немає")