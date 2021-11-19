from xmlrpc.server import SimpleXMLRPCServer

chat = ''

class ChatService:     
    def send_message(self, nickname, msg):
        global chat
        chat = nickname + ': ' + msg

    def get_message(self):
        global chat
        return chat

if __name__ == '__main__':
    try:
        server = SimpleXMLRPCServer(("localhost", 7700),  allow_none=True)
        server.register_instance(ChatService())
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')