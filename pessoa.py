'''
Criação da classe Pessoa para um sistema de controle de estoque
A classe pessoa contém: nome, endereço, cpf e data de nascimento

A função @property é um decorator integrado à função property() em Python.
O principal objetivo de qualquer decorador é alterar os métodos ou atributos de sua classe de forma
que o usuário de sua classe não precise fazer nenhuma alteração em seu código.
A função @property é usada para dar uma funcionalidade "especial" a certos métodos para fazer com que ajam como:
getters e setters (encapsulamento de dados) - adicionar lógica de validação para obter e definir um valor.
Para evitar o acesso direto a um campo da classe.
'''

class Pessoa:
    __slots__ = ['_nome', '_cpf', '_endereco', '_data_nascimento']

    def __init__(self, nome, endereco, cpf, data_nascimento):
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._nome = endereco

    @property
    def cpf(self):
        return self._cpf

    @property
    def data_nascimento(self):
        return self._data_nascimento