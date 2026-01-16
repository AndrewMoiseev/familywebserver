def power(a, n):
    # Базовый случай: остановка рекурсии
    if n == 0:
        return 1
    
    # Обработка отрицательной степени
    if n < 0:
        return 1 / power(a, -n)
    
    # Рекурсивный шаг
    return a * power(a, n - 1)

# Тесты
print(power(2, 10))    # 1024
print(power(5, -2))    # 0.04
print(power(1.5, 2))   # 2.25
