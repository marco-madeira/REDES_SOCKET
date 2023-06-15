import socket
import subprocess

HOST = '127.0.0.1'
PORT = 6886

def transfer_data(file_name: str):
  
  bytes_per = 1024

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
      with open(f'{file_name}.txt', 'a') as file:
        file.write(line)
    open_document(file_name)



def open_document(file_name: str):
    try:
        subprocess.Popen(['explorer', f"{file_name}.txt"])
    except OSError:
        print("Não foi possível abrir o documento.")

# file = input("What file do you wanna copy? ")
# bytes_per = 1024

# if file == 'medium':
#   bytes_per = 10240  
# elif file == 'large':
#   bytes_per = 102400


# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
#   stream.connect((HOST, PORT))
#   stream.sendall(bytes(file, "utf-8"))
#   while True:
#     data = stream.recv(bytes_per)
#     if not data:
#       break 
#     line = data.decode("utf-8") 
#     with open('large.txt', 'a') as file:
#       file.write(line)        