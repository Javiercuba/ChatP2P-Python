import rpyc
from rpyc.utils.server import ThreadedServer


class MyService(rpyc.Service):

    def exposed_set_nickname(self, nickname):
        print(nickname)
        self.nickname = nickname
        

    def exposed_echo(self, message):
        print(message)


    def exposed_set_mensage(self, msg, nickname):
        global collection
        item_msg = {
                "dest": nickname,
                        "msg": self.nickname + ": " + msg
            }
        collection.insert_one(item_msg)
        # chat = self.nickname + ": " + msg
    def exposed_add(self, x, y):
        print('Result is: {}'.format(x + y))


if __name__ == "__main__":
    server = ThreadedServer(MyService, port=18830)
    server.start()
