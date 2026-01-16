def is_prime(n):
    """Проверка числа на простоту."""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_numbers_with_three_divisors(start, end):
    """
    Ищет числа в диапазоне, имеющие ровно 3 делителя (не считая 1 и самого числа).
    Такие числа имеют вид p^4, где p - простое число.
    """
    results = []
    
    # Чтобы p^4 попало в [start, end], 
    # p должно быть в пределах от start^(1/4) до end^(1/4)
    p_min = int(start**0.25)
    p_max = int(end**0.25) + 1
    
    for p in range(p_min, p_max + 1):
        if is_prime(p):
            n = p**4
            if start <= n <= end:
                # Делители кроме 1 и n: p, p^2, p^3
                # Нам нужны наименьший (p) и наибольший (p^3)
                results.append((p, p**3))
    
    return results

# Запуск программы
start_range = 81234
end_range = 134689

found = find_numbers_with_three_divisors(start_range, end_range)

print("Наименьший | Наибольший")
print("-" * 23)
for low, high in found:
    print(f"{low:<10} | {high}")
