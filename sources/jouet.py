# -*- coding: utf-8 -*-
'''
Author : prof
'''
import trancheAge

class Jouet(object):
    '''
    Classe métier Jouet
    '''

    def __init__(self,unLibelle,uneTranche):
        '''
        Instancie un objet Jouet
        @param unLibelle: définit le libelle du jouet_P
        @param uneTranche : définit la tranche d'age correspondant au jouet_P
        @type unLibelle : string
        @type uneTranche : TrancheAge 
        '''
        
        self.__libelle=unLibelle
        self.__laTranche=uneTranche

    def get_libelle(self):
        '''
        @rtype: string 
        '''
        return self.__libelle

    def get_laTranche(self):
        '''
        @rtype : laTranche
        '''
        return self.__laTranche

    def convient (self,unAge):
        '''
        Retourne True si le jouet convient à l’âge unAge passé en paramètre. False sinon.
        @param unAge: entier
        @rtype: boolean
        
        '''
        return (unAge >= self.__laTranche.get_age_min()) or (unAge <= self.__laTranche.get_age_max())

    
    def __str__(self):
        '''
        Retourne une chaîne contenant : le libellé du jouet_P,les âges minimum et maximum de la tranche d’âge lui correspondant.
        Les informations sont séparées par des points-virgules.
        @note : appelée lors de l'appel à l'instruction print
        @return : String
        '''
        return self.__libelle + " ; " + str(self.__laTranche.get_age_min()) + " ans à " + str(self.__laTranche.get_age_max()) + " ans"

