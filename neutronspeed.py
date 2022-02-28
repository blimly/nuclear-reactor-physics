import matplotlib.pyplot as plt
from numpy import arange, mean, array
from math import pi, e

k         = 1.3806e-23
max_speed = 10  # km/s
j_to_ev   = 6.242e18
steps     = 100
neutron_m = 1.6749275e-27

P      = lambda T, E: 2 * pi / ((pi * k * T)**1.5) * E**0.5 * e**(-E / (k * T))
    
speeds = arange(0, max_speed, max_speed/steps)
T300K  = [P(300, neutron_m * (i * 1000)**2 / 2) for i in speeds]
T600K  = [P(600, neutron_m * (i * 1000)**2 / 2) for i in speeds]

T300K  = [steps * v / sum(T300K) / speeds[-1] for v in T300K]
T600K  = [steps * v / sum(T600K) / speeds[-1] for v in T600K]

#modeEV300 = eVs[T300K.index(max(T300K))]
#modeEV600 = eVs[T600K.index(max(T600K))]
meanSpeed300 = sum([speeds[i] * T300K[i] for i in range(len(speeds))]) / sum(T300K)
meanSpeed600 = sum([speeds[i] * T600K[i] for i in range(len(speeds))]) / sum(T600K)

plt.rcParams["text.usetex"] = True
plt.plot(speeds, T300K, label="$v_{300K}$", c="royalblue")
plt.plot(speeds, T600K, label="$v_{600K}$", c="darkorange")
plt.xlabel("$v (km/s)$")
plt.ylabel("$\chi_p (s/km)$")
plt.axvline(x=meanSpeed300, label="$\overline{v}_{300K} $" + f"={meanSpeed300:.04f}", c="royalblue",  linestyle=":")
plt.axvline(x=meanSpeed600, label="$\overline{v}_{600K} $" + f"={meanSpeed600:.04f}", c="darkorange", linestyle=":")
plt.legend()
plt.show()




