import unittest
from syntax import *
class SyntaxTest(unittest.TestCase):
    def test_readMolekyl(self):
        """ Testar molekylen ger korrekt """
        self.assertEqual(kollaMolekylen("H2"),  "Formeln är syntaktiskt korrekt")
        self.assertEqual(kollaMolekylen("Mn4"), "Formeln är syntaktiskt korrekt")

    def test_readLetter(self):
        self.assertEqual(kollaMolekylen("cr12"), "Saknar stor bokstav")
    def test_readNum(self):
        self.assertEqual(kollaMolekylen("Cr0"), "För litet tal vid radslutet")
        self.assertEqual(kollaMolekylen("Pb1"), "För litet tal vid radslutet")
if __name__ == '__main__':
    unittest.main()
