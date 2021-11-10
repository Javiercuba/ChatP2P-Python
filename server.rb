require "xmlrpc/server"

class ChatServer
  def initialize(port)
    @server = XMLRPC::Server.new(port)
    @server.add_handler("chat.set_nickname") do |nickname|
      @nickname = nickname
    end
    @server.add_handler("chat.send_message") do |message|
      @nickname + ": " + message
    end 
    @server.serve
  end
end

server = ChatServer.new(8000)