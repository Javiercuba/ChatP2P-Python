import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:7700')

last_msg = ''
while True:
  if last_msg != s.get_message():
      print(s.get_message())
      last_msg = s.get_message()