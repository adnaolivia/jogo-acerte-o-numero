import Pyro4
import random

@Pyro4.expose
class AdivinheoNumero(object):
    def __init__(self):
        self.novo_jogo()
    
    def novo_jogo(self):
        self.numero_sorteado = random.randint(1, 10) # sorteia aleatoriamente um inteiro entre 1 e 100
        self.tentativas = 0 # inicia em 0, depois vai iterando ate acertar
    
    def sugestao(self, numero):
        self.tentativas += 1 # soma uma nova tentativa a cada erro
        if numero < self.numero_sorteado:
            return "Tente um número MAIS ALTO!¯\_(ツ)_/¯\n"
        elif numero > self.numero_sorteado:
            return "Tente um número MAIS BAIXO!¯\_(ツ)_/¯\n"
        else:
            resultado = f"Parabéns, depois de {self.tentativas} tentativas!╰(*°▽°*)╯"
            self.novo_jogo()
            return resultado

# Inicializando o daemon Pyro4
def main():
    # ip_address = "ip_aqui"
    # port = 00000
    daemon = Pyro4.Daemon()  # Cria um daemon Pyro
    uri = daemon.register(AdivinheoNumero)  # Registra o objeto remoto
    print("Servidor está pronto.")
    print(uri)
    daemon.requestLoop()  # Mantém o servidor rodando

if __name__ == "__main__":
    main()
