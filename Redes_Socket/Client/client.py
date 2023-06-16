import tkinter as tk
from functions.transfer_data import transfer_data 
from functions.transfer_data import end_transmission

root = tk.Tk()
root.title('Redes')
root.geometry('600x400')

text = tk.Label(root, text="Escolha o arquivo que deseja copiar", font=('Arial', 16, 'bold'))
small_button = tk.Button(root, text="Small", command=lambda: transfer_data('small'), bg="blue", fg="white", font=('Arial', 12))
medium_button = tk.Button(root, text="Medium", command=lambda: transfer_data('medium'), bg="green", fg="white", font=('Arial', 12))
large_button = tk.Button(root, text="Large", command=lambda: transfer_data('large'), bg="orange", fg="white", font=('Arial', 12))
end_button = tk.Button(root, text="Encerrar conexão", command=end_transmission, bg="red", fg="white", font=('Arial', 12, 'bold'))

text.pack(ipadx=10, ipady=10, pady=10)  
small_button.pack(ipadx=10, ipady=10, pady=10, fill=tk.X) 
medium_button.pack(ipadx=10, ipady=10, pady=10, fill=tk.X)
large_button.pack(ipadx=10, ipady=10, pady=10, fill=tk.X)
end_button.pack(ipadx=10, ipady=10, pady=10, fill=tk.X)


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