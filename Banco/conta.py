from emprestimo import Emprestimo

class Conta:
    def __init__(self, numero: str, titular: str):
        self.numero: str = numero
        self.titular: str = titular
        self.saldo: float = 0
        self.emprestimos: list[Emprestimo] = []
        
    
    def depositar(self, valor: float) -> True:
        self.saldo += valor
        return True
    

    def sacar(self, valor: float) -> True:
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False
    

    def realizar_emprestimo(self, id: str, valor: float, parcelas: int):
        emprestimo = Emprestimo(id=id, valor_total=valor, parcelas_totais=parcelas)
        self.emprestimos.append(emprestimo)
        self.depositar(valor=valor)
        pass
    
    
    def buscar_emprestimo(self, id: str) -> Emprestimo:
        for emprestimo in self.emprestimos:
            if emprestimo.id == id:
                return emprestimo
        return None
    
    
    def pagar_emprestimo(self, id_emprestimo: str, parcelas: int) -> bool:
        emprestimo = self.buscar_emprestimo(id_emprestimo)

        if emprestimo is None:
            return False  # não achou o empréstimo com o id fornecido
        
        parcelas_restantes = emprestimo.parcelas_totais - emprestimo.parcelas_pagas

        # Não paga parcelas a mais do que falta
        parcelas = min(parcelas, parcelas_restantes)

        if parcelas <= 0:
            return False  # Não há nada para pagar

        quantia_a_pagar = emprestimo.valor_parcela * parcelas
        
        if self.saldo >= quantia_a_pagar:  # Se há saldo
            self.saldo -= emprestimo.valor_parcela
            emprestimo.pagar()
            return True  # Conseguiu pagar as parcelas do empréstimo
        
        return False
    
    def __str__(self) -> str:
        return f'{self.numero} - Titular: {self.titular} | Saldo: R$ {self.saldo:,.2f}'
