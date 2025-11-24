#code1

import math

def is_deficient(n):
    
    if n <= 0:
        return False
        
    sum_of_divisors = 1  
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            sum_of_divisors += i
            if i * i != n:
                sum_of_divisors += n // i
    
    return sum_of_divisors < n

        
          
print(is_deficient(6))
print(is_deficient(8))
print(is_deficient(95))


#code2

def is_harshad(n):
  
  if n <= 0:  
    return False

  sum_of_digits = 0
  x = n
  while x > 0:
    sum_of_digits += x % 10  
    x //= 10  

 
  return n % sum_of_digits==0


print(is_harshad(12))
print(is_harshad(15))


#code3

def is_automorphic(n):

    if n < 0:
        print("Enter positive number")

    square = n * n
  
  
    x = str(n)
    y = str(square)

  
    if y.endswith(x):
        return True
    else:
        return False
        

print(is_automorphic(1))
print(is_automorphic(12))
print(is_automorphic(6))


#code4

import math

def is_pronic(n):
   
    
    if n < 0:
        return False  
    
    
    for i in range(0,n): 
        if i * (i + 1) == n:
            return True
    else:
        return False

print(is_pronic(6))
print(is_pronic(4))
print(is_pronic(42))
print(is_pronic(30))


#code5

def prime_factors(n):

    
    i = 2

    while i * i <= n:
      while n % i == 0:
        print(i)
        n //= i
      i += 1

    if n > 1:
        print(n)

      
print(prime_factors(35))
print(prime_factors(315))
print(prime_factors(6))
print(prime_factors(18))