import tkinter as tk
from functions.transfer_data import transfer_data 

root = tk.Tk()
root.title('Redes')
root.geometry('400x300')

small_button = tk.Button(root, text="Small", command =lambda: transfer_data('small'))
medium_button = tk.Button(root, text="Medium", command =lambda: transfer_data('medium'))
large_button = tk.Button(root, text="Large", command =lambda: transfer_data('large'))

small_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
medium_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
large_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

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
     
root.mainloop()     
      

#   result = int.from_bytes(data, byteorder='big')

# print(f"Received {result!r}")  