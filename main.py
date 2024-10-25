from mma import *

if __name__ == "__main__":

    L1 = Boxeador("Bambam", 100.0)
    print(L1)
    
    L2 = MuayThai("Milton", 100.0)
    print(L2)

    print(L1.soco(L2))
    print(L2)

    print(L2.gancho(L1))

    print(L2.chute_alto(L1))

    print(L2.cruzado(L1))
    print(L1)

    print(L1.cruzado(L2))
    print(L2)

    print(L2.gancho(L1))

    print(L2.gancho(L1))

    print(L2.chute_alto(L1))
    print(L1)