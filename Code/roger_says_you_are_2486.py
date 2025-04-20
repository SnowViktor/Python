from math import factorial
from numpy import array

# x ∈ N₀
x = [i for i in range(7, 7 + 4 * int(input("\nlength(positive integer): ")))]


# f(x) = x! - 2^x
def f(x):
    return factorial(x) - 2**x


# u = f(x) - 10 ． ⌊ ⅒ • f(x) ⌋
u = [f(j) - 10 * (f(j) // 10) for j in x]

print(u)

# Mathematical Induction: x ≥ 7 ⇔ u = {2, 4, 8, 6}
u_cycle = [u[k : k + 4] for k in range(0, len(u), 4)]
for l in u_cycle:
    if (array(l) == array([2, 4, 8, 6])).all():
        test = True
    else:
        test = False
print(test)
