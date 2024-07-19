import Pyro4

def main():
    # Localizando o servidor de nomes e obtendo o URI do objeto remoto
    ns = Pyro4.locateNS()
    uri = ns.lookup("example.calculator1")
    calculator = Pyro4.Proxy(uri)  # Cria um proxy para o objeto remoto

    # Usando os métodos remotos
    print("3 + 5 =", calculator.add(3, 5))
    print("10 - 7 =", calculator.subtract(10, 7))

if __name__ == "__main__":
    main()

    # PYRO:Pyro.NameServer@10.25.2.66:9090