import autoDataEntry


def effectuerTraitement(ligneCouranteBase):
    '''
    Contrairement aux autres méthodes, cette méthode se trouve dans le fichier **main.py**, car elle doit être modifiée par l'utilisateur!  

    Elle est utile dans le cas où on utilise un fichier CSV de base de données.   
    Pour chaque ligne du fichier CSV, cette méthode sera appelée automatiquement par la méthode lireCsv afin d'effectuer une suite d'opérations.  

    L'utilisateur doit donc y entrer les différentes opérations à réaliser pour chaque ligne du fichier CSV.  

    Pour accéder aux colonnes de la ligne courante du fichier CSV il faut entrer le mot clé `base`.

    Exemple:  
    - base[0] => Première colonne du fichier CSV
    - base[1] => deuxième colonne du fichier CSV
    - base[10] =>onxième colonne du fichier CSV
    '''
    try:
        flagReussi = False
        # Exemples:
        # autoDataEntry.cliquerSur("entete.png")

        # autoDataEntry.ecrire("\n") #Retourne à la ligne dans le fichier texte
        # autoDataEntry.ecrire(ligneCouranteBase[0])

        # autoDataEntry.ecrire("\n")
        # autoDataEntry.ecrire(ligneCouranteBase[1])

        # autoDataEntry.ecrire("\n")
        # autoDataEntry.ecrire(ligneCouranteBase[2])

        # autoDataEntry.ecrire("\n")
        # autoDataEntry.scrollSouris(-200)

        # Ecrire les instructions en dessous:
        # ...
      
        flagReussi = True
        return flagReussi

    except:
        print(f"Erreur lors du traitement d'une ligne. Le programme va s'arrêter.")
        quit()
  


if __name__ == '__main__':
    
    # Exemples:
    # autoDataEntry.gloCheminCaptures = "nouveauRepertoireCaptures/"
    # autoDataEntry.csvNom = 'base2.csv'
    # autoDataEntry.csvDelimiteur = "_"
    # autoDataEntry.afficherCoordonneesCapture("boutonValider")
    # autoDataEntry.lireCsv()
    # autoDataEntry.afficherCoordonneesCapture("entete.png")

    print ("Début du programme")
    # Ecrire les instructions en dessous de cette ligne. Exemples:
    #...
       

    