import math
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Aerodynamic
import BasicCalculations


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# print(BasicCalculations.reynolds_number(127))
#print(BasicCalculations.mach_speed(127))

# print(0.455/(math.pow(math.log10(BasicCalculations.reynolds_number(127)), 2.58)))

#print(BasicCalculations.C_xar_wing)
print(Aerodynamic.C_xar_wing())
print(Aerodynamic.C_xar_wing_add())
print(Aerodynamic.C_xa_wing())
print(Aerodynamic.C_xa_wing_int())
print(Aerodynamic.C_xa_stab())
print(Aerodynamic.C_xa_tail())
print(Aerodynamic.C_xa_body())
print(Aerodynamic.C_xa_eng())

