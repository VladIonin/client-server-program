import socket
import tkinter as tk
from tkinter import font


def change_image():
    server_host = entry.get()
    server_port = 9090
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    client_socket.sendall(b'change_image')
    client_socket.close()


window = tk.Tk()
window.iconbitmap("images/client-icon.ico")
window.title('Client Cat')
window.geometry('300x250')

window.resizable(width=False, height=False)
tk.Label().pack()

label = tk.Label()
label.pack()
label["text"] = "Введите IP сервера:"

entry = tk.Entry()
entry.pack(padx=8, pady=8)

btn = tk.Button(window, text='Кнопка', width=6, height=2, font=font.Font(size=24), bg='#d9544d', command=change_image)
btn.pack()

window.mainloop()
