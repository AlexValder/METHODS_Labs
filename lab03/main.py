from sympy import *
from sympy.abc import x, t
from numpy import arange
from math import exp
from graphics import draw_graph
from typing import List

# VAR 9 - Скінченно-різницевий

# 0 <= x <= l, 0 <= t <= T
l : float = 1.0
T : float = 0.02

# (∂u)/(∂t) = a^2 (∂^2u)/(∂x^2) + b (∂u)/(∂x) + c u
a : float = 1.0
b : float = 0.0
c : float = 1.0

# α (∂u (0,t))/(∂x) + β u(0,t) = φ0(t), x = 0, t > 0
alpha : float = 0.0
beta : float = 1.0
def phi_0(t: float) -> float:
    return (t + 1)*exp(-t)

# γ (∂u (l,t))/(∂x) + 𝛿 u(l,t) = φ1(t), x = l, t > 0
gamma : float = 0.0
delta : float = 1.0
def phi_1(t: float) -> float:
    return (t + 1)*exp(1 - t)

# 
n : int = 10
m : int = 10
step : float = l / n
omega : float = 0.25
tau : float = omega * step**2 / a**2

xs : List[float] = [x for x in arange(0.0, 1.0 + step, step)]
ts : List[float] = [t*tau for t in range(m + 1)]


# u(x,0) = ψ(x), 0 <= x <= l, t = 0
def psi(x: float) -> float:
    return exp(x)

def accurate(x: float, t: float) -> float:
    return (t + 1)*exp(x - t)

if __name__ == "__main__":
    zs = [accurate(x, t) for x, t in zip(xs, ts)]

    draw_graph((xs, ts, zs, "Accurate"))