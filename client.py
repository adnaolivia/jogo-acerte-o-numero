import Pyro4

def main():


    uri = input('Insira a URI do servidor: ')
    calculator = Pyro4.Proxy(uri)  

    print("3 + 5 =", calculator.add(3, 5))
    print("10 - 7 =", calculator.subtract(10, 7))

if __name__ == "__main__":
    main()