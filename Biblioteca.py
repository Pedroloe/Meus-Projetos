from abc import ABC, abstractmethod

class Usuario(ABC): #Clase Principal de Usuarios

    def __init__(self, nome, senha, matricula, email, data_de_entrada, limite_emprestimo, quantidade_emprestimos):
        self._nome = nome
        self._senha = senha
        self._matricula = matricula
        self._email = email
        self._data_de_entrada = data_de_entrada
        self._limite_emprestimo = limite_emprestimo
        self._quantidade_emprestimo = quantidade_emprestimos
        self._emprestimos = []

    def set_senha(self, senha):
        if len(senha) >= 8:
            self._senha = senha

    @abstractmethod
    def prazo_emprestimo(self):
        pass

class Aluno(Usuario): #Classe aluno herdando a classe Principal

    def __init__(self, nome, senha, matricula, email, data_de_entrada, curso, periodo):

        super().__init__(nome, senha, matricula, email, data_de_entrada, 5,)
        self._curso = curso
        self._periodo = periodo

    def get_curso(self):
        return self._curso

    def get_periodo(self):
        return self._periodo

    def consultar(self):
        pass

    def pegar_Livro(self):
        pass

    def devolver_Livro(self):
        pass

    def prazo_emprestimo(self):
        return 7

    def set_periodo(self, periodo):
        if periodo > 0:
            self._periodo = periodo



class Professor(Usuario): #Classe Professor herdando a classe Principal
    def __init__(self, nome, senha, matricula, email, data_de_entrada, departamento):
        super().__init__(nome, senha, matricula, email, data_de_entrada, 10)
        self._departamento = departamento

    def get_departamento(self):
        return self._departamento

    def consultar(self):
        pass
    def pegar_Livro(self):
        pass
    def devolver_Livro(self):
        pass
    def prazo_emprestimo(self):
        return 15

    def set_limite_emprestimo(self, limite_emprestimo):
        self._limite_emprestimo = limite_emprestimo

class Pesquisador(Usuario): #Classe Pesquisador herdando a classe Principal

    def __init__(self, nome, senha, matricula, email, data_de_entrada, pesquisa, projeto):
        super().__init__(nome, senha,matricula, email, data_de_entrada, 15)
        self._pesquisa = pesquisa
        self._projeto = projeto

    def get_pesquisa(self):
        return self._pesquisa

    def get_projeto(self):
        return self._projeto

    def consultar(self):
        pass
    def pegar_Livro(self):
        pass
    def devolver_Livro(self):
        pass
    def prazo_emprestimo(self):
        return 10

    def set_limite_emprestimo(self, limite_emprestimo):
        self._limite_emprestimo = limite_emprestimo


class Material(ABC): #Materiais da Biblioteca
    def __init__(self, codigo, titulo, autor, ano_publicacao):
        self._codigo = codigo
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao


    @abstractmethod
    def tipo_material(self):
        pass

class Livro(Material):

    def tipo_material(self):
        return "Livro"

class Revista(Material):

    def tipo_material(self):
        return "Revista"

class TCC(Material):

    def tipo_material(self):
        return "TCC"

class Ebook(Material):

    def tipo_material(self):
        return "Ebook"

class Emprestimo:

    def __init__(self, usuario, material, data_emprestimo, data_prevista, data_devolucao):
        self._usuario = usuario
        self._material = material
        self._data_emprestimo = data_emprestimo
        self._data_devolucao = data_devolucao
        self._data_prevista = data_prevista

    def set_data_emprestimo(self, data_emprestimo):
        self._data_emprestimo = data_emprestimo

    def set_data_devolucao(self, data_devolucao):
        self._data_devolucao = data_devolucao

class Multa:
    def __init__(self, usuario, material, valor, data_geracao, paga):
        self._usuario = usuario
        self._material = material
        self._valor = valor
        self._data_geracao = data_geracao
        self._paga = paga

    def get_usuario(self):
        return self._usuario

    def get_material(self):
        return self._material

    def get_valor(self):
        return self._valor

    def get_data_geracao(self):
        return self._data_geracao

    def get_paga(self):
        return self._paga

    def set_valor(self, valor):
        if valor >=0:
            self._valor = valor


class Biblioteca:

    def __init__(self):
        self._usuarios = []
        self._materiais = []
        self._emprestimos = []
        self._multas = []

    def cadastrar_usuario(self):
        pass

    def realizar_emprestimo(self, usuario):
        if len(usuario._emprestimos) < usuario._limite_emprestimo:
            print("Emprestimo Realizado!")

        else:
            print("Limite Excedido!")

    def devolver_material(self):
        pass
