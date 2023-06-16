import socket, subprocess, time, tkinter as tk

HOST = '127.0.0.1'
PORT = 6886

def transfer_data(file_name: str):
  start_time = time.time()
  
  bytes_per = 1024
  line_count = 0

  if file_name == 'medium':
    bytes_per = 10240  
  elif file_name == 'large':
    bytes_per = 102400

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
      stream.connect((HOST, PORT))
      stream.sendall(file_name.encode("utf-8"))
        
      while True:
          data = stream.recv(bytes_per)
          if not data:
              break 
          line = data.decode("utf-8") 
          line_count += line.count('\n')
          with open(f'{file_name}.txt', 'a') as file:
              file.write(line)
        
      stream.sendall("end".encode("utf-8"))

  end_time = time.time()
  time_elapsed = end_time - start_time

  open_document(file_name)
  show_result(time_elapsed, file_name, line_count)

def open_document(file_name: str):
    try:
        subprocess.Popen(['explorer', f"{file_name}.txt"])
    except OSError:
        print("Não foi possível abrir o documento.")

def end_transmission():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
        stream.connect((HOST, PORT))
        stream.sendall("end".encode("utf-8"))

def show_result(time_elapsed: float, file_name: str, line_count: int):
    root = tk.Tk()
    root.title('Redes')
    root.geometry('1000x100')

    text = tk.Label(root, text=f"Tempo gasto na transferência do arquivo {file_name} que contem {line_count} linhas: {time_elapsed:.2f} segundos", font=('Arial', 16, 'bold'))
    text.pack(ipadx=10, ipady=10, pady=10)  

    root.mainloop()