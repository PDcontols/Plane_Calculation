import numpy

import BasicCalculations


#wing
def C_xar_wing():  # eng_amount, A_wing_eng, c_mid, V, A_wing
    return 0.925 * BasicCalculations.k_eng() * BasicCalculations.c_f0(BasicCalculations.A_wing, BasicCalculations.L_wing) * BasicCalculations.n_c(BasicCalculations.c_mid_wing) * BasicCalculations.n_m()


def C_xar_wing_add():
    return BasicCalculations.c_xa_wc + 2 * BasicCalculations.c_xa_split(BasicCalculations.l_split_flap,
                                                                        BasicCalculations.L_wing_wet) * 2 * BasicCalculations.c_xa_split(
        BasicCalculations.l_split_ail, BasicCalculations.L_wing_wet) + 0.0003


def C_xa_wing():
    return C_xar_wing() + C_xar_wing_add()


def C_xa_wing_int():
    return C_xa_wing() * (1 - (BasicCalculations.Ka_i * (BasicCalculations.S_body/BasicCalculations.A_wing)))


#stabilizer
def C_xa_stab():
   return 0.925 * 2 * BasicCalculations.c_f0(BasicCalculations.A_stab, BasicCalculations.L_stab) * BasicCalculations.n_c(BasicCalculations.c_mid_stab) + 0.003 + BasicCalculations.c_xa_stab + BasicCalculations.c_xa_split(BasicCalculations.l_split_stab, BasicCalculations.L_stab)


#tail
def C_xa_tail():
    return 0.003 + BasicCalculations.c_xa_tail + BasicCalculations.c_xa_split(BasicCalculations.l_split_tail, BasicCalculations.L_tail)


#body
def C_xa_body():
    return BasicCalculations.c_f0_body(BasicCalculations.L_body) * BasicCalculations.n_l * BasicCalculations.n_m_body * ((BasicCalculations.S_body_air)/(BasicCalculations.S_body_mid)) + BasicCalculations.c_xa_body + BasicCalculations.c_xa_body_eng


#engines pods
def C_xa_eng():
    return BasicCalculations.eng_amount * (BasicCalculations.c_f0_body(BasicCalculations.L_eng) * BasicCalculations.n_l_eng * BasicCalculations.n_m_eng) * ((BasicCalculations.S_eng_air)/(BasicCalculations.S_eng_mid)) + BasicCalculations.c_xa_eng
