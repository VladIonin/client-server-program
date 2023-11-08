import tkinter as tk
from PIL import Image, ImageTk
import socket
import threading


def handle_client(client_socket, server_app):
    while True:
        data = client_socket.recv(1024).decode()

        if data == 'change_image':
            server_app.change_image()

        client_socket.close()

        break


class ServerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.iconbitmap("images/server-icon.ico")
        self.window.title('Server Cat')
        self.window.geometry('400x400')
        self.window.resizable(width=False, height=False)

        self.image1 = Image.open("images/image1.png")
        self.image2 = Image.open("images/image2.png")
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.current_image = self.photo1

        self.label = tk.Label(self.window, height=500, width=500, image=self.current_image)
        self.label.pack(expand=True)

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_host = socket.gethostbyname(socket.gethostname())
        server_port = 9090
        self.server_socket.bind((server_host, server_port))
        self.server_socket.listen(1)

        threading.Thread(target=self.accept_clients, daemon=True).start()

    def change_image(self):
        if self.current_image == self.photo1:
            self.current_image = self.photo2
        else:
            self.current_image = self.photo1

        self.label.config(image=self.current_image)

    def accept_clients(self):
        while True:
            client_socket, addr = self.server_socket.accept()

            threading.Thread(target=handle_client, args=(client_socket, self)).start()

    def run(self):
        self.window.mainloop()


server_app = ServerApp()
server_app.run()






