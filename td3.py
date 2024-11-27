# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes
import time
def tempsEnSeconde(temps):
    return temps[0]* 86400+ temps[1] * 3600 + temps[2]*60 + temps[3]

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours =seconde // 86400
    reste = seconde %86400
    heures = reste //3600
    reste = reste % 3600
    minutes = reste //60
    reste = reste%60
    
    return (jours,heures,minutes , reste)
    
temps = secondeEnTemps(100000)
print(f"{temps[0]}jours{temps[1]} heures {temps[2]} minutes {temps[3]} secondes")

#fonction auxiliaire ici

def affichePluriel(mot : str , nombre : int) -> None :
    
    if nombre > 0: 
        print(nombre, mot, end="")
    if nombre > 1:
        print("s", end=" ")
def afficheTemps(temps: tuple[int, int, int, int]) -> None:

    affichePluriel("jour",temps[0])
    affichePluriel("heure", temps[1])
    affichePluriel("minute",temps[2])
    affichePluriel("seconde",temps[3])

    print()


    
afficheTemps((1,0,14,23))    

def demandeTemps() -> tuple [int, int , int ,int]:
    ''' Demande à l'utilisateur un nombre de jours, d'heures, de minutes et de secondes et 
    les renvoie sous la forme d'un tuple de temps.'''
    jours = -1
    heures = -1
    minutes = -1
    secondes = -1
    while (jours<0):
        jours = int(input("Entrez un nombre de jour"))

    while (heures<0 or heures >=24):
        heures = int(input("Entrez un nombre d'heures"))
    while (minutes <0 or minutes >= 60):
        minutes = int(input("entrez unnombre de minutes"))
    while (secondes <0 or secondes >= 60): 
        secondes = int(input("Entrez un nombre de secondes"))

    return (jours, heures, minutes , secondes)

afficheTemps(demandeTemps())

def sommeTemps(temps1: tuple[int,int,int,int],temps2: tuple[int,int,int,int]):
    
    sommeTemps = tempsEnSeconde(temps1) + tempsEnSeconde(temps2)
    return sommeTemps

Result =sommeTemps((2,3,4,25),(5,22,57,1))
Result = secondeEnTemps(Result)
print(Result)

def proportionTemps(temps: tuple[int, int, int ,int],proportion : float)-> tuple[int,int,int,int]:
    
    return secondeEnTemps(int(tempsEnSeconde(temps)* proportion))
afficheTemps(proportionTemps((2,0,36,0),0.2))
afficheTemps
#appeler la fonction en échangeant l'ordre des arguments


def tempsEnDate(temps: tuple[int,int,int,int])-> tuple[int,int,int,int,int]:

    annee = 1970 + temps[0]//365
    numero_du_jour=1+ temps [0] % 365
    return (annee , numero_du_jour , temps[1], temps[2], temps[3])

    


def afficheDate(date: tuple = ()) -> None:

    if len(date) == 0:
        date = tempsEnDate(secondeEnTemps(int(time.time())))
    print("Jour numéro", date [1], "de l'année", date[0], str(date[2]) + ":" + str(date[3]) + ":" + str(date[4]))



mon_temps = secondeEnTemps(1000000000)
afficheTemps(mon_temps)
afficheDate(tempsEnDate(mon_temps))
afficheDate()

print(time.time())

def estBissextile(annee: int)-> bool:
    return annee % 4 == 0 and (annee % 100 != 0 or annee %400 == 0 )

def bissextile(jours: int) -> None : 

    annee = 1970
    while(jours >= 365):
        if estBissextile(annee):
            print("L'année" + str(annee)+ "est bissextile")
            jours -= 366
        else:
            jours -= 365
        annee += 1

bissextile(20000)

def nombreBissextile (jours: int) -> int:
    