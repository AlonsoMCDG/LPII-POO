from conta import Conta
from emprestimo import Emprestimo

class Agencia:
    def __init__(self, numero: str):
        self.numero: str = numero
        self.contas: list[Conta] = []
        self.aberta:bool = True
    
    
    def adicionar_conta(self, numero: str, titular: str) -> bool:
        if not self.aberta:
            return False
        
        self.contas.append(Conta(numero=numero, titular=titular))
        return True
    
    
    def listar_contas(self) -> bool:
        print(f'Contas da agência {self.numero}:')
        if not self.aberta:
            print('<Agência fechada>')
            return False

        for conta in self.contas:
            print(conta) 
        
        if len(self.contas) == 0:
            print('<Nao há contas>')

        return True
    
    def buscar_conta(self, numero: str):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        
        return None
    
    
    def realizar_emprestimo(self, numero_conta: str, id_emprestimo: str, valor: float, numero_parcelas: int):
        conta = self.buscar_conta(numero_conta)
        
        if conta is None:
            print('Conta não encontrada')
            return False

        conta.realizar_emprestimo(id_emprestimo, valor, numero_parcelas)
        return True
    
    
    def pagar_emprestimo(self, numero_conta: str, id_emprestimo: str, parcelas: int):
        conta = self.buscar_conta(numero_conta)
        return conta.pagar_emprestimo(id_emprestimo, parcelas)
        
    
    def encerrar_conta(self, numero: str) -> bool:
        for i in range(len(self.contas) - 1, -1, -1):
            if self.contas[i].numero == numero:
                del(self.contas[i])
                return True
        return False # Não achou a conta
    
    
    def fechar_agencia(self):
        for i in range(len(self.contas) - 1, -1, -1):
            del(self.contas[i])
        self.aberta = False
    
