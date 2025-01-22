class Emprestimo:
    def __init__(self, id:str, valor_total: float, parcelas_totais: int):
        self.id = id
        self.valor_total = valor_total
        self.parcelas_totais = parcelas_totais
        self.valor_parcela = valor_total / parcelas_totais
        self.parcelas_pagas = 0
    
    
    def pagar(self, parcelas: int):
        self.parcelas_pagas += parcelas


    def __str__(self):
        print(f'id={self.id} | valor: R$ {self.valor_total: ,.2f}, | parcelas: {self.parcelas_pagas} / {self.parcelas_totais}')
        
        