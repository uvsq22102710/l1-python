#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

from typing import ValuesView


def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    tempsEnSeconde = (temps[0]* 86400,temps[1]*3600,temps[2]*60,temps[3])
    return tempsEnSeconde

temps = (3,23,1,34)
mon_temps=tempsEnSeconde(temps)
print(mon_temps)


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    secondeEnTemps = (seconde//86400),(seconde)%86400//3600, ((seconde%86400)%3600)//60,(((seconde%86400)%3600)%60)
    return secondeEnTemps
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")



#fonction auxiliaire ici

def afficheTemps(temps):
         if temps[0]>1: 
              print(temps[0],"jours",end="")
         elif temps==0:
              print(end="")
         else:
             print(temps[0],"jour",end="")

         if temps[1]>1:
              print(temps[1],"heures",end="")
         elif temps[1]==1:
              print(temps[1],"heure",end="")
         else:
              print(end="")

         if temps[2]>1:
             print(temps[2],"minutes",end="")
         elif temps[2]==1:
             print(temps[2],"minute",end="")
         else:
             print(end="")

         if temps[3]>1:
             print(temps[3],"secondes",end="")
         elif temps[3]==1:
             print(temps[3],"seconde",end="")
         else:
             print(end="")

    
    
afficheTemps ((1,0,14,23))
print(afficheTemps)