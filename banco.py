class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        """
        Inicializa uma conta bancária com um titular e saldo inicial.
        :param titular: Nome do titular da conta.
        :param saldo_inicial: Saldo inicial da conta.
        """
        self.__titular = titular
        self.__saldo = saldo_inicial

    def __str__(self):
        """
        Retorna uma representação em string da conta.
        :return: Uma string com o nome do titular e saldo da conta.
        """
        return f"{self.__titular}: R${self.__saldo:.2f}"

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, nome):
        self.__titular = nome

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self.__saldo = valor

    def deposito(self, valor):
        if valor < 0:
            raise ValueError("O valor do depósito não pode ser negativo.")
        self.__saldo += valor

    def saque(self, valor):
        if valor < 0:
            raise ValueError("O valor do saque não pode ser negativo.")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente para o saque.")
        self.__saldo -= valor


class Banco:
    def __init__(self):
        """
        Inicializa o banco com uma lista de contas.
        """
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def buscar_conta(self, titular):
        for conta in self.contas:
            if conta.titular.casefold() == titular.casefold():
                return conta
        return None

    def listar_contas(self):
        return sorted(self.contas, key=lambda conta: conta.saldo)

    def saldo_total(self):
        return sum(conta.saldo for conta in self.contas)

    def remover_conta(self, titular):
        conta = self.buscar_conta(titular)
        if conta:
            self.contas.remove(conta)
            return True
        return False


if __name__ == "__main__":
    banco = Banco()
    banco.adicionar_conta(ContaBancaria("João", 500))
    banco.adicionar_conta(ContaBancaria("Maria", 1500))
    banco.adicionar_conta(ContaBancaria("Carlos", 300))

    conta = banco.buscar_conta("maria")
    if conta:
        print(f"Conta encontrada: {conta}")
    else:
        print("Conta não encontrada.")

    conta = banco.buscar_conta("João")
    if conta:
        conta.deposito(200)
        conta.saque(100)
        print(f"Após operações, saldo de João: R${conta.saldo:.2f}")

    conta1 = banco.buscar_conta("João")
    conta2 = banco.buscar_conta("Maria")
    if conta1 and conta2:
        valor_transferido = 300
        conta1.saque(valor_transferido)
        conta2.deposito(valor_transferido)
        print(f"Após transferência, saldos: R${conta1.saldo:.2f} (João), R${conta2.saldo:.2f} (Maria)")

    print(f"Saldo total do banco: R${banco.saldo_total():.2f}")

    banco.remover_conta("Carlos")
    print("Contas após remoção de Carlos:")
    for conta in banco.listar_contas():
        print(conta)
