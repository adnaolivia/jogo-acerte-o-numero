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

# PYRO:obj_675b7fe49c5d4069ab4858b3c113fc9e@localhost:50363