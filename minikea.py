# minikea.py

def acceuillir():
    nom_visiteur = input(
        'merci de contacter Minikea ! Je peux avoir votre prénom ? ').capitalize()
    print(f'Bienvenue che Minikea . {nom_visiteur} !')
    return


# Menu Général

def choisir_categ():
    print(
        '*** Menu général MINIKEA *** \n[1] Horaires et accès \n[2] Gestion de commande \n[3] Suivi de livraison \n[4] Suggestion de produit \n[5] Autres sujet ')
    cCatego = input(
        'Choisissez une gatégories en tapant un chiffre entre 1 et 5 : ')
    if cCatego == '1':
        info_boutique()
        return
    if cCatego == '2':
        gestion_commandes()
        return
    if cCatego == '3':
        suivi_livraison()
        return
    if cCatego == '4':
        service_marketing()
        return
    if cCatego == '5':
        autres()
        return
    if cCatego not in [1, 2, 3, 4, 5]:
        choisir_categ()


# Catégorie: Horaires & Accès

def info_boutique():
    adrph = '58 Rue de Zwickau 75011 PARIS'
    hora = 'du lundi au samedi 10h - 18h'
    print(f'\nMinikea se trouve au {adrph}. \nLa boutique est ouverte {hora}.')
    cStopEncore = input('Autre chose ? [o/n] ').lower()
    if cStopEncore == "o":
        choisir_categ()
    else:
        print('Merci de nous avoir contacté')
        return


# Catégorie: Gestion de commande

def gestion_commandes():
    print('\nVous êtes au service de gestion des commandes.')
    nom_client = input('Nom indiqué sur le bon de commande : ')
    num_commande = input('Indiquez le numéro de commande : ')
    transfert_Elliot()
    return


# Catégorie: Suivi de livraison

def suivi_livraison():
    print('Nous somme désdolés que vous ayez subi un souci avec votre commande.')
    nom_client = input('Nom indiqué sur le bon de commande : ')
    num_commande = input('indiquez le numéro de commande : ')
    souci = input('Décriver votre problème : ')
    transfert_Christine()
    return


# Catégorie: Suggestion de produit

def service_marketing():
    print('Nous vous remercions pour votre suggestion et allons vous mettre en relation avec le service concerné.')
    transfet_Raoul()
    return


# Catégorie: Autre sujet

def autres():
    transfert_Therese()
    return


# Transferts aux départements de Minikea

def transfert_Elliot():
    print('Parfait ! Je verifie le statut de votre commande . ')
    return


def transfert_Christine():
    print('Merci pour votre détails. Nous vérifions votre commande et vous recontactons au plus vite.')
    return


def transfet_Raoul():
    suggestion_marketing = input(
        'Dites-moi quel autre produit nous devrions proposer : ')
    return


def transfert_Therese():
    autre_info = input('De quoi aimeriez-vous nous informer? : ')
    return


# *** Bloc principal du programme qui appelle les fonctions

acceuillir()
choisir_categ()
