import Pyro4

@Pyro4.expose
class Calculator(object):
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

# Inicializando o daemon Pyro4
def main():
    # ip_address = "ip_aqui"
    # port = 00000
    daemon = Pyro4.Daemon()  # Cria um daemon Pyro
    uri = daemon.register(Calculator)  # Registra o objeto remoto
    print("Servidor está pronto.")
    print(uri)
    daemon.requestLoop()  # Mantém o servidor rodando

if __name__ == "__main__":
    main()
