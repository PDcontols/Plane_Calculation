import numpy
import math

# input parameters
# enviroment
u_air = 0.0000265  # air viscosity Pa*s
p_air = 0.64  # air density Kg/m3
V = 127  # flight speed m/c
# wing
A_wing = 74.98  # wing surface area m2
L_wing = 29.90  # wing length m
k_tur = 1.73
eng_amount = 2  # amount of engine on the wing
A_wing_eng = 7.7  # part of the wing area occupied by engine nacelles
c_mid_wing = 0.16  # relative thickness of wing profile
c_xa_wc = 0.0012  # rate of wing cover manufacturing
c_xa_eng = 0.0003  # rate of wing resistance with engine blowing
L_wing_wet = 26.30
l_split_flap = 8
l_split_ail = 6.1
Ka_i = 0.85
S_body = 9.3  # wing surface under/over body
# stabilizer
A_stab = 7.77
L_stab = 8.4
c_mid_stab = 0.18  # relative thickness of stabilizer profile
c_xa_stab = 0.0012  # rate of wing cover manufacturing
l_split_stab = 10.6  # gap between elevator and stabilizer
# tail
A_tail = 23.36
L_tail = 5
l_split_tail = 7  # gap between rudder and tail
c_xa_tail = 0.0012  # rate of tail cover manufacturing
#body
L_body = 23.53
n_l = 1.08
n_m_body = 1.05
S_body_air = 143.9
S_body_mid = 5.5
c_xa_body = 0.00018  # rate of body cover manufacturing
c_xa_body_eng = 0.005  # Coefficient out of engine type
#engines pods
L_eng = 7.2
n_l_eng = 1.25
n_m_eng = 1.05
S_eng_air = 31.16
S_eng_mid = 2.2
c_xa_eng = 0.00015  # rate of pods cover manufacturing


# basic functions
def reynolds_number(V, Area, Lenght):
    return (V * b_0(Area, Lenght)) / viscosity_air(u_air, p_air)


def b_0(Area, Lenght):
    return Area / Lenght


def viscosity_air(u_air, p_air):  # kinematic coefficient of air viscosity.
    return u_air / p_air


def mach_speed(V):
    return V / 320.6


def c_f0(Area, Lenght): #V
    return 0.455 / (math.pow(math.log10(reynolds_number(V, Area, Lenght)), 2.58))


def n_c(c_mid): #c_mid
    return 1 + 3.5 * c_mid


def n_m(): #V
    return 1 + 0.1 * math.pow(mach_speed(V), 2)


def k_eng(): #eng_amount, A_wing_eng, A_wing
    if eng_amount == 0:
        return 2
    else:
        return 2 - (A_wing_eng / A_wing)


def c_xa_split(l_split, Lenght):
    return 0.0017 * (l_split / Lenght)


# body
def reynolds_number_body(V, Lenght):
    return (V * Lenght) / viscosity_air(u_air, p_air)


def c_f0_body(Lenght): #V
    return 0.455 / (math.pow(math.log10(reynolds_number_body(V, Lenght)), 2.58))

# def c_xar_wing(eng_amount_0, A_wing_eng_0, c_mid_0, V_0, A_wing_0):
# return 0.925 * k_eng(eng_amount_0, A_wing_eng_0, A_wing_0) * c_f0(V_0) * n_c(c_mid_0) * n_m(V_0)


print(k_eng())  # 2, 7.7, 29.2
print(c_f0(A_wing, L_wing))  # 127
print(n_c(c_mid_stab))  # 0.16
print(n_m())  # 127
print(c_xa_split(2 * l_split_flap, L_wing))
print(c_xa_split(2 * l_split_ail, L_wing))
# print(c_xar_wing(2, 7.7, 0.16, 127, 29.2))
# print(c_xar_wing())
