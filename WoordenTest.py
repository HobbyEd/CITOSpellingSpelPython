import random
import os
#een vieze globale variable die het resultaat vasthoud
resultaat = {"goed": 0, "fout": 0}

def startSpelletje(): 
        #Lees eerst de lijsten met woorden in
        GoedeWoorden = leesBestandIn(r"GoedeWoorden.txt")
        FouteWoorden = leesBestandIn(r"FouteWoorden.txt")
        #Hussel de woorden door elkaar
        GoedeWoorden = random.sample(GoedeWoorden, len(GoedeWoorden))
        FouteWoorden = random.sample(FouteWoorden, len(FouteWoorden))
        
        vraagNummer=1
        while True:
                vraagSet = stelVraagSamen(GoedeWoorden, FouteWoorden, vraagNummer)
                if(vraagSet != None):
                        #stelEenvraag levert true op als de vraag goed is beantwoord,
                        #het resultaat is False als de gebruik wil stoppen.
                        if (stelEenVraag(vraagSet, vraagNummer) == False):  
                                break
                        vraagNummer = vraagNummer + 1
                else:
                        break
        input("Oke, dat wat het voor nu...")
         
def stelVraagSamen(goedeWoorden, fouteWoorden, vraagNummer):
        woorden = {} #Directory waarin de woorden worden opgenomen
        i=1
        #test of er nog genoeg goedeWoorden in de lijst zijn 
        if (len(goedeWoorden) >= (vraagNummer*3-i)):
                while (i<= 3):
                        #Let op: VraagNummer wordt eerst met 3 vermenigvuldigd zodat
                        #je iedere keer een blok van drie woorden achterste voren in leest
                        woorden.update({goedeWoorden[vraagNummer*3-i]:"goed"})
                        i += 1
                
        else:
                return None
        #test of er nog genoeg fouteWoorden in de lijst zijn
        if (len(fouteWoorden) > (vraagNummer-1)):
                woorden.update({fouteWoorden[vraagNummer-1]: "fout"})
        else:
                return None 
        return woorden

def stelEenVraag(vraagSet, vraagNummer):              
        printDeVraag(vraagSet, vraagNummer)
        antwoord = input("Welke zin bevat een fout geschreven woord? (Type het nummer voor het woord):")
        if(antwoord.upper() == "X"):
                return False
        elif(antwoord.upper() in ["A", "B", "C", "D"]):
                if (controleerAntwoord(vraagSet, antwoord.upper()) == False):
                        stelEenVraag(vraagSet, vraagNummer)
                else:
                        return True
        else: #er is een ongeldig karakter terug gegeven. Opnieuw proberen
                stelEenVraag(vraagSet, vraagNummer)

def controleerAntwoord(vraagSet, antwoord):
        #vertaal dictionary van letter naar cijfer in lijst
        antwoordMap = {"A": 0, "B": 1, "C": 2, "D": 3}
        
        #maak eerst een lijst met de woorden die gevraagd gaan worden
        #de lijst wordt gebruikt om het antwoordnummer te vertalen naar het geselecteerde woord
        woorden = []
        for key in vraagSet.keys():
                woorden.append(key)
                
        if (vraagSet[woorden[antwoordMap.get(antwoord)]] == "goed"):
                #een goed woord is selecteert, dat is dus fout
                print("Helaas, zin " + antwoord + " is goed geschreven.\nDus probeer het opnieuw.")
                resultaat["fout"] = resultaat.get("fout") + 1
                input()
                return False
        else:
                print("\nJa, goed gezien, zin " + antwoord +" bevat het foute woord.")
                resultaat["goed"] = resultaat.get("goed") + 1
                input()
                return True

def printDeVraag(vraagSet, vraagNummer):
        os.system('cls()')
        keus = "A"
        print ("Om het spelletje te stoppen type: 'X'. \n \n")
        print ("Aantal keren goed geantwoord: " + str(resultaat.get("goed")))
        print ("Aantal keren fout geantwoord: " + str(resultaat.get("fout")))
        print ("Dit is de vraag nummer: " + str(vraagNummer)  + " \n")
        for key in vraagSet.keys():
                print (keus + ": " + key + " \n")
                keus = chr(ord(keus) +1)

def leesBestandIn(bestandsNaam):
        try:
                file = open(bestandsNaam, "r")
                lijst = []
                for line in file.readlines():
                        if line.strip(): #Controlleer of de lijn leeg is.
                                lijst.append(line.rstrip())
                file.close()
                return lijst
        except: 
                return "Niet gelukt om een bestand in te lezen"
 

if __name__ == "__main__":
        startSpelletje()
