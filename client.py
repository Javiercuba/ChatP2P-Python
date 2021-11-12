import rpyc


if __name__ == "__main__":
    print("calling the server")
    c = rpyc.connect("localhost", 18830)
    c.root.echo("Hello Server")
    nickname = input("Insira seu nickname: ")
    c.root.set_nickname(str(nickname))
