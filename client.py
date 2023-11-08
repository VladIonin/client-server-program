import socket
import tkinter as tk
from tkinter import font


def change_image():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    client_socket.sendall(b'change_image')

    client_socket.close()


window = tk.Tk()
window.title('Client Cat')
window.geometry('400x400')

window.resizable(width=False, height=False)
server_host = input('Введите ip сервера: ')
server_port = 9090

btn = tk.Button(window, text='Кнопка', width=6, height=2, font=font.Font(size=24), bg='#d9544d', command=change_image)
btn.pack(expand=True)

window.mainloop()
