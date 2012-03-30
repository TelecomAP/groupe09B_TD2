""" module de test de la classe logic"""

from unittest import TestCase
import logic

class LogicTests(TestCase):

    def test_and(self):
        self.assertEquals(logic.and_(0,1),0)

    def test_or(self):
        self.assertEquals(logic.or_(0,1),1)

