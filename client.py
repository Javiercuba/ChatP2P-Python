import rpyc


if __name__ == "__main__":
    c = rpyc.connect("localhost", 18830)
    c.root.echo("Hello Server")
    nickname = input("Insira seu nickname: ")
    c.root.set_nickname(str(nickname))
    while True:
        msg = input("#")
        c.root.set_mensage(str(msg))
