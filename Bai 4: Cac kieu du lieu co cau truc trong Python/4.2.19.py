print ("Họ tên: Phan Thế Đạt")
print ("MSSV: 235752021610094")

def sieve_of_eratosthenes(limit):
    is_prime = [True] * limit
    is_prime[0], is_prime[1] = False, False  
    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            for multiple in range(number * number, limit, number):
                is_prime[multiple] = False
    prime_numbers = tuple(num for num, prime in enumerate(is_prime) if prime)
    return prime_numbers

limit = 1000000

prime_tuple = sieve_of_eratosthenes(limit)

print(f"Có tổng cộng {len(prime_tuple)} Số nguyên tố nhỏ hơn 1 triệu.")
print(f"các số nguyên tố đầu tiên là: {prime_tuple[:10]}") 
