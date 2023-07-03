from math import soma
import unittest

class TestSoma(unittest.TestCase):
    def test_soma(self):
        total = soma(15, 10)
        self.assertEqual(total, 30, "Resultado da soma invalido")

if __name__ == "__main__":
    unittest.main()