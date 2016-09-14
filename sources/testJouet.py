# -*- coding: utf-8 -*-

import unittest
import jouet


class TestJouet(unittest.TestCase):

    def setUp(self):
        import fakeTrancheAge as trancheAge
        unittest.TestCase.setUp(self)
        self.uneTrancheA = trancheAge.TrancheAge(3, 6)
        self.unJouet = jouet.Jouet("Draisienne Junior", self.uneTrancheA)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_convenir(self):
        message = "Erreur dans intervalle"
        self.assertTrue(self.unJouet.convient(4), message)

    def test_convenir_sup(self):
        message = "Erreur : age supérieur borne sup"
        self.assertFalse(self.unJouet.convient(7), message)

    def test_convenir_inf(self):
        message = "Erreur : age inférieur borne inf"
        self.assertFalse(self.unJouet.convient(2), message)

if __name__ == "__main__":
    unittest.main()
