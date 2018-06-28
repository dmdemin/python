import socket

with socket.socket() as sock:
    sock.bind(("127.0.0.1", 10002))
    sock.listen()

    conn, addr = sock.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            break

        print(data.decode("utf8"))
