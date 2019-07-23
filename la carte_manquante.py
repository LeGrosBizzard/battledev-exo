lines = ['T5 TA CA P7 P10 C7 QD T2 C6 PA C9 Q10 P3 C10 P2 TD QR P9 C2']

dico = {'11':'V', "12":'D', "13":'R', "14":'A'}

traitement = [i.split() for i in lines]
traitement = traitement[0]


liste_carte = []

c = 0
lettre = ""
for i in range(4):

    if c == 0:
        lettre = "C"
    elif c == 1:
        lettre = "P"
    elif c == 2:
        lettre = "Q"
    elif c == 3:
        lettre = "T"


    present = False
    non_present = False

    
    for i in range(2, 15):
        for carte in traitement:
            
            if i == carte:
                present = True
            else:
                non_present = True

        if present is True:
            pass
        else:
            liste_carte.append([lettre, str(i)])

    c += 1





liste_manquante = []
for i in liste_carte:

    ok = False
    
    for cle, valeur in dico.items():
        if i[1] == cle:
            liste_manquante.append(str(i[0]) + str(valeur))
            ok = True

    if ok is True:
        pass
    elif ok is False:
        liste_manquante.append(str(i[0]) + str(i[1]))


fin = []
for i in liste_manquante:

    non = False
    for j in traitement:
        if i == j:
            non = True
    if non is True:
        pass
    else:
        fin.append(i)



out = ""
for i in fin:
    out += str(i + " ")


print(out)















