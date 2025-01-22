from funcionario import Funcionario
from projeto import Projeto
from datetime import datetime

class FuncionarioProjeto:
    def __init__(self, funcionario: Funcionario, papel: str, projeto: Projeto, data_inicio: datetime):
        self.funcionario: Funcionario = funcionario
        self.papel: str = papel
        self.projeto: Projeto = projeto
        self.data_inicio: datetime = data_inicio
    
    def __str__(self):
        return f'{self.funcionario} é {self.papel} em {self.projeto}'
    