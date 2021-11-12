import rpyc
from rpyc.utils.server import ThreadedServer


class Client(rpyc.Service):

    def __init__(self,port):
        self.server = self.start_server(port)

    def start_server(self,port):
        server = ThreadedServer(Client, hostname="127.0.0.1", port=port)
        #server.start()
        return server



if __name__ == "__main__":
    port = input("Escolha uma porta")
    client = Client(port)
    c = rpyc.connect("localhost", port)
    nickname = input("Insira seu nickname: ")
    c.root.set_nickname(str(nickname))
    while True:
        msg = input("#")
        c.root.set_mensage(str(msg))
        client.start()