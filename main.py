import time
import datetime


def cadastroDeUsuario():
    nome = input("digite seu nome:")
    idade = input("digite sua idade:")
    turma = input("fale sua turma:")
    curso = input("fale seu curso")
    completo = (f"olá {name}, você tem {idade} anos")
    print(completo)
    filme18(idade)

def filme18(idade):
    if idade <18:
        print("voce é de menor pode nao")
    else:
        print("safado")
    time.sleep(3)
    seucadastro(idade, nome, turma, curso)

def seucadastro():
    print("seu cadastro foi terminado")
    cadastroDeUsuario.append({"NOME":name,"idade": idade, });
    print("cadastro realizado!")
  
def ver_Cadastro(seucadastro)
    if not seucadastro:
       print("nenhum cadastro no sistema.")
    else:
       print("\n -----lista de cadastro-----")

       for i, pessoa in enumerate (cadastro, 1):
         print(f"{i}. Nome: {pessoa['Nome']}, Idade:
                  {pessoa ['idade']}, Turma: {pessoa ['Turma']}, Curso: {pessoa['Curso']}")

def main():
   


cadastroDeUsuario()