#code1

def lucas_sequence(n):
   
    if n <= 0:
        return  
    a, b = 2, 1

   
    if n >= 1:
        yield a
    
    
    if n >= 2:
        yield b

    
    for _ in range(2, n):
        c = a + b
        yield c
        a, b = b, c

n_terms = 10
lucas_gen = lucas_sequence(n_terms)

print(f"The first {n_terms} Lucas numbers are:")

print(list(lucas_gen))


#code2

def is_perfect_power(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    
    max_a = int(n**0.5)
    
    for a in range(2, max_a + 1):
        if n % a == 0:
            power = a * a
            while power <= n:
                if power == n:
                    return True
                power = power * a
                
    return False


print(f"Is 8 a perfect power? {is_perfect_power(8)}")


#code3

def collatz_length(n):
    if n < 1:
        return 0

    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    
    return steps

start_num = 6
print(f"The Collatz sequence length for {start_num} is: {collatz_length(start_num)}")


#code4

def polygonal_number(s, n):
   
    if s < 3 or n < 1:
        return None  

    numerator = (s - 2) * (n ** 2) - (s - 4) * n
    
  
    return numerator // 2


print(f"The 5th 3-gonal (triangular) number is: {polygonal_number(3, 5)}")


#code5

def _is_prime(n):

    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def _get_prime_factors(n):
   
    factors = set()
    
   
    if n % 2 == 0:
        factors.add(2)
        while n % 2 == 0:
            n //= 2
            
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.add(i)
            while n % i == 0:
                n //= i
        i += 2
        
  
    if n > 2:
        factors.add(n)
        
    return factors

def is_carmichael(n):
   
   
    if n < 2 or _is_prime(n):
        return False
        
    factors = _get_prime_factors(n)
    
   
    product_of_factors = 1
    for p in factors:
        product_of_factors *= p
        
    if product_of_factors != n:
        return False
        
    
    for p in factors:
        if (n - 1) % (p - 1) != 0:
            return False