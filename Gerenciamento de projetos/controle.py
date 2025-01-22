from projeto import Projeto
from funcionario import Funcionario

class Controle:
    def __init__(self):
        self.funcionarios: list[Funcionario] = []
        self.projetos: list[Projeto] = []
    
    def novo_funcionario(self, id: str, nome: str, cargo: str):
        self.funcionarios.append(Funcionario(id, nome, cargo))
    
    def novo_projeto(self, id: str, nome: str, descricao: str = 'Sem descrição.'):
        self.projetos.append(Projeto(id, nome, descricao))
    
    def listar_projetos(self):
        print('Projetos ativos:')
        t = len(str(len(self.projetos)))
        for i, projeto in enumerate(self.projetos):
            print(f'{i: >{t}}. {projeto}')
    
    def listar_funcionarios(self):
        print('Funcionários cadastrados:')
        t = len(str(len(self.funcionarios)))
        for i, funcionario in enumerate(self.funcionarios):
            print(f'{i: >{t}}. {funcionario}')
    