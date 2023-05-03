import numpy

A_wing = 74.98
L_wing = 29.90
u_air = 0.0000265
p_air = 0.64


def reynolds_number(V):
    return (V * b_wing(A_wing, L_wing))/viscosity_air(u_air, p_air)


def b_wing(A_wing, L_wing):
    return A_wing/L_wing


def viscosity_air(u_air, p_air):
    return u_air/p_air


