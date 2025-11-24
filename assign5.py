#code1

import time
st=time.perf_counter()
def aliquot_sum(n):

   
  if  n <= 0:
    return "enter a positive integer"
  
  x = 0
 
  for i in range(1, n // 2 + 1):
    if n % i == 0:
      x += i
      
  return x


st=time.perf_counter()
print(aliquot_sum(12)) 
print(aliquot_sum(6))  
print(aliquot_sum(1))   
et=time.perf_counter() 
execution_time =et-st
print("Execution time:",execution_time)


#code2

import time

def are_amicable(a,b):
     if a<0:
         return "enter a positive number"

     x=0
     for i in range (1,a//2+1):
         if a % i ==0:
             x+=i
         if x==b:
             return True

st=time.perf_counter()
print(are_amicable(84,20))
print(are_amicable(7,8))
print(are_amicable(220,284))
et=time.perf_counter()
duration=et-st
print("duration:",duration)


#code3

import time

def multiplicative_persistence(n):
    if n <10:
        return 0


    persistence=0
    number=n

    while number>=10:
        product=1
        for i in str(number):
            product *= int(i)
        number= product
        persistence += 1

    return persistence


st=time.perf_counter()
print(multiplicative_persistence(78))
print(multiplicative_persistence(888))
print(multiplicative_persistence(4))
et=time.perf_counter()
duration=et-st
print("duration:",duration)


#code4

import math
import time


def count_divisors(num):
  
    if num <= 0:
        return 0
    divisor_count = 0
    for i in range(1, int(math.sqrt(num) + 1)):
        if num % i == 0:
            if num / i == i:  
                divisor_count += 1
            else:
                divisor_count += 2
    return divisor_count

def is_highly_composite(n):
  
    if n <= 0:
        return False
        
    original_divisor_count = count_divisors(n)
    
  
    for i in range(1, n):
        if count_divisors(i) >= original_divisor_count:
            return False 
            
    return True  


st=time.perf_counter()
print(is_highly_composite(1))
print(is_highly_composite(6))
print(is_highly_composite(7)) 
et=time.perf_counter()
duration=et-st
print(f"Execution time: {duration:.6f} seconds")


#code5

import time

def mod_exp(base, exponent, modulus):
    
    if modulus == 1:
        return 0  

    result = 1
    base %= modulus  

    while exponent > 0:
        
        if exponent % 2 == 1:
            result = (result * base) % modulus

        
        base = (base * base) % modulus

       
        exponent //= 2
    

    return result



st=time.perf_counter()
base1 = 2
exponent1 = 3
modulus1 = 5
result1 = mod_exp(base1, exponent1, modulus1)
print(f"({base1}^{exponent1}) % {modulus1} = {result1}")
et=time.perf_counter()
duration=et-st
print(f"Execution time: {duration:.6f} seconds")