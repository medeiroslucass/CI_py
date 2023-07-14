import unittest
from math_1 import soma

class TestSoma(unittest.TestCase):
    def test_soma(self):
        total = soma(15, 10)
        print(f"TOTAL: {total}")
        self.assertEqual(total, 30, "Resultado da soma invalido")

if __name__ == "__main__":
    unittest.main()