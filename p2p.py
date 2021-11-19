from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import sys
from threading import Thread

chat = ''

class ChatService:
    def send_message(self, nickname, msg):
        global chat
        chat = '\n' + nickname + ': ' + msg
        print(chat)


def init_server():
    port = int(sys.argv[1])
    server = SimpleXMLRPCServer(('localhost', port), allow_none=True, logRequests=False)
    server.register_instance(ChatService())
    Thread(target=server.serve_forever).start()
    print('Servidor iniciado na porta {}'.format(port))
    
if __name__ == '__main__':
    try:
        init_server()
        port = input('Digite a porta do destinatário: ')
        nickname = input('Digite seu nickname: ')
        connection = xmlrpc.client.ServerProxy('http://localhost:%s' % port, allow_none=True)
        while True:
             msg = input('> ')
             if msg == 'sair':
                break
             connection.send_message(nickname, msg)
    except KeyboardInterrupt:
        print('Exiting')
