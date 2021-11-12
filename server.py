import rpyc
from rpyc.utils.server import ThreadedServer


class P2P(rpyc.Service):
    known_hosts = []

    def __init__(self):
        self.known_hosts = [9000, 9001, 9002]

    def get_hosts(self):
        return self.known_hosts

    def update_hosts(self):
        temp_hosts = []
        for host in self.known_hosts:
            try:
                temp_hosts.append(rpyc.connect(
                    "localhost", host).root.get_hosts())
            except:
                pass
        self.known_hosts = self.known_hosts.append(temp_hosts)

    def exposed_set_nickname(self, nickname):
         self.nickname = nickname

    def exposed_echo(self, message):
         print(message)

    def exposed_set_mensage(self, msg):
         global chat
         chat = self.nickname + ": " + msg
         print(chat)
    

if __name__ == "__main__":
    port = input("Port: ")
    server = ThreadedServer(P2P, hostname="127.0.0.1", port=port)
    server.start()
