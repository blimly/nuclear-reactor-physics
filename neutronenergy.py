import matplotlib.pyplot as plt
from numpy import arange, mean, array
from math import pi, e

k       = 1.3806e-23
max_e   = 5e-20
j_to_ev = 6.242e18
steps   = 500

P       = lambda T, E: 2 * pi / ((pi * k * T)**1.5) * E**0.5 * e**(-E / (k * T))
    
T300K   = [P(300, i)   for i in arange(0, max_e, max_e/steps)]
T600K   = [P(600, i)   for i in arange(0, max_e, max_e/steps)]
eVs     = [i * j_to_ev for i in arange(0, max_e, max_e/steps)]

T300K  = [steps * v / sum(T300K) / eVs[-1] for v in T300K]
T600K  = [steps * v / sum(T600K) / eVs[-1] for v in T600K]

#modeEV300 = eVs[T300K.index(max(T300K))]
#modeEV600 = eVs[T600K.index(max(T600K))]
meanEV300 = sum([eVs[i] * T300K[i] for i in range(len(eVs))]) / sum(T300K)
meanEV600 = sum([eVs[i] * T600K[i] for i in range(len(eVs))]) / sum(T600K)

plt.rcParams["text.usetex"] = True
plt.plot(eVs, T300K, label="$E_{300K}$", c="royalblue")
plt.plot(eVs, T600K, label="$E_{600K}$", c="darkorange")
plt.xlabel("$E (eV)$")
plt.ylabel("$\chi_p (eV^{-1})$")
plt.axvline(x=meanEV300, label="$\overline{E}_{300K} $" + f"={meanEV300:.04f}", c="royalblue",  linestyle=":")
plt.axvline(x=meanEV600, label="$\overline{E}_{600K} $" + f"={meanEV600:.04f}", c="darkorange", linestyle=":")
plt.legend()
plt.show()




