"""Independent finite check of No.54 proof without permutations or sec/tan calculus.

Uses simplex beta integrals and exact polynomial transfer recurrence.
Independently computes Euler numbers from Entringer's triangular recurrence.
Standard library only. 2026-11-05, independent adversarial check.
"""
from fractions import Fraction as Q
from math import factorial, comb

MAX_N = 22

def poly_transfer(coeff):
    # Polynomial representation of Uf(t)= integral_0^{1-t} f(s) ds
    out = [Q(0)] * (len(coeff) + 1)
    for i,c in enumerate(coeff):
        for k in range(i+2):
            out[k] += c * Q((-1)**k * comb(i+1,k),i+1)
    return out

F = [[Q(1)]]
for k in range(MAX_N-2):
    F.append(poly_transfer(F[-1]))

# Euler secant/tangent numbers from Entringer triangle, not from EGF A'=...
rows = [[1]]
E = [1]
for n in range(1,MAX_N+2):
    a = [0]*(n+1)
    for k in range(1,n+1):
        a[k] = a[k-1] + rows[-1][n-k]
    rows.append(a)
    E.append(a[-1])

def mark_integral(Fleft,Fright):
    # Dirichlet integral on u,v>=0, u+v<=1:
    # int u^i v^j (1-u-v) du dv = i! j!/(i+j+3)!
    return sum((c*d*Q(factorial(i)*factorial(j),factorial(i+j+3))
                for i,c in enumerate(Fleft) for j,d in enumerate(Fright)),Q(0))

for n in range(3,MAX_N+1):
    # Adjacent u_j,u_{j+1}, m=n-1, remaining n-3 coordinates.
    h = sum((mark_integral(F[l],F[n-3-l])
             for l in range(n-2)),Q(0))
    observed = h * factorial(n)
    predicted = E[n+1]-2*E[n]
    assert observed.denominator == 1
    assert observed == predicted,(n,observed,predicted)
    if n in (3,4,5,6,7,10,15,22):
        print(f'PASS n={n}: independent simplex DP N321={predicted}')
print(f'PASS: all n=3..{MAX_N} match, no shared core recurrence or original verifier')
