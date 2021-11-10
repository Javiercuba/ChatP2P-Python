require 'xmlrpc/client'
require 'pp'

connection = XMLRPC::Client.new2("http://localhost:8000")

print "Digite seu nickname: "
nickname = gets.chomp

result = connection.call("chat.set_nickname", nickname)

while true
  print "# "
  message = gets.chomp
  result = connection.call("chat.send_message", message)
  pp result
end