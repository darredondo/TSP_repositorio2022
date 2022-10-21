import unittest

from funciones import funciones


class PruebasUnitarias(unittest.TestCase):
    def test_funcionContarPares1(self):
        entrada = [1, 2, 3, 4]
        resultado_esperado = 2
        fun = funciones()
        resultado_obtenido = fun.funcionContarPares(entrada)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionContarPares2(self):
        entrada = [2, 2, 3, 4]
        resultado_esperado = 3
        fun = funciones()
        resultado_obtenido = fun.funcionContarPares(entrada)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionContarNegativos1(self):
        entrada = [-1, 2, -7, -4]
        resultado_esperado = 3
        fun = funciones()
        resultado_obtenido = fun.funcionContarNegativos(entrada)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionContarNegativos2(self):
        entrada = [1, 2, 7, 0]
        resultado_esperado = 0
        fun = funciones()
        resultado_obtenido = fun.funcionContarNegativos(entrada)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionInversaMayus1(self):
        entrada = "Hola"
        resultado_esperado = "ALOH"
        fun = funciones()
        resultado_obtenido = fun.funcionInversaMayus(entrada)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionInversaMayus2(self):
        entrada = "abcd"
        resultado_esperado = "DCBA"
        fun = funciones()
        resultado_obtenido = fun.funcionInversaMayus(entrada)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionVocales1(self):
        entrada = "Hola"
        resultado_esperado = 2
        fun = funciones()
        resultado_obtenido = fun.funcionVocales(entrada)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionVocales2(self):
        entrada = "abcd"
        resultado_esperado = 1
        fun = funciones()
        resultado_obtenido = fun.funcionVocales(entrada)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionIniciales1(self):
        entrada = "Juan Camaney"
        resultado_esperado = "JC"
        fun = funciones()
        resultado_obtenido = fun.funcionIniciales(entrada)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionIniciales2(self):
        entrada = "Ana Rosa Torres Mendez"
        resultado_esperado = "ARTM"
        fun = funciones()
        resultado_obtenido = fun.funcionIniciales(entrada)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionEsOrden1(self):
        entrada = [1, 7, 8, 14]
        fun = funciones()
        resultado_obtenido = fun.funcionEsOrden(entrada)
        self.assertTrue(resultado_obtenido)

    def test_funcionEsOrden2(self):
        entrada = [1, 23, 7, 0]
        fun = funciones()
        resultado_obtenido = fun.funcionHayDuplicados(entrada)
        self.assertFalse(resultado_obtenido)

    def test_funcionHayDuplicados1(self):
        entrada = [1, 7, 1, 14]
        fun = funciones()
        resultado_obtenido = fun.funcionHayDuplicados(entrada)
        self.assertTrue(resultado_obtenido)

    def test_funcionHayDuplicados2(self):
        entrada = [1, 23, 7, 0]
        fun = funciones()
        resultado_obtenido = fun.funcionHayDuplicados(entrada)
        self.assertFalse(resultado_obtenido)

    def test_funcionListaTipos1(self):
        entrada = ["a", 3]
        resultado_esperado = [str, int]
        fun = funciones()
        resultado_obtenido = fun.funcionListaTipos(entrada)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionListaTipos2(self):
        entrada = [2, 2.3, "XYZ", 3]
        resultado_esperado = [int, float, str, int]
        fun = funciones()
        resultado_obtenido = fun.funcionListaTipos(entrada)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionAjustar1(self):
        entrada1 = 3
        entrada2 = 1
        entrada3 = 10
        resultado_esperado = 3
        fun = funciones()
        resultado_obtenido = fun.funcionAjustar(entrada1, entrada2, entrada3)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionAjustar2(self):
        entrada1 = 2
        entrada2 = 5
        entrada3 = 10
        resultado_esperado = 5
        fun = funciones()
        resultado_obtenido = fun.funcionAjustar(entrada1, entrada2, entrada3)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionListaClasificados1(self):
        entrada = [12, 3, 0, -1]
        resultado_esperado = [1, 1, 2]
        fun = funciones()
        resultado_obtenido = fun.funcionListaClasificados(entrada)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionListaClasificados2(self):
        entrada = [12, 3, -1]
        resultado_esperado = [1, 0, 2]
        fun = funciones()
        resultado_obtenido = fun.funcionListaClasificados(entrada)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionListaMultiplos1(self):
        entrada1 = [1, 2, 3]
        entrada2 = 3
        resultado_esperado = [3, 6, 9]
        fun = funciones()
        resultado_obtenido = fun.funcionListaMultiplos(entrada1, entrada2)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionListaMultiplos2(self):
        entrada1 = [1, 2, 3, 5]
        entrada2 = 10
        resultado_esperado = [10, 20, 30, 50]
        fun = funciones()
        resultado_obtenido = fun.funcionListaMultiplos(entrada1, entrada2)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionCombinarListas1(self):
        entrada1 = [1, 3]
        entrada2 = [2, 4]
        resultado_esperado = [1, 2, 3, 4]
        fun = funciones()
        resultado_obtenido = fun.funcionCombinarListas(entrada1, entrada2)
        self.assertEqual(resultado_esperado, resultado_obtenido)

    def test_funcionCombinarListas2(self):
        entrada1 = [1, 3]
        entrada2 = [2, 5, 8, 12]
        resultado_esperado = [1, 2, 3, 5, 8, 12]
        fun = funciones()
        resultado_obtenido = fun.funcionCombinarListas(entrada1, entrada2)
        self.assertEqual(resultado_esperado, resultado_obtenido)


if __name__ == '__main__':
    unittest.main()
