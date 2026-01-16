def power(a, n):
    res = 1.0
    # Работаем с абсолютным значением степени для цикла
    abs_n = abs(n)
    
    for _ in range(abs_n):
        res *= a
    
    # Если степень была отрицательной, переворачиваем дробь
    if n < 0:
        return 1 / res
    return res

# Примеры вызова:
print(power(2.0, 3))   # 8.0
print(power(2.0, -2))  # 0.25
