"""No.54 limited arithmetic verifier. Python 3.10+, standard library only.

Checks exact Euler-number formulas using a directly enumerated permutation class.
Does NOT substitute for a mathematical proof or independent human/AI review.
"""
from collections import Counter
from itertools import permutations
from math import comb, pi

N = 121
E = [0] * (N + 2)
E[0] = 1
for n in range(N + 1):
    numer = (1 if n == 0 else 0) + sum(comb(n, k) * E[k] * E[n-k] for k in range(n+1))
    assert numer % 2 == 0
    E[n+1] = numer // 2

FORBIDDEN = {"123", "231", "312"}

def pattern3(a, b, c):
    return ''.join(str(sorted((a,b,c)).index(v) + 1) for v in (a,b,c))

def expected(n):
    size = n * E[n-1]
    t321 = E[n+1] - 2 * E[n]
    assert ((n-2)*size - t321) % 2 == 0
    other = ((n-2)*size - t321) // 2
    return size, Counter({"321":t321, "132":other, "213":other})

for n in range(3, 10):
    actual = Counter()
    size = 0
    for perm in permutations(range(1, n+1)):
        pats = [pattern3(*perm[i:i+3]) for i in range(n-2)]
        if any(p in FORBIDDEN for p in pats):
            continue
        size += 1
        actual.update(pats)
    ex_size, ex_patterns = expected(n)
    assert size == ex_size, (n, size, ex_size)
    assert actual == ex_patterns, (n, actual, ex_patterns)
    print(f'PASS n={n}: |A_n|={size}, 321={actual["321"]}, 132=213={actual["132"]}')

print('n | normalization n*|A_n| (%) | normalization (n-2)*|A_n| (%)')
for n in (10,20,40,60,100,120):
    size, c = expected(n)
    print(f'{n:3d} | {100*c["321"]/(n*size):.6f} | {100*c["321"]/((n-2)*size):.6f}')
print(f'4/pi^2 limit: {100*4/pi**2:.6f}%')
print('ALL ARITHMETIC CHECKS PASS; PROOF AND NOVELTY STILL REQUIRE INDEPENDENT REVIEW')
