import time


def cadastroDeUsuario():
    name = input("digite seu nome: ")
    idade = int(input("digite sua idade: "))
    completo = (f"olá {name}, você tem {idade} anos")
    print(completo)
    filme18(idade)

def filme18(idade):
    if idade <18:
        print("voce é de menor pode nao")
    seucadastro(cadastroDeUsuario)

def seucadastro(name, idade):
    print("seu cadastro foi terminado")
    cadastroDeUsuario.append({"NOME": name, "idade": idade});



cadastroDeUsuario()