import socket
import subprocess
import time
import tkinter as tk
import threading

HOST = '127.0.0.1'
PORT = 6889

def transfer_data(file_name: str):
    start_time = time.time()

    BUFFER_SIZE = 1024 * 300
    line_count = 0

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        udp_socket.sendto(file_name.encode("utf-8"), (HOST, PORT))

        with open(f'{file_name}.txt', 'w') as file:
            while True:
                data, _ = udp_socket.recvfrom(BUFFER_SIZE)

                if data == b"End of File":
                    print("Arquivo terminado")
                    break

                line = data.decode("utf-8")
                line_count += 1
                file.write(line)

        udp_socket.sendto(b"EOF Received", (HOST, PORT))
        print("Confirmation sent")

    end_time = time.time()
    time_elapsed = end_time - start_time

    show_result(time_elapsed, file_name, line_count)
    open_document(file_name)

def open_document(file_name: str):
    try:
        subprocess.Popen(['explorer', f"{file_name}.txt"])
    except OSError:
        print("Não foi possível abrir o documento.")

def show_result(time_elapsed: float, file_name: str, line_count: int):
    root = tk.Tk()
    root.title('Redes')
    root.geometry('1000x100')

    text = tk.Label(
        root,
        text=f"Tempo gasto na transferência do arquivo {file_name} que contém {line_count} linhas: {time_elapsed:.2f} segundos",
        font=('Arial', 16, 'bold')
    )
    text.pack(ipadx=10, ipady=10, pady=10)

    root.mainloop()

def execute_transfer(file_name: str):
    transfer_thread = threading.Thread(target=transfer_data, args=(file_name,))
    transfer_thread.start()
