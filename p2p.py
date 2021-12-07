from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
from threading import Thread


class MessageService:
    def __init__(self, nickname):
        self.nickname = nickname

    def send_message(self, sender, message):
        print('\n{} -> {}:\n{}'.format(sender, self.nickname, message))


class Peer:
    def __init__(self, nickname, address, port):
        self.address = address
        self.port = port
        self.nickname = nickname
        self.known_peers = []
        self.init_server()

    def init_server(self):
        server = SimpleXMLRPCServer(
            (self.address, self.port), allow_none=True, logRequests=False)
        server.register_instance(MessageService(self.nickname))
        self.threaded_server = Thread(target=server.serve_forever)
        self.threaded_server.setDaemon(True)
        self.threaded_server.start()
        print('Servidor de {} iniciado em {}:{}'.format(
            self.nickname, self.address, self.port))

    def connect_to_peer(self, new_peer):
        if new_peer not in self.my_peers():    # se o peer não estiver na minha lista...
            self.known_peers.append(new_peer)  # adicione-o
            new_peer.known_peers.append(self)  # e vice-versa
            print('{} conectado a {}'.format(self.nickname, new_peer.nickname))

            # verificar minha lista para que o novo par faça conexão com outros pares
            for other_peer in self.my_peers():
                if other_peer not in new_peer.my_peers() and other_peer is not new_peer:
                    new_peer.connect_to_peer(other_peer)


    def my_peers(self):
        return self.known_peers

    def send_message(self, index_of_peer, msg):
        receiver = self.known_peers[index_of_peer]
        connection = xmlrpc.client.ServerProxy(
            'http://{}:{}'.format(receiver.address, receiver.port))
        connection.send_message(self.nickname, msg)


if __name__ == '__main__':
    # Criando instâncias dos peers
    p1 = Peer('Guilherme', 'localhost', 5000)
    p2 = Peer('Maria', 'localhost', 5001)
    p3 = Peer('Javier', 'localhost', 5002)

    # Fazendo as conexões entre os peers
    p1.connect_to_peer(p2)
    p1.connect_to_peer(p3)

    # Envio das mensagens
    p1.send_message(0, 'Olá, tudo bem?')
    p2.send_message(1, 'Oi, tudo bom?')
    p3.send_message(1, 'Tudo e você?')
