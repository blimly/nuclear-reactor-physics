from math import log

# Most of the equasions are taken from this site
# https://www.nuclear-power.com/glossary/neutron-moderatoraverage-logarithmic-energy-decrement/

alpha       = lambda M, m           : (M-m)**2 / (M+m)**2 + 1e-32
frac_E_loss = lambda K1, Kf, alpha  : -log(K1/Kf) / log(alpha)
decrement   = lambda M, alpha       : 1 + alpha / (1-alpha) * log(alpha)
collisions  = lambda dec, E         : log(E) / dec

m           = 1 #.00866  # amu (neturon mass)

M_Be9       = 9 #9.0122   # amu
M_D2        = 2 # .01363  # amu

Kf          = 0.025    # eV (thermal neutron)
K_1Be9      = 1.667e6  # eV
K_1D2       = 2.225e6  # eV (Treshhold energy)

def report(M):
    K1 = 2e6
    print("Fractional energy loss (f) of deuterium: ")
    a = alpha(M, m)
    print(frac_E_loss(K1, Kf, a))
    print("Logarithmic energy decrement per collision (ξ): ")
    dec = decrement(M, a)
    print(dec)
    print("Average collisions to thermalize (2 MeV -> 1eV)")
    print(round(collisions(dec, K1)))
    print()

print("D")
report(2)

print("Be9")
report(9)

print("C12")
report(12)

print("H")
report(1)

print("O")
report(16)






