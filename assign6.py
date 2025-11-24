#code1

import time
import tracemalloc

def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return old_r, old_s, old_t   

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None              
    return x % m                 

a = 3
m = 11

print(f"\nFinding modular inverse of {a} mod {m}...\n")
tracemalloc.start()
t0 = time.perf_counter()

inverse = mod_inverse(a, m)

elapsed = time.perf_counter() - t0
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

if inverse is None:
    print(f"No modular inverse exists because gcd({a}, {m}) ≠ 1.")
else:
    print(f"Modular Multiplicative Inverse: {inverse}")
    print(f"Check: ({a} * {inverse}) % {m} = {(a * inverse) % m}")

print("\n--- Performance Stats ---")
print(f"Time taken        : {elapsed:.8f} seconds")
print(f"Memory (current)  : {current} bytes")
print(f"Memory (peak)     : {peak} bytes")



#code2

import time
import tracemalloc
import math
from typing import List, Optional, Tuple


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t


def mod_inverse(a: int, m: int) -> Optional[int]:
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None
    return x % m


def pairwise_coprime(moduli: List[int]) -> bool:
    n = len(moduli)
    for i in range(n):
        for j in range(i + 1, n):
            if math.gcd(moduli[i], moduli[j]) != 1:
                return False
    return True


def crt(remainders: List[int], moduli: List[int]) -> Tuple[Optional[int], Optional[int], dict]:
    if len(remainders) != len(moduli) or len(moduli) == 0:
        raise ValueError("remainders and moduli must be non-empty lists of the same length.")

    if not pairwise_coprime(moduli):
        return None, None, {"error": "Moduli are not pairwise coprime."}

    M = 1
    for m in moduli:
        if m <= 0:
            return None, None, {"error": f"Invalid modulus {m}; moduli must be positive integers."}
        M *= m

    debug = {"M": M, "terms": []}
    total = 0

    for i, (r_i, m_i) in enumerate(zip(remainders, moduli)):
        M_i = M // m_i                        
        inv = mod_inverse(M_i, m_i)          
        if inv is None:
            return None, M, {"error": f"No inverse for M_i mod m_i (i={i}): gcd({M_i}, {m_i}) != 1"}
        term = (r_i * M_i * inv) % M          
        debug["terms"].append({
            "index": i,
            "r_i": r_i,
            "m_i": m_i,
            "M_i": M_i,
            "inv_Mi_mod_mi": inv,
            "term_mod_M": term
        })
        total = (total + term) % M

    result = total % M
    return result, M, debug


def human_readable_bytes(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024.0:
            return f"{n:.0f} {unit}"
        n /= 1024.0
    return f"{n:.2f} TB"


if __name__ == "__main__":
    remainders = [2, 3, 2]   # r1, r2, r3
    moduli      = [3, 5, 7]  # m1, m2, m3

    print("Solving the system of congruences:")
    for r, m in zip(remainders, moduli):
        print(f"  x ≡ {r} (mod {m})")
    print("\n------------------------------\n")

    tracemalloc.start()
    t0 = time.perf_counter()

    result, M, debug = crt(remainders, moduli)

    elapsed = time.perf_counter() - t0
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    if result is None:
        print("CRT failed:")
        if debug and "error" in debug:
            print("  Error:", debug["error"])
        else:
            print("  Unknown error.")
    else:
        print(f"The unique solution is: x ≡ {result} (mod {M})\n")
        print("Verification (each congruence):")
        for t in debug["terms"]:
            idx = t["index"]
            r_i = t["r_i"]
            m_i = t["m_i"]
            check = result % m_i
            print(f"  eq {idx+1}: x % {m_i} = {check}  (expected {r_i})")

        print("\nComputation details (per term):")
        for t in debug["terms"]:
            print(f"  i={t['index']}: r_i={t['r_i']}, m_i={t['m_i']}, M_i={t['M_i']}, inv={t['inv_Mi_mod_mi']}, term={t['term_mod_M']}")

    print("\n--- Performance ---")
    print(f"Time elapsed       : {elapsed:.8f} seconds")
    print(f"Memory (current)   : {current} bytes ({human_readable_bytes(current)})")
    print(f"Memory (peak)      : {peak} bytes ({human_readable_bytes(peak)})")


#code3

import time
import tracemalloc

def modular_pow(base, exponent, modulus):
    """Efficient modular exponentiation (repeated squaring)."""
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:     
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result


def quadratic_residue_check(a, p):
    """Return True if 'a' is a quadratic residue modulo prime 'p'."""
    if p <= 2 or p % 2 == 0:
        raise ValueError("Modulus p must be an odd prime.")

    a = a % p
    if a == 0:
        return True                     

    exponent = (p - 1) // 2
    result = modular_pow(a, exponent, p)

    if result == 1:
        return True
    elif result == p - 1:
        return False
    else:
        print("Warning: Unexpected Euler result.")
        return False

a = 10
p = 13
print(f"\nChecking if {a} is a quadratic residue modulo {p}...\n")

tracemalloc.start()
t0 = time.perf_counter()

try:
    is_residue = quadratic_residue_check(a, p)
except Exception as e:
    elapsed = time.perf_counter() - t0
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Error: {e}")
    print(f"Time elapsed: {elapsed:.8f} seconds")
    print(f"Memory current: {current} bytes")
    print(f"Memory peak:    {peak} bytes")
    exit()

elapsed = time.perf_counter() - t0
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

if is_residue:
    print(f"Result: {a} *is* a Quadratic Residue modulo {p}.")
    print(f"A solution to x² ≡ {a} (mod {p}) exists.\n")
else:
    print(f"Result: {a} is a Quadratic NON-Residue modulo {p}.")
    print(f"No solution to x² ≡ {a} (mod {p}) exists.\n")

print("--- Performance ---")
print(f"Time elapsed     : {elapsed:.8f} seconds")
print(f"Memory (current) : {current} bytes")
print(f"Memory (peak)    : {peak} bytes")
print()


#code4

import time
import tracemalloc
import math
from typing import Optional, List, Tuple, Dict

def prime_factorization(n: int) -> Dict[int, int]:
    """Return prime factorization of n as {prime: exponent} using trial division."""
    factors = {}
    x = n
    while x % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        x //= 2
    f = 3
    maxf = int(math.isqrt(x)) + 1
    while f <= maxf and x > 1:
        while x % f == 0:
            factors[f] = factors.get(f, 0) + 1
            x //= f
            maxf = int(math.isqrt(x)) + 1
        f += 2
    if x > 1:
        factors[x] = factors.get(x, 0) + 1
    return factors


def euler_phi(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    factors = prime_factorization(n)
    result = n
    for p in factors:
        result = result // p * (p - 1)
    return result


def divisors(n: int) -> List[int]:
    if n <= 0:
        return []
    pf = prime_factorization(n)
    divs = [1]
    for p, exp in pf.items():
        new_divs = []
        for e in range(1, exp + 1):
            mul = p ** e
            for d in divs:
                new_divs.append(d * mul)
        divs += new_divs
    return sorted(set(divs))

def multiplicative_order(a: int, n: int) -> Tuple[Optional[int], Dict]:
    debug = {"a": a, "n": n}

    g = math.gcd(a, n)
    debug["gcd"] = g
    if g != 1:
        return None, debug

    phi = euler_phi(n)
    debug["phi(n)"] = phi

    divs = divisors(phi)
    debug["divisors_of_phi"] = divs

    for d in divs:
        if pow(a, d, n) == 1:
            debug["found_d"] = d
            return d, debug
    return None, debug

if __name__ == "__main__":
    a = 2
    n = 15

    print(f"Finding multiplicative order of {a} modulo {n}...\n")

    tracemalloc.start()
    t0 = time.perf_counter()

    order, info = multiplicative_order(a, n)

    elapsed = time.perf_counter() - t0
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    if order is None:
        if info.get("gcd", None) != 1:
            print(f"Result: Order does NOT exist because gcd({a}, {n}) = {info['gcd']} ≠ 1.")
        else:
            print("Result: No order found (unexpected). Debug info:", info)
    else:
        print(f"Result: The multiplicative order of {a} modulo {n} is k = {order}.")
        print(f"Check: pow({a}, {order}, {n}) = {pow(a, order, n)}  (should be 1)\n")

        print("Extra info:")
        print(f"  gcd({a},{n}) = {info['gcd']}")
        print(f"  phi({n}) = {info['phi(n)']}")
        print(f"  divisors of phi(n) (checked): {info['divisors_of_phi']}")
        if "found_d" in info:
            print(f"  smallest d found  = {info['found_d']}")

    def nice_bytes(x):
        for unit in ("B","KB","MB","GB"):
            if x < 1024.0:
                return f"{x:.0f} {unit}"
            x /= 1024.0
        return f"{x:.2f} TB"

    print("\n--- Performance ---")
    print(f"Time elapsed       : {elapsed:.8f} seconds")
    print(f"Memory (current)   : {current} bytes ({nice_bytes(current)})")
    print(f"Memory (peak)      : {peak} bytes ({nice_bytes(peak)})")



#code5

import time
import tracemalloc
import math

def is_prime(n: int) -> bool:
    """Simple and fast primality test for n."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_fibonacci(n: int) -> bool:
    if n < 0:
        return False
    if n in (0, 1):
        return True

    f0, f1 = 0, 1
    while f1 < n:
        f0, f1 = f1, f0 + f1
    return f1 == n

n = 13
print(f"\nChecking if {n} is a Fibonacci Prime...\n")

tracemalloc.start()
t0 = time.perf_counter()

prime_status = is_prime(n)
fib_status = is_fibonacci(n)

elapsed = time.perf_counter() - t0
current_mem, peak_mem = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Is {n} Prime?       {prime_status}")
print(f"Is {n} Fibonacci?   {fib_status}")

if prime_status and fib_status:
    print(f"\n✔ Conclusion: {n} IS a Fibonacci Prime.\n")
else:
    print(f"\n✘ Conclusion: {n} is NOT a Fibonacci Prime.\n")

def nice_bytes(x):
    for unit in ("B", "KB", "MB", "GB"):
        if x < 1024:
            return f"{x:.0f} {unit}"
        x /= 1024
    return f"{x:.2f} TB"

print("--- Performance ---")
print(f"Time elapsed     : {elapsed:.8f} seconds")
print(f"Memory (current) : {current_mem} bytes ({nice_bytes(current_mem)})")
print(f"Memory (peak)    : {peak_mem} bytes ({nice_bytes(peak_mem)})\n")


