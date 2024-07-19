import Pyro4

# Definindo um objeto remoto
@Pyro4.expose
class Calculator(object):
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

# Inicializando o daemon Pyro4
def main():
    daemon = Pyro4.Daemon()  # Cria um daemon Pyro
    ns = Pyro4.locateNS()    # Localiza o servidor de nomes
    uri = daemon.register(Calculator)  # Registra o objeto remoto
    ns.register("example.calculator", uri)  # Registra o objeto no servidor de nomes
    print("Servidor está pronto.")
    daemon.requestLoop()  # Mantém o servidor rodando

if __name__ == "__main__":
    main()