import rpyc

connection = rpyc.connect("localhost", 18861)
exampleServerInstance = connection.root
exampleServerInstance.set_nickname("Fighters")

while True:

    msg = exampleServerInstance.get_mensage()
    if msg != None:
        print msg
