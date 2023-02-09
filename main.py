#megoldas
def eredmeny(jatekoslapok: [int], geplapok: [int]):
    jatekospont: int = szamolas(jatekoslapok)
    geppont: int = szamolas(geplapok)
    jatekoslapok = len(jatekoslapok)
    geplapok = len(geplapok)
    if jatekospont <= 21 and geppont <= 21:
        if jatekospont > geppont:
            s = "Játékos nyert!"
        elif geppont > jatekospont:
            s = "Gép nyert!"
        elif geppont == jatekospont:
            if jatekoslapok < geplapok:
                s = "Játékos nyert!"
            elif jatekoslapok > geplapok:
                s = "Gép nyert!"
            else:
                s = "Döntetlen osztoztok a nyereségen"
    else:
        if jatekospont > 21:
            s = "Játékos vesztett!"
        if geppont > 21:
            s = "Gép vesztett!"
        if jatekospont > 21 and geppont > 21:
            s = "Döntetlen osztoztok a nyereségen"

    return s

def szamolas(lapok)->int:
    pontok: int = 0
    i: int = 0
    while i < len(lapok):
        pontok += lapok[i]
        i += 1
    return pontok
#tesztek
def jatekos_vesztett_teszt():
    jatekospontok = [10, 5, 7]
    geppontok = [2, 7, 9]
    #teszt
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos vesztett!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def gep_vesztett_teszt():
    jatekospontok = [2, 7, 9]
    geppontok = [10, 5, 7]
    #teszt
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép vesztett!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def lapok_osszege_teszt():
    jatekospontok = [11, 11]
    geppontok = [10, 10]
    #teszt
    osszeg = szamolas(jatekospontok)
    if osszeg > 21:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def jatekos_kozelebb_teszt():
    jatekospontok = [9, 10]
    geppontok = [8, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def gep_kozelebb_teszt():
    jatekospontok = [8, 10]
    geppontok = [9, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép nyert!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def gep_vesztett_dontetlen_teszt():
    jatekospontok = [9, 10]
    geppontok = [9, 5, 5]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def jatekos_vesztett_dontetlen_teszt():
    jatekospontok = [9, 5, 4]
    geppontok = [9, 9]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép nyert!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def dontetlen_teszt():
    jatekospontok = [10, 10]
    geppontok = [10, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Döntetlen osztoztok a nyereségen"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")




def jatekos_nyer_huszonegy():
    jatekospontok = [11, 10]
    geppontok = [10, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def jatekos_nyer_tobb_lap():
    jatekospontok = [10, 5, 4]
    geppontok = [10, 9]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def jatekos_nyer_kevesebb_lap():
    jatekospontok = [10, 9]
    geppontok = [10, 5, 4]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def jatekos_veszit_tobb_lap():
    jatekospontok = [10, 5, 4]
    geppontok = [10, 9]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép nyert!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def jatekos_veszit_kevesebb_lap():
    jatekospontok = [10, 9]
    geppontok = [10, 5, 4]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos vesztett!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")


def gep_nyer_tobb_lap():
    jatekospontok = [10, 9]
    geppontok = [10, 5, 4]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép nyert!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def gep_nyer_kevesebb_lap():
    jatekospontok = [10, 5, 4]
    geppontok = [10, 9]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép nyert!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def gep_veszit_tobb_lap():
    jatekospontok = [10, 9]
    geppontok = [10, 5, 4]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")



def dontetlen_huszonegy():
    jatekospontok = [10, 11]
    geppontok = [10, 11]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Döntetlen osztoztok a nyereségen"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def dontetlen_lap():
    jatekospontok = [10, 10]
    geppontok = [10, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Döntetlen osztoztok a nyereségen"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def dontetlen_tobb_mint_huszonegy():
    jatekospontok = [12, 11]
    geppontok = [12, 11]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Döntetlen osztoztok a nyereségen"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")

def tesztek():
    jatekos_vesztett_teszt()
    gep_vesztett_teszt()
    lapok_osszege_teszt()
    jatekos_kozelebb_teszt()
    gep_kozelebb_teszt()
    gep_vesztett_dontetlen_teszt()
    jatekos_vesztett_dontetlen_teszt()
    dontetlen_teszt()
    jatekos_nyer_huszonegy()
    jatekos_nyer_tobb_lap()
    jatekos_nyer_kevesebb_lap()
    jatekos_veszit_tobb_lap()
    jatekos_veszit_kevesebb_lap()
    gep_nyer_tobb_lap()
    gep_nyer_kevesebb_lap()
    gep_veszit_tobb_lap()
    dontetlen_huszonegy()
    dontetlen_lap()
    dontetlen_tobb_mint_huszonegy()


tesztek()