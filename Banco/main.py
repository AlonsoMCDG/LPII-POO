# 1) Desenvolva uma classe Agencia que possui uma
# lista de contas bancárias, mas as contas só 
# existem enquanto a agência existir. Adicione a 
# capacidade de fechar uma agência, excluindo 
# todas as contas associadas.

# 2) Implemente uma classe Emprestimo que está 
# diretamente associada a uma conta. A conta pode
# ter empréstimos vinculados. Adicione a 
# funcionalidade de pagar parcelas, diminuindo o 
# saldo da conta e reduzindo a dívida.

from agencia import Agencia

if __name__ == '__main__':
    bancoDoBrasil = Agencia(numero='0001')
    bancoDoBrasil.adicionar_conta(numero='10', titular='Alonso')
    bancoDoBrasil.adicionar_conta(numero='12', titular='Martins')

    print('Olá')
    bancoDoBrasil.listar_contas()
    bancoDoBrasil.encerrar_conta('10')
    bancoDoBrasil.listar_contas()

    print(type(bancoDoBrasil.contas))

    bancoDoBrasil.fechar_agencia()
    bancoDoBrasil.listar_contas()
    bancoDoBrasil.realizar_emprestimo(numero_conta='12', id_emprestimo='13', valor=10000, numero_parcelas=10)
    bancoDoBrasil.pagar_emprestimo(numero_conta='12', id_emprestimo='13', parcelas=2)

    
    