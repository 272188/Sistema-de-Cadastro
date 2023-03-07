'''
Classe Cadastro possui uma lista vazia
Possui uma função/método para cadastrar e buscar
'''
class Cadastro:

    __slots__ = ['_lista']

    def __init__(self):
        self._lista = []

    def cadastrarPessoa(self, pessoa):
        verifica = self.buscarPessoa(pessoa.cpf)
        if verifica == None:
            self._lista.append(pessoa)
            return True
        else:
            return False

    def buscarPessoa(self, cpf):
        for x in self._lista:
            if x.cpf == cpf:
                return x
        return None