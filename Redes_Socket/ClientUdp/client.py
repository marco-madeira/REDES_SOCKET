import tkinter as tk
from functions.transfer_data import execute_transfer

root = tk.Tk()
root.title('Redes UDP')
root.geometry('600x400')

text = tk.Label(root, text="Escolha o arquivo que deseja copiar", font=('Arial', 16, 'bold'))
small_button = tk.Button(root, text="Small", command=lambda: execute_transfer('small'), bg="blue", fg="white", font=('Arial', 12))
medium_button = tk.Button(root, text="Medium", command=lambda: execute_transfer('medium'), bg="green", fg="white", font=('Arial', 12))
large_button = tk.Button(root, text="Large", command=lambda: execute_transfer('large'), bg="orange", fg="white", font=('Arial', 12))

text.pack(ipadx=10, ipady=10, pady=10)
small_button.pack(ipadx=10, ipady=10, pady=10, fill=tk.X)
medium_button.pack(ipadx=10, ipady=10, pady=10, fill=tk.X)
large_button.pack(ipadx=10, ipady=10, pady=10, fill=tk.X)

root.mainloop()
