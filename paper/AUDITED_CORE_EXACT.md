## 1. Definitions and claimed theorem

Let `A_n = Av_n(123,231,312)` be the set of length-`n` permutations avoiding the three indicated **consecutive** patterns. Let `E_n` be the Euler up/down (zigzag) numbers characterized by

`A(z) = sum_{n>=0} E_n z^n / n! = sec(z)+tan(z)`.

Let `N_n(p)` be the sum of the numbers of consecutive occurrences of pattern `p` over **all** permutations in `A_n`, counting each location separately.

**Theorem (independent AI mathematical audit reported PASS; novelty not established).** For every integer `n >= 3`,

1. `|A_n| = n E_{n-1}` (known, included only as a cross-check).
2. `N_n(321) = E_{n+1} - 2 E_n`.
3. `N_n(132) = N_n(213) = ((n-2)n E_{n-1} - E_{n+1} + 2 E_n)/2`.
4. Using the original paper's normalization `pop(p)=lim N_n(p)/(n|A_n|)`, whenever the limit is evaluated:
   `pop(321)=4/pi^2`, `pop(132)=pop(213)=1/2-2/pi^2`.

Since `pi` is transcendental, the three limits above are irrational (indeed transcendental, since a nonzero rational affine transform of a transcendental number is transcendental).

## 2. Uniform real variables and circular differences

Let `x_1,...,x_n` be independent `Unif(0,1)` random variables. Almost surely they are distinct, and their rank permutation is uniformly distributed on `S_n`. Define

`u_j = {x_j - x_{j+1}}`, for `1<=j<=n-1`,

where braces denote fractional part in `[0,1)`.

The map `(x_1,...,x_n) -> (x_1,u_1,...,u_{n-1})` is an invertible triangular group transformation on the torus modulo one, preserving normalized Lebesgue measure. Therefore the anchor `x_1` and all `u_j` are mutually independent `Unif(0,1)` random variables. Conditional on the entire `u` vector, each `x_j` is uniform on `[0,1)`.

**Local equivalence:** for any triple of distinct reals `x_j,x_{j+1},x_{j+2}`, the associated rank pattern is in `{132,213,321}` if and only if `u_j+u_{j+1}<1`. The other three patterns `{123,231,312}` correspond to `u_j+u_{j+1}>1`. Equality occurs only on a measure-zero set.

Indeed, the three positions on the circle are `x_j`, `{x_j-u_j}`, and `{x_j-u_j-u_{j+1}}`. When `u_j+u_{j+1}<1`, the rank pattern is `321` precisely when `x_j >= u_j+u_{j+1}`, a conditional event of probability `1-u_j-u_{j+1}`.

Write `m=n-1`, `Omega_m={u in [0,1]^m: u_j+u_{j+1}<1 for j=1,...,m-1}`. It follows that

`|A_n|/n! = int_{Omega_{n-1}} 1 du`, and

`N_n(321)/n! = int_{Omega_{n-1}} [sum_{j=1}^{n-2}(1-u_j-u_{j+1})] du`.

**Audit checkpoint A:** Independently verify the torus measure-preserving change of variables, the six-pattern case split, and the weight `1-u_j-u_{j+1}`. All later equations depend on this step.

## 3. Resolvent and Euler EGF

Define the integral operator on continuous functions

`(Uf)(t)=int_0^{1-t} f(s) ds`

and its resolvent applied to `1` as a power series

`F(z,t)=sum_{k>=0} z^k (U^k 1)(t)`.

Initially the series converges for `|z|<1`, which suffices to justify term-by-term integration and differentiation in `t` locally near `z=0`. The identity `F=1+zUF` gives

`dF(z,t)/dt = -z F(z,1-t)`, `F(z,1)=1`, and `d^2F/dt^2 = -z^2 F`.

Solving yields

`F(z,t)=A(z)cos(zt)-sin(zt)`,

where `A(z)=(1+sin z)/cos z = sec z+tan z`, since `F(z,1)=1`.

For `m>=1`, the integral `int_{Omega_m} 1 du = int_0^1 (U^{m-1}1)(t)dt`. Consequently

`sum_{m>=1} z^m vol(Omega_m) = z int_0^1 F(z,t)dt = F(z,0)-1 = A(z)-1`.

Coefficient comparison yields `vol(Omega_m)=E_m/m!`, and hence the known `|A_n|=n E_{n-1}`.

**Audit checkpoint B:** Check both boundary conditions, the series index `m=n-1`, and the normalizing `n!`.

## 4. Marking a 321 occurrence and the exact EGF

Set

`J(z)=int_0^1 int_0^{1-u} (1-u-v) F(z,u)F(z,v) dv du`.

Choosing a marked adjacent pair `u_j,u_{j+1}` in an admissible chain `u_1,...,u_{n-1}`, the chain on either side of that edge contributes powers of `U`. Thus the product of the two `F` factors enumerates all left/right extensions. Since the two marked variables contribute `z^2`, while the original occurrence-count EGF is indexed by permutation length `n=m+1`, we get the **crucial shift**

`H(z):=sum_{n>=3} N_n(321) z^n/n! = z^3 J(z)`.

The following algebra evaluates the integral exactly. From `F(z,t)=1+z int_0^{1-t}F(z,s)ds`, first obtain

`z int_0^{1-u} (1-u-v)F(z,v)dv = int_u^1 (F(z,y)-1)dy`.

Therefore, interchanging integration order,

`J(z) = (1/z) int_0^1 F(z,u) int_u^1(F(z,y)-1)dy du`

`     = (1/z) int_0^1 (F(z,y)-1) int_0^y F(z,u)du dy`

`     = (1/z^2) int_0^1 (F(z,y)-1)(F(z,1-y)-1)dy`.

Use `F_y(z,y)=-z F(z,1-y)`, `F(z,0)=A(z)`, `F(z,1)=1`, and `z int_0^1F(z,y)dy=A(z)-1`. Then

`z^3 J(z) = -int_0^1 (F-1) F_y dy - z int_0^1(F-1)dy`

`          = (A-1)^2/2 - (A-1) + z`

`          = (A^2-4A+3)/2 + z`.

Finally `A'=(A^2+1)/2`, as follows by differentiating `sec z+tan z`. Therefore

`H(z)=A'(z)-2A(z)+1+z`.

The coefficients of `z^0,z^1,z^2` are zero. Comparing the coefficient of `z^n/n!` for every `n>=3` proves

`N_n(321) = E_{n+1}-2E_n`.

**Audit checkpoint C:** The most important possible failure points are the `z^3` shift in `H`, swapping integrals, and the last integration by parts. Check each separately, without relying on numerical data.

## 5. The two other allowed patterns

Reverse-complement (`R o C`) fixes the forbidden set `{123,231,312}` (it fixes `123` and swaps `231` and `312`), and exchanges the permitted patterns `132` and `213`, while fixing `321`. Hence `N_n(132)=N_n(213)` exactly for all `n`.

Every admissible permutation contributes `n-2` consecutive triples, all in `{132,213,321}`; therefore

`N_n(132)+N_n(213)+N_n(321) = (n-2)|A_n|`.

Combining this relation with the established expression for `N_n(321)` proves claim 3.

## 6. Asymptotic normalization (important correction)

Hassler–Kirgizov (arXiv:2511.02442v2, their Eq. (1.1)) use `n|A_n|` as the denominator in their definition of `pop`. The alternative `(n-2)|A_n|` is a natural normalization over actual length-three windows but differs at finite `n`; both have the same limit.

The standard asymptotic of Euler zigzag numbers is

`E_n/n! ~ 2(2/pi)^(n+1)`.

Hence, using `|A_n|=nE_{n-1}`,

`N_n(321)/(n|A_n|) = (E_{n+1}-2E_n)/(n^2 E_{n-1}) -> 4/pi^2`.

The other two limits follow from symmetry and the sum of `(n-2)|A_n|` windows. This gives both a solution candidate for their open Class 12 and an irrational asymptotic popularity example.

## 7. Independent arithmetic checking

Run accompanying `No54_v0.1_VERIFY_20261105.py` with standard-library Python 3.10+; it builds Euler numbers using a recurrence and separately brute-forces all permutations for `3<=n<=9`. It checks the avoidance-set count, each allowed-pattern count, and the exact formulas. Additional values for `n=10,20,40,60,100,120` are generated by exact integer arithmetic. These computations do **not** replace proof or external review.

