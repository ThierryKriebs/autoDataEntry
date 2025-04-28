

import pyautogui
import time
import csv
import pyperclip
import re
import main

pyautogui.useImageNotFoundException()       #Force l'utilisation de l'exception: ImageNotFound

gloCheminCaptures = "assets/images/captures/"
csvNom = 'base.csv'
csvDelimiteur = ";"


def afficherCoordonneesCapture(pNomChamps):
    """
    Affiche et renvoie les coordonnées et dimensions d'un champ.  
    - X, Y             => coordonnées gauche, haut du champ  
    - Largeur, Hauteur => Largeur et Hauteur du champ.
    - Si non trouvé, retourne un tupple (-1, -1, -1, -1)
    """

    try:
        pNomChamps = gloCheminCaptures + pNomChamps
        (champsX, champsY, champsLargeur, champsHauteur) = pyautogui.locateOnScreen(pNomChamps)
        print(f"Coordonnées dela capture: X: {champsX}    Y: {champsY}    Largeur: {champsLargeur}    "
              f"Hauteur: {champsHauteur}")
        return (champsX, champsY, champsLargeur, champsHauteur)

    except pyautogui.ImageNotFoundException as err:

        print(f"la capture suivante n'a pas été localisée: {pNomChamps}")
        return (-1, -1, -1, -1)


def renvoyerCoordonneesCapture(pNomChamps, pFlagAfficher = False):
    """
    Identique à la méthode afficherCoordonneesCapture, mais l'affichage des informations peut être désactivé (désactivé par défaut).  
    - X, Y             => Point gauche haut du champ
    - Largeur, Hauteur => Largeur et Hauteur du champ.  
    - Si non trouvé, retourne un tupple (-1, -1, -1, -1)
    """

    try:
        pNomChamps = gloCheminCaptures + pNomChamps
        (champsX, champsY, champsLargeur, champsHauteur) = pyautogui.locateOnScreen(pNomChamps)

        if pFlagAfficher:
            print(f"Coordonnées dela capture: X: {champsX}    Y: {champsY}    Largeur: {champsLargeur}    "
                  f"Hauteur: {champsHauteur}")

        return (champsX, champsY, champsLargeur, champsHauteur)

    except pyautogui.ImageNotFoundException as err:

        print(f"la capture suivante n'a pas été localisée: {pNomChamps}")
        return (-1, -1, -1, -1)


def attendreApparition(pCapture, pNbreTentative = 1, pTempsEntreTentative = 0.5, pFlagAffiMessErr = False,
                           pFlagAffiMessTrouve = False, flagArreterSiNonTrouve = True):
    """
    Attend que le programme à piloter affiche une information (popup, nouveau menu, nouveau formulaire, nouvelle fenêtre...)  
    Parfois certaines fonctionnalités mettent du temps à apparaître ou apparaissent progressivement.  
    Cette méthode recherche en boucle sur le site la capture passée en paramètre.  
    - pCapture               => Image à rechercher sur le site
    - pNbreTentative         => (Optionnel) Nombre de tentative de recherche
    - pTempsEntreTentative   => (Optionnel) Temps entre chaque tentative
    - pFlagAffiMessErr       => (Optionnel) Affiche un message à chaque tentative échouée
    - pFlagAffiMessTrouve    => (Optionnel) Affiche un message si capture trouvée
    - flagArreterSiNonTrouve => (Optionnel) Arrête le script python si la capture n'est pas trouvée
    """

    cpt = 1
    flagTrouve = False
    coord = (-1, -1, -1, -1)
    captureAvecChe = gloCheminCaptures + pCapture

    while not flagTrouve and cpt <= pNbreTentative:
        try:
            coord = pyautogui.locateOnScreen(captureAvecChe)
            if coord[0] != -1:
                flagTrouve = True
                if pFlagAffiMessTrouve:
                    print(f"La capture <<{pCapture}>> a été localisée!  Coordonnées: X: {coord[0]}    Y: {coord[1]}    "
                          f"Largeur: {coord[2]}     Hauteur: {coord[3]}")

        except pyautogui.ImageNotFoundException as err:

            if pFlagAffiMessErr:
                print(f"Essais numéro: {cpt}, la capture <<{pCapture}>> n'a pas été trouvée!")

            cpt += 1
            mettreEnPause(pTempsEntreTentative)

    if coord[0] == -1:
        if flagArreterSiNonTrouve:
            print(f"ARRET DU PROGRAMME,la capture suivante n'a pas été localisée: <<{pCapture}>>")
            quit()

        return False
    else:
        return True


def verifierPasApparition (pCapture, pNbreEssaisAEff = 2, pTempsEntreEssais = 0.5, pFlagAffiMessNonTrouve = False,
                           pFlagAffiMessTrouve = True, flagArreterSiTrouve = True):
    """
    Vérifie que le programme à piloter n'affiche PAS une alerte (message d'erreur, fenêtre indésirable, messageBox compromettant...)  
    Parfois certains alertes mettent du temps à apparaître ou apparaissent progressivement.  
    Cette fonction recherche en boucle sur le site que la capture passée en paramètre n'apparaît PAS!  
    - pCapture                => Image à rechercher sur le site
    - pNbreEssaisAEff         => (Optionnel) Nombre d'essais à effectuer
    - pTempsEntreEssais       => (Optionnel) Temps entre chaque essai
    - pFlagAffiMessNonTrouve  => (Optionnel) Affiche un message à chaque essais réussi (capture non trouvée!)
    - pFlagAffiMessTrouve     => (Optionnel) Affiche un message d'avertissement si capture trouvée
    - flagArreterSiTrouve     => (Optionnel) Arrête le script python si la capture est trouvée
    """

    cpt = 1
    flagTrouve = False
    coord = (-1, -1, -1, -1)
    captureAvecChe = gloCheminCaptures + pCapture

    while not flagTrouve and cpt <= pNbreEssaisAEff:
        try:
            coord = pyautogui.locateOnScreen(captureAvecChe)
            if coord[0] != -1:
                flagTrouve = True
                if pFlagAffiMessTrouve:
                    print(f"ATTENTION: La capture <<{pCapture}>> a été localisée!  Coordonnées: X: {coord[0]}    "
                          f"Y: {coord[1]}    Largeur: {coord[2]}     Hauteur: {coord[3]}")

        except pyautogui.ImageNotFoundException as err:

            if pFlagAffiMessNonTrouve:
                print(f"Essais numéro: {cpt}, la capture <<{pCapture}>> n'est bien pas apparue!")

            cpt += 1
            mettreEnPause(pTempsEntreEssais)

    if coord[0] != -1:
        if flagArreterSiTrouve:
            print(f"ARRET DU PROGRAMME, car la capture suivante est apparue: <<{pCapture}>>")
            quit()
        return False

    else:
        return True


def mettreEnPause (tempsDePause = 0.5):
    """
    Met en pause le programme pendant la durée spécifiée en secondes
    Si aucune durée n'est spécifiée, la pause dure 1/2 seconde.
    """
    time.sleep(tempsDePause)


def cliquerSur (pNomChamps, positionClic = "centré", offsetX = 0, flagArreterSiNonTrouve = True,
               pFlagAffiMessTrouve = False):
    """
    Recherche un champ (passé en paramètre sous forme d'une capture PNG) et clique dedans.  
    - positionClic           => Par défaut le clic se fait au centre du champ trouvé. Valeurs possibles (centré, gauche, droite)  
    - offsetX                => Décalage en pixel (positif ou négatif) par rapport à la positionClic  
    - flagArreterSiNonTrouve => A True (valeur par défaut), arrête le programme si le champ n'est pas localisé. A False, le programme continue
    """

    try:
        FlagCliquer = False

        pNomChamps = gloCheminCaptures + pNomChamps
        (champsX, champsY, champsLargeur, champsHauteur) = pyautogui.locateOnScreen(pNomChamps)

        if pFlagAffiMessTrouve:
            print(f"Capture: <<{pNomChamps}>> trouvée aux coordonnées suivantes:"
                  f" X: {champsX}    Y: {champsY}    Largeur: {champsLargeur}     Hauteur: {champsHauteur}")

        clicPosX = champsX
        clicPosY = champsY

        if positionClic == "centré":
            (clicPosX, clicPosY) = pyautogui.center((champsX, champsY, champsLargeur, champsHauteur))
            clicPosX += offsetX

        elif positionClic == "droite":
            clicPosX = champsX + champsLargeur + offsetX
            clicPosY = champsY + 10

        elif positionClic == "gauche":
            clicPosX = champsX + offsetX
            clicPosY = champsY + 10

        pyautogui.click(clicPosX, clicPosY)

        FlagCliquer = True
        return FlagCliquer

    except pyautogui.ImageNotFoundException as err:

        if flagArreterSiNonTrouve:
            print(f"ARRET DU PROGRAMME,la capture suivante n'a pas été localisée: <<{pNomChamps}>>")
            quit()

        FlagCliquer = False
        return FlagCliquer


def cliquerSurSexe(sexe="M", decalageEnX = 7):
    """
    Permet de détecter puis de cliquer sur l'un des deux boutons radio SEXE fourni en exemple (voir le répertoire captureExemples des assets).  

- M => Demande de cliquer sur le sexe masculin
- F => Demande de cliquer sur le sexe féminin
- decalageEnX => Nombre de pixel de décalage vers la gauche entre la zone trouvée (le dessin) et l'endroit où doit avoir lieu la capture (le bouton radio) 

Cette méthode est en fait destinée à cliquer sur un type de bouton radio bien précis (voir le répertoire captureExemples des assets). Si les radio boutons ne sont pas exactement les mêmes (probables), le décalage est les captures d'écran devront bien sûr être adaptés. 
    
    """

    if sexe == "M":
        retour = cliquerSur("sexeMasculin.png", "gauche", decalageEnX)

    elif sexe == "F":
        retour = cliquerSur("sexeFeminin.png", "gauche", decalageEnX)

    else:
        print("ERREUR: La Valeur du champ sexe est incorrecte. Valeurs possibles: M, F")
        retour = False

    return retour


def scrollSouris (nbrePixel = -500):
    """
    Permet de simuler la molette de la souris pour monter ou descendre l'ascenseur du navigateur
    Un nombre positif de pixel monte l'ascenseur.  
    Un nombre négatif le fait descendre. Par défaut -500 pixels.  
    """

    try:
        pyautogui.scroll(nbrePixel)
        time.sleep(0.2)

    except:
        print(f"Erreur lors du scrolling de la fenêtre. Le programme va s'arrêter. "
              f"Vérifiez le paramètre nombre de Pixel.")
        quit()


def ecrire(pdonnee):
    """
    Écrit un texte passé en paramètre à l'endroit où la souris vient de cliquer
    après appel de la fonction: cliquerSur
    """

    pyperclip.copy(pdonnee)
    pyautogui.hotkey('ctrl', 'v')       #gestion des caractères spéciaux #'-_)=@+-...
    pyautogui.press('escape')
    time.sleep(0.2)


def lireCsv():
    """
    Lit ligne par ligne le fichier CSV fourni à csvNom et lance, pour chaque ligne, 
    une suite d'opération définie dans la méthode: effectuerTraitement
    """

    try:
        fichier = open(csvNom, "r")
        contenuFichier = fichier.read()  # Pour traitement dans MajCsv
        fichier.close()

    except:
        print(f"Erreur lors de la lecture du CSV. Le programme va s'arrêter. "
              f"Vérifiez le nom du fichier et son emplacement.")
        quit()

    with open(csvNom, newline='') as csvFichier:
        contenuFichierCsv = csv.reader(csvFichier, delimiter=csvDelimiteur, quotechar='|')

        i = 1
        print(f"Début traitement")
        for tabLigne in contenuFichierCsv:
            if (tabLigne[len(tabLigne) - 1] == "NON"):
                print(f"traitement de la ligne numéro <<{i}>>:   {tabLigne}")

                if main.effectuerTraitement (tabLigne):
                    contenuFichier = majCsv(contenuFichier, ";".join(tabLigne), i)
            i += 1
    print(f"Fin traitement")

def majCsv(contenu, ligneAModif, numLigne):
    """
    Passe les lignes traitées du fichier CSV à OUI.  
    Cette méthode est appelée automatiquement par lireCsv et ne devrait normalement pas être appelée par l'utilisateur.
    """

    try:
        expReg = re.compile('(;NON$)', 1)           #Permet d'être sûr de détecter uniquement le dernier NON
        ligneModifiee = expReg.sub(";OUI", ligneAModif)
        contenu = contenu.replace(ligneAModif, ligneModifiee)

        fichier = open(csvNom, "w")
        fichier.write(contenu)
        fichier.close()

        return contenu

    except:
        print(f"Erreur lors de la MAJ du CSV à la ligne numéro: {numLigne}. Le programme va s'arrêter."
              f" Ligne = <<{ligneAModif}>>")
        quit()

