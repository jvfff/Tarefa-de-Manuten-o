import unittest
from banco import ContaBancaria, Banco

class TestContaBancaria(unittest.TestCase):

    def setUp(self):
        self.conta = ContaBancaria("Ana", 1000)

    def test_criacao_conta(self):
        self.assertEqual(self.conta.titular, "Ana")
        self.assertEqual(self.conta.saldo, 1000)

    def test_deposito(self):
        self.conta.deposito(500)
        self.assertEqual(self.conta.saldo, 1500)

    def test_saque(self):
        self.conta.saque(200)
        self.assertEqual(self.conta.saldo, 800)

    def test_saque_excedente(self):
        with self.assertRaises(ValueError):
            self.conta.saque(2000)

    def test_deposito_negativo(self):
        with self.assertRaises(ValueError):
            self.conta.deposito(-50)

    def test_saldo_negativo(self):
        with self.assertRaises(ValueError):
            self.conta.saldo = -10


class TestBanco(unittest.TestCase):

    def setUp(self):
        self.banco = Banco()
        self.conta1 = ContaBancaria("Lucas", 500)
        self.conta2 = ContaBancaria("Laura", 1500)
        self.banco.adicionar_conta(self.conta1)
        self.banco.adicionar_conta(self.conta2)

    def test_adicionar_conta(self):
        self.assertEqual(len(self.banco.contas), 2)

    def test_buscar_conta(self):
        conta = self.banco.buscar_conta("lucas")
        self.assertIsNotNone(conta)
        self.assertEqual(conta.titular, "Lucas")

    def test_listar_contas(self):
        contas = self.banco.listar_contas()
        self.assertEqual(contas[0].titular, "Lucas")
        self.assertEqual(contas[1].titular, "Laura")

    def test_saldo_total(self):
        self.assertEqual(self.banco.saldo_total(), 2000)

    def test_remover_conta(self):
        self.assertTrue(self.banco.remover_conta("Lucas"))
        self.assertIsNone(self.banco.buscar_conta("Lucas"))
        self.assertEqual(len(self.banco.contas), 1)

if __name__ == "__main__":
    unittest.main()
