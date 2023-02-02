def eredmeny(jatekoslapok,geplapok):
    return "nincs kesz"


def jatekosvesztett_teszt():
    jatekos = [10, 9, 3]
    gep = [10, 9]
    varteredmeny = "jatekos vesztett"
    kapotteredmeny = eredmeny (jatekos, gep)
    print("jatékos vesztett teszt")
    if kapotteredmeny == varteredmeny:
        print("teszt sikeres")
    else:
        print("megbukott")


def tesztesetek():
    jatekosvesztett_teszt()

tesztesetek()