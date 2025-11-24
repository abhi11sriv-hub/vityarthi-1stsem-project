#code1

def count_distinct_prime_factors(n):
    if n < 2:
        raise ValueError
    
    count = 0
    temp = n
    

    if temp % 2 == 0:
        count += 1
        while temp % 2 == 0:
            temp //= 2
    

    factor = 3
    while factor * factor <= temp:
        if temp % factor == 0:
            count += 1
            while temp % factor == 0:
                temp //= factor
        factor += 2
    
    if temp > 1:
        count += 1
    
    return count
print(count_distinct_prime_factors(2310)) 


#code2

def is_prime_power(n):
    
    if n < 2:
        raise ValueError("Input must be a positive integer greater than 1")
    
    max_exponent = n.bit_length()  
    for k in range(1, max_exponent + 1):
        
        root = round(n ** (1 / k))
        
    
        for candidate in [root - 1, root, root + 1]:
            if candidate < 2:
                continue
            power = candidate ** k
            if power == n and is_prime(candidate):
                return True
    
    return False

def is_prime(num):
    
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
print(is_prime_power(27)) 


#code3

def is_mersenne_prime(p):

    if p < 2:
        raise ValueError("Input p must be at least 2")
    
    mersenne = 2**p - 1
    
    known_mersenne_primes = {2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127}
    if p in known_mersenne_primes:
        return True
    
    return is_prime_mersenne(mersenne)

def is_prime_mersenne(n):
   
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(n**0.5) + 1
    
    k = 1
    divisor = 2 * k * (n.bit_length()) + 1  
    
    while divisor <= limit:
        if n % divisor == 0:
            return False
        k += 1
        divisor = 2 * k * (n.bit_length()) + 1
    
    return True
print(is_mersenne_prime(7))


#code4

def twin_primes(limit):
    

    if limit < 3:
        raise ValueError("Limit must be at least 3")
    
    
    primes = sieve_of_eratosthenes(limit)
    
    
    twin_pairs = []
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            twin_pairs.append((primes[i], primes[i + 1]))
    
    return twin_pairs

def sieve_of_eratosthenes(n):
   
    if n < 2:
        return []
    
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i : n+1 : i] = [False] * len(sieve[i*i : n+1 : i])
    
    return [i for i, is_prime in enumerate(sieve) if is_prime]
print("Twin primes up to 20:")
print(twin_primes(20))


#code5

def count_divisors(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    if n == 1:
        return 1
    
    count = 1  
    i = 2
    while i * i <= n:
        if n % i == 0:

            if i * i == n:
                count += 1  
            else:
                count += 2  
        i += 1
    
    return count + 1
print(f"d(12) = {count_divisors(12)}")