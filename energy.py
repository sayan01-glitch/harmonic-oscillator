def energy(n,omega):
    hbar=1.0
    E=hbar*omega*(n+0.5)
    return E

for n in range(10):
    print("n=",n,"Energy=",energy(n,2.0))
