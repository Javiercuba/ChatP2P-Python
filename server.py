import rpyc
from rpyc.utils.server import ThreadedServer

chat = ""
class MyService(rpyc.Service):

    def exposed_set_nickname(self, nickname):
        self.nickname = nickname
        
    def exposed_echo(self, message):
        print(message)

    def exposed_set_mensage(self, msg):
        global chat       
        chat = self.nickname + ": " + msg
        print(chat)

if __name__ == "__main__":
    server = ThreadedServer(MyService, port=18830)
    server.start()
