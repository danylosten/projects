# функції
#додаваня
def add(x, y):
    return x + y
# віднімання
def subtract(x, y):
    return x - y
# множення
def multiply(x, y):
    return x * y
# ділення
def divide(x, y):
    if y == 0:
        return "Ділення на нуль неможливе"
    return x / y
# вибір операції 
print("Доступні операції:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")
choice = input("Виберіть операцію (1/2/3/4): ")
# введення чисел 
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
# резульати операцій
if choice == '1':
    print("Результат:", add(num1, num2))
elif choice == '2':
    print("Результат:", subtract(num1, num2))
elif choice == '3':
    print("Результат:", multiply(num1, num2))
elif choice == '4':
    print("Результат:", divide(num1, num2))
else:
    print("Невірний вибір операції")