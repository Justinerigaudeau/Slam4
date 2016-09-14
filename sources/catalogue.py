# -*- coding: utf-8 -*-
'''
Author : prof
'''
import jouet


class Catalogue(object):
    '''
    Classe métier catalogue
    '''

    def __init__(self, uneAnnee):
        '''
        Constructor
        @param uneAnnee : l'année de référence du catalogue
        @type uneAnnee : integer
        '''
        self.__annee = uneAnnee
        self.__les_jouets = {}
        # Il s'agit d'une collection de type dictionnaire.
        # Chaque clé est de type Jouet.
        # la valeur associée est un entier.
        # la valeur correspondant au nombre de fois où le jouet a été choisi.

    def get_annee(self):
        '''
        @return : integer
        '''
        return self.__annee

    def get_nb_jouets(self):
        '''
        Retourne le nombre de jouets proposés
        @return : integer
        '''
        return len(self.__les_jouets)

    def afficher_catalogue(self):
        '''
        Permet d'afficher les jouets du catalogue
        '''
        for unJouet in self.__les_jouets.keys():
            print(str(unJouet))

    def ajouter_jouet(self, libelleJouet, laTrancheAge):
        '''
        Ajoute le nouveau jouet au catalogue
        @param libelleJouet : libelle du jouet à ajouter
        @type libelleJouet : string
        @param laTrancheAge : tranche d'âge du jouet à ajouter
        @type laTancheAge : TancheAge
        '''
        pass

    def choisir_jouet(self, libelleJouet, laTrancheAge):
        '''
        Permet d'enregistrer la sélection du jouet.
        Le jouet choisi a pour libelle "libelle"
        Le jouet appartient à la tranche d'age laTranche.
        @param libelleJouet : libelle du jouet choisi
        @type libelleJouet : string
        @param laTrancheAge : tranche d'âge du jouet à ajouter
        @type laTancheAge : TancheAge
        '''
        pass
