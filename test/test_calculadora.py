import unittest
import Calculadoreition 

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        Calculadoreition.clear()

    def test_suma_basica(self):
        Calculadoreition.click("5")
        Calculadoreition.click("+")
        Calculadoreition.click("7")
        Calculadoreition.equal()
        self.assertEqual(Calculadoreition.entry.get(), "12")

    def test_division_decimal(self):
        Calculadoreition.click("1")
        Calculadoreition.click("0")
        Calculadoreition.click("/")
        Calculadoreition.click("4")
        Calculadoreition.equal()
        self.assertEqual(Calculadoreition.entry.get(), "2.5")

    def test_boton_clear(self):
        Calculadoreition.click("9")
        Calculadoreition.click("9")
        Calculadoreition.clear()
        self.assertEqual(Calculadoreition.entry.get(), "")

if __name__ == '__main__':
    unittest.main()