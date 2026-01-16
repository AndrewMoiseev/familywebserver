def get_divisors_info(n):
    """
    Находит все делители числа n (кроме 1 и n).
    Возвращает кортеж (количество, сумма).
    """
    divisors_sum = 0
    divisors_count = 0
    
    # Итерируемся от 2 до квадратного корня из n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i * i == n:
                # Если число — идеальный квадрат (делители совпали)
                divisors_sum += i
                divisors_count += 1
            else:
                # Добавляем сразу пару делителей
                divisors_sum += i + (n // i)
                divisors_count += 2
                
    return divisors_count, divisors_sum

def solve():
    start = 135790
    end = 163228
    threshold = 460000
    
    # Шапка таблицы
    print(f"{'Число':<10} | {'Кол-во делителей':<18} | {'Сумма'}")
    print("-" * 45)
    
    for num in range(start, end + 1):
        count, d_sum = get_divisors_info(num)
        
        if d_sum > threshold:
            print(f"{num:<10} | {count:<18} | {d_sum}")

if __name__ == "__main__":
    solve()
