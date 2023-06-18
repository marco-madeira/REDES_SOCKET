import socket

HOST = '127.0.0.1'
PORT = 6886

def receive_file_lines(server_socket):
    lines = []
    while True:
        data, _ = server_socket.recvfrom(1024)
        if not data:
            break
        lines.append(data.decode('utf-8'))

    return lines

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        udp_socket.sendto('get_file'.encode('utf-8'), (HOST, PORT))

        file_lines = receive_file_lines(udp_socket)

    for line in file_lines:
        with open("small.txt", 'a') as file:
              file.write(line)

if __name__ == '__main__':
    start_client()
