import socket

HOST = '127.0.0.1'
PORT = 6886

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
    stream.bind((HOST, PORT))
    stream.listen()

    while True:  
        connection, address = stream.accept()
        with connection:
            print(f"Connected by {address}")
            data = connection.recv(1024)
            file_name = data.decode("utf-8")

            if file_name.lower() == "end":
                break

            with open(f"database/{file_name}.txt") as file:
                for line in file:
                    connection.sendall(line.encode('utf-8'))
