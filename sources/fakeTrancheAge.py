# -*- coding: utf-8 -*-
'''
Author : prof
'''


class TrancheAge:
    '''
    Fake de la classe métier TrancheAge
    '''

    def __init__(self, unAgeMin, unAgeMax):
        '''
        Fake Constructor
        '''
        pass

    def __str__(self):
        '''
        @note : Appelée par l'instruction print
        '''
        return "tranche"

    def get_age_min(self):
        '''
        @rtype : int
        '''
        return 3

    def get_age_max(self):
        '''
        @rtype : int
        '''
        return 6
