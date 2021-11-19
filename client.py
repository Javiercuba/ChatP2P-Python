import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:7700')

nickname = input('Nickname: ')

while True:
  msg = input('> ')
  if msg == 'sair':
    break
  s.send_message(nickname, msg)