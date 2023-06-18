import socket

HOST = '127.0.0.1'
PORT = 6886
FILE_PATH = "../ServTcp/database/small.txt"

def send_file_lines(client_socket, client_address):
    with open(FILE_PATH, 'r') as file:
        for line in file:
            client_socket.sendto(line.encode('utf-8'), client_address)
    
    client_socket.sendto(b'', client_address)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        udp_socket.bind((HOST, PORT))
        print(f"Servidor UDP iniciado em {HOST}:{PORT}")

        while True:
            data, client_address = udp_socket.recvfrom(1024)
            print(f"Solicitação recebida de {client_address}")

            if data.decode('utf-8') == 'get_file':
                send_file_lines(udp_socket, client_address)

if __name__ == '__main__':
    start_server()
