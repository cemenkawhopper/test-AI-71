#задание 3
import random
# Функция для генерации случайных чисел и вычисления суммы и произведения
def generate_random_numbers(n, low=1, up=100):

    random_numbers = [random.randint(low, up) for _ in range(n)]
    total_sum = sum(random_numbers)

    return random_numbers, total_sum,



n = int(input("Введите количество случайных чисел: "))
random_numbers, total_sum,= generate_random_numbers(n)

print(f"Случайные числа: {random_numbers}")
print(f"Сумма: {total_sum}")

