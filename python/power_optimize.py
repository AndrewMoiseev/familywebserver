def power(a, n):
    # 1. Базовый случай
    if n == 0:
        return 1
    
    # 2. Обработка отрицательной степени
    if n < 0:
        return 1 / power(a, -n)
    
    # 3. Рекурсивный шаг для четной степени
    if n % 2 == 0:
        res = power(a, n // 2)
        return res * res
    
    # 4. Рекурсивный шаг для нечетной степени
    else:
        return a * power(a, n - 1)

# Проверка
print(power(2, 10))  # Выполнит всего около 5-7 вызовов вместо 10
print(power(3, 13))  # 1594323