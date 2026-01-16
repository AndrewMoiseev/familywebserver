def solve():
    start = 190201
    end = 190280
    
    for num in range(start, end + 1):
        even_divisors = []
        
        # Находим все делители числа
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                # Проверяем первый делитель из пары
                if i % 2 == 0:
                    even_divisors.append(i)
                
                # Проверяем второй делитель из пары (если он не равен первому)
                second_div = num // i
                if second_div != i:
                    if second_div % 2 == 0:
                        even_divisors.append(second_div)
        
        # Если нашли ровно 4 чётных делителя
        if len(even_divisors) == 4:
            # Сортируем по убыванию
            even_divisors.sort(reverse=True)
            print(f"Число {num}: {even_divisors}")

if __name__ == "__main__":
    solve()
