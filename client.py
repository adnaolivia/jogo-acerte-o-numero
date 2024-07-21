import Pyro4

def main():

    # ip_address = "ip_aqui"
    uri = input('Insira a URI do servidor: ')
    jogo = Pyro4.Proxy(uri)

    print("☆*: .｡. Bem vindo ao jogo! Será que você consegue acertar o número sorteado? .｡.:*☆")
    print("(●'◡'●)")
    while True:
        try:
            sugestao = int(input("Digite um número entre 1 e 100:\n"))
            resultado = jogo.sugestao(sugestao)
            print(resultado)
            if "Parabéns" in resultado:
                break
        except ValueError:
            print("Digite um número válido ¯\_(ツ)_/¯")

if __name__ == "__main__":
    main()