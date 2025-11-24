README — 34 Number-Theory Topics (with execution measurement notes)

GENERAL NOTE ABOUT MEASUREMENTS
When code for these topics runs, we measure:
- **Wall-clock time**: use `time.perf_counter()` for high-resolution elapsed time measurements.
- **Python memory allocations**: `tracemalloc` to measure allocated memory and peak usage inside the Python runtime.
- **OS-level peak memory (optional, Unix only)**: `resource.getrusage(resource.RUSAGE_SELF).ru_maxrss` returns the process resident set size.
- **Profiling (optional)**: `cProfile` or `profile` for function-level CPU profiling; `line_profiler` (third-party) for line-by-line timings.
- **External process stats (optional)**: `psutil` (third-party) for real-time RSS, CPU percentage, and I/O counters.

Important caveats:
- `tracemalloc` reports Python memory allocations (heap) and does not include memory used by C extensions or the Python interpreter itself.
- `resource.getrusage` gives OS-level peak memory but is platform dependent (Linux/macOS differences).
- Results depend heavily on hardware, OS, Python version, input size and randomness (for probabilistic algorithms). Reported time/memory should always be accompanied by the input size used for the measurement.
---

1) factorial(n)
Calculates n! = 1×2×...×n. Implementation uses an iterative or math.gamma approach. Time complexity: O(n) multiplications; memory minimal (O(1)). Measurement: small CPU time for common inputs; use `time.perf_counter()` and `tracemalloc` to show allocations only if big integers grow very large.

2) is_palindrome(n)
Checks if decimal string equals its reverse. Time: O(d) where d = digits; memory: O(d) for string. Measurement: trivial; use `time.perf_counter()`.

3) mean_of_digits(n)
Average of decimal digits. Time: O(d); memory: O(d) for digit extraction. Measurement method same as above.

4) digital_root(n)
Repeated digit sums until single digit. Time: O(d * iterations) but typically small; memory: O(1) auxiliary. Measurements: show iterations count and elapsed time.

5) is_abundant(n)
Sum proper divisors and compare to n. Naive divisor enumeration is O(sqrt(n)). For many queries, use sieve-based precomputation or prime factorization to compute divisor sums faster. Measuring: show time for a single input and optionally amortized cost per range using precomputation.

6) is_deficient(n)
Same as abundant; uses aliquot sum.

7) is_harshad(n)
Compute digit sum and test divisibility. Time O(d). Memory negligible. Measurement trivial.

8) is_automorphic(n)
Square n and compare trailing digits. Time depends on multiplication of large integers; for big n, multiplication cost matters (use Python big-int multiplication; complexity ~ O(M(n))). Measure both time and peak allocation for very large n.

9) is_pronic(n)
Check integer square root and test x(x+1) == n. Time O(1) for arithmetic and sqrt; measurement trivial.

10) prime_factors(n)
Trial division: O(sqrt(n)). Faster methods: Pollard's Rho (probabilistic). Memory: small; measurement for large n includes time spent in random cycles. Use `tracemalloc` and `time.perf_counter()`.

11) count_distinct_prime_factors(n)
Derived from prime factorization; cost dominated by factorization.

12) is_prime_power(n)
Test exponents up to log2(n) and primality checks for bases. Use integer roots, then fast primality (Miller–Rabin) to check base. Measurement: show exponent loop iterations and time.

13) is_mersenne_prime(p)
Compute M = 2^p - 1 and test primality. For large p use Lucas–Lehmer test (deterministic for Mersenne numbers). Measurement: report iterations and peak memory when working with big M.

14) twin_primes(limit)
Find primes up to limit (sieve of Eratosthenes recommended). Time: O(limit log log limit); memory: O(limit) for the sieve bit-array. Measure sieving time and peak memory; `tracemalloc` may not track all array memory, so use `resource` or `psutil` for total RSS if needed.

15) count_divisors(n)
Compute from prime factorization: if n = ∏ p_i^{e_i} then d(n) = ∏ (e_i + 1). Cost: factorization cost; measurement accordingly.

16) aliquot_sum(n)
Sum proper divisors; methods same as above. For ranges, precompute divisor sums using modified sieve (O(limit log limit)).

17) are_amicable(a, b)
Compute aliquot_sum for both numbers and compare; measurement shows two divisor-sum computations.

18) multiplicative_persistence(n)
Repeatedly multiply digits until single-digit. Time proportional to number of iterations and digits processed; memory minimal. Measurement: log the sequence length and elapsed time.

19) is_highly_composite(n)
Naive test: compare divisor counts for all smaller integers — expensive (O(n sqrt(n))). Practical approach: generate highly composite numbers using known multiplicative structure or check only known candidates. Measurement: show that naive approach is slow for large n and provide timings.

20) mod_exp(base, exponent, modulus)
Binary exponentiation: O(log exponent) multiplications. Constant memory. Critical in cryptography. Measurement: time scales with bit-length of exponent and modulus; use `time.perf_counter()` and optionally `cProfile` for hotspots.

21) mod_inverse(a, m)
Extended Euclidean algorithm: O(log m) time. Measurement trivial except for very large integers.

22) crt(remainders, moduli)
Chinese Remainder Theorem solver: multiplications and modular inverses; time dominated by modular inverses and multiprecision arithmetic. Measurement: show runtime for sets of congruences and memory for intermediate big integers.

23) is_quadratic_residue(a, p)
Compute using Euler’s criterion: a^{(p-1)/2} mod p, O(log p) exponentiation. Measurement: time for modular exponentiation.

24) order_mod(a, n)
Compute powers until 1 or use factorization of φ(n) for faster computation. Measurement: worst-case may iterate up to φ(n) steps — report runtime and note dependence on φ(n).

25) is_fibonacci_prime(n)
Two checks: Fibonacci membership (using 5n^2 ± 4 check) and primality (Miller–Rabin). Measurement: show time for primality test on candidate values.

26) lucas_sequence(n)
Linear generation: O(n) additions. Memory O(n) if storing sequence. Measurement: elapsed time and memory for large n.

27) is_perfect_power(n)
Try exponent bounds and integer root tests; use fast integer-power checks. Measurement: time vs. n size.

28) collatz_length(n)
Iterate Collatz map until 1. Time depends on trajectory length; measurement: report steps and elapsed time. For large n, store intermediate results in memoization dict (memory tradeoff).

29) polygonal_number(s, n)
Closed-form formula O(1) arithmetic. Measurement unnecessary beyond trivial timing.

30) is_carmichael(n)
Carmichael detection: Korselt's criterion requires factorization and checks on (p-1)|(n-1) for each prime factor p. Alternatively test with many coprime bases. Measurement: include factorization time.

31) is_prime_miller_rabin(n, k)
Probabilistic test with k rounds. Each round does modular exponentiation O(log n). Measurement: show failure/success time and note probabilistic nature and error bounds O(4^{-k}) approximately.

32) pollards_rho(n)
Probabilistic factorization; typical runtime sub-exponential for many composites. Measurement: report found factor, iterations, elapsed time and peak memory for large n.

33) zeta_approx(s, terms)
Partial sum ∑ 1/n^s. Time O(terms). Measurement: time scales linearly with terms; memory minimal if computed in streaming fashion. For better convergence, use acceleration techniques (Euler–Maclaurin) — note these in the README.

34) partition_function(n)
Dynamic programming DP approach: O(n^2) time and O(n) memory for naive DP. Faster asymptotic algorithms exist (Hardy–Ramanujan asymptotic formula, pentagonal theorem recurrence). Measurement: include sample runtimes for moderate n and memory usage.

---

USAGE SUGGESTIONS FOR CODE BENCHMARKS
1. Always record input sizes (e.g., n=10^6 or bits=2048) next to time/memory numbers.
2. Use multiple runs and report median/mean and standard deviation.
3. For memory reporting, combine `tracemalloc` (Python allocations) with `resource` (OS RSS) or `psutil` for more complete measurements.
4. Use `time.perf_counter()` for wall-clock and `time.process_time()` to measure CPU time excluding sleep.
5. For cryptographic-size integers, prefer deterministic algorithms where available (e.g., Lucas–Lehmer for Mersenne) and be explicit about randomness seeds for reproducibility when using probabilistic algorithms (Pollard's Rho, Miller–Rabin).

---

End of README.
