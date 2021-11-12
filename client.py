import rpyc

connection = rpyc.connect("localhost", 18861)
exampleServerInstance = connection.root

nickname = input("Insira seu nickname: ")

exampleServerInstance.set_nickname(str(nickname))

while True:
	msg = input("#")
	exampleServerInstance.set_mensage(str(msg))