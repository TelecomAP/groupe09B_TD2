""" module de test de la classe operators"""

from unittest import TestCase
import operators

class OperatorsTests(TestCase):

    def test_add(self):
        self.assertEquals(operators.add(2,3),5)

    def test_mul(self):
        self.assertEquals(operators.mul(2,3),6)
