# python eventm.py

from imports import *

def limpar():
    os.system("cls")  

def pausar():
    input("\nPressione ENTER para voltar ao menu...")

def menu():
    while True:
        limpar()

        print("===============================")
        print("SISTEMA DE EVENTO MUSICAL")
        print("===============================")
        print("1 - Listar eventos")
        print("2 - Listar ingressos")
        print("3 - Cadastrar participante")
        print("4 - Ver participantes de um evento")
        print("5 - Excluir participante")
        print("6 - Editar participante")   
        print("7 - Sair")                 
        print("===============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar()
            listar_eventos()
            pausar()

        elif opcao == "2":
            limpar()
            listar_ingressos()
            pausar()

        elif opcao == "3":
            limpar()
            cadastrar_participante()
            pausar()

        elif opcao == "4":
            limpar()
            listar_participantes()
            pausar()

        elif opcao == "5":
            limpar()
            print("Excluir participante:")
            print("a - Por CPF")
            print("b - Por email")
            escolha = input("Escolha: ")

            if escolha == "a":
                cpf = input("Digite o CPF: ")
                excluir_participante_por_cpf(cpf)

            elif escolha == "b":
                email = input("Digite o email: ")
                excluir_participante_por_email(email)

            else:
                print("Opção inválida.")

            pausar()

        elif opcao == "6":       
            limpar()
            editar_participante()
            pausar()

        elif opcao == "7":       
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida.")
            pausar()


if __name__ == "__main__":
    if login_admin():
        menu()
    else:
        print("Encerrando o sistema.")
