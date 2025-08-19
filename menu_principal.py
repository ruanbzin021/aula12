import runpy

def menu():
    while True:
        print("\n --Menu de opções--")
        print("1 - converter metros para centimetros")
        print("2 - calcular area circular")
        print("3 - calcular area do quadrado")
        print("0 - Sair")
        escolha = int(input("Escolha uma opcção: "))

        if escolha == 1:
            #runpy.run_path("5.py")   # é necessario usar o "import runpy" no começo do código
            exec(open("5.py").read()) # serve para executar funções de outros arquivos
            break

        elif escolha == 2:
            #runpy.run_path("6.py")
            exec(open("6.py").read())
            break

        elif escolha == 3:
            #runpy.run_path("7.py")
            exec(open("7.py").read())
            break

        elif escolha == 0:
            print("Você ira sair do menu!!!")
            break
        else:
            print("!!!Digite um numero valido!!!")

while True:
    menu()
    resposta = input("\n🔁 Deseja voltar ao menu? (s/n): ").strip().lower()
    if resposta != "s":
        print("\n👋 Obrigado! Até a próxima!")
        break

