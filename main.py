from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from tela_inicial import Tela_Inicial
from tela_cadastro import Tela_Cadastrar
from tela_buscar import Tela_Buscar

from pessoa import Pessoa
from cadastro import Cadastro


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastrar = Tela_Cadastrar()
        self.tela_cadastrar.setupUi(self.stack1)

        self.tela_buscar = Tela_Buscar()
        self.tela_buscar.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)


class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)

        #conexao de multitelas a partir da tela inicial criada

        self.cad = Cadastro()
        self.tela_inicial.pushButton.clicked.connect(self.abrirTelaCadastro)
        self.tela_inicial.pushButton_2.clicked.connect(self.abrirTelaBuscar)
        self.tela_inicial.pushButton_3.clicked.connect(self.sair)

        self.tela_cadastrar.pushButton.clicked.connect(self.botaoCadastra)
        self.tela_cadastrar.pushButton_2.clicked.connect(self.botaoVoltar)

        self.tela_buscar.pushButton_2.clicked.connect(self.botaoBusca)
        self.tela_buscar.pushButton.clicked.connect(self.botaoVoltar)

    def abrirTelaCadastro(self):     #Método para abrir a tela de cadastrar
        self.QtStack.setCurrentIndex(1)

    def abrirTelaBuscar(self):       #Método para abrir a tela de busca
        self.QtStack.setCurrentIndex(2)

    def botaoVoltar(self):          #Método para ativar o botão voltar
        self.QtStack.setCurrentIndex(0)

    def botaoCadastra(self):        #Método para ativar o botão cadastrar
        nome = self.tela_cadastrar.lineEdit.text()
        endereco = self.tela_cadastrar.lineEdit_2.text()
        cpf = self.tela_cadastrar.lineEdit_3.text()
        data_nascimento = self.tela_cadastrar.lineEdit_4.text()
        if not (nome == '' or endereco == '' or cpf == '' or data_nascimento == ''):
            pessoa = Pessoa(nome, endereco, cpf, data_nascimento)
            if (self.cad.cadastrarPessoa(pessoa)):
                QMessageBox.information(None, 'POO2', 'Cadastro realizado com sucesso :)')
                self.tela_cadastrar.lineEdit.setText('')
                self.tela_cadastrar.lineEdit_2.setText('')
                self.tela_cadastrar.lineEdit_3.setText('')
                self.tela_cadastrar.lineEdit_4.setText('')
            else:
                QMessageBox.information(None, 'POO2', 'O CPF informado já está cadastrado na base de dados!')
        else:
            QMessageBox.information(None, 'POO2', 'Ops, todos os valores devem ser preenchidos :(')

    def botaoBusca(self):        #Método para ativar o botão buscar
        cpf = self.tela_buscar.lineEdit.text()
        pessoa = self.cad.buscarPessoa(cpf)
        if (pessoa != None):
            self.tela_buscar.lineEdit_2.setText(pessoa.nome)
            self.tela_buscar.lineEdit_3.setText(pessoa.endereco)
            self.tela_buscar.lineEdit_4.setText(pessoa.data_nascimento)
        else:
            QMessageBox.information(None, 'POO2', 'Ops, CPF não encontrado :(')

    @staticmethod
    def sair():
        sys.exit(app.exec_())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
