import socket
import time

HOST = '127.0.0.1'
PORT = 6889
BUFFER_SIZE = 1024 * 300

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
    udp_socket.bind((HOST, PORT))

    while True:
        data, address = udp_socket.recvfrom(BUFFER_SIZE)
        file_name = data.decode("utf-8")

        if file_name.lower() == "end":
            break

        with open(f"database/{file_name}.txt") as file:
            for line in file:
                udp_socket.sendto(line.encode('utf-8'), address)

        udp_socket.sendto(b"End of File", address)
        print(f"File {file_name} sent to {address}")

        confirmation, _ = udp_socket.recvfrom(BUFFER_SIZE)
        if confirmation == b"EOF Received":
            print(f"Confirmation received from {address}")
