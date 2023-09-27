import socket
import tkinter as tk
import threading
import random
HOST = "127.0.0.1"
PORT = 2050

class Circle:
    def __init__(self, canvas, name, color, radius):
        self.canvas = canvas
        self.name = name
        self.color = color
        self.radius = radius
        self.create_circle()

    def create_circle(self):
        x = random.randint(self.radius, self.canvas.winfo_width() - self.radius)  # Random x within canvas width
        y = random.randint(self.radius, self.canvas.winfo_height() - self.radius)  # Random y within canvas height
        self.circle = self.canvas.create_oval(
            x - self.radius, y - self.radius,
            x + self.radius, y + self.radius,
            fill=self.color
        )
        self.label = self.canvas.create_text(x, y, text=self.name)

def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print("Server is waiting for a client...")
    client, addr = server_socket.accept()
    print("Client connected from", addr)

    while True:
        try:
            data = client.recv(1024).decode()
            if not data:
                break
            handle_command(data)
            print(data)
        except Exception as e:
            print(e)
            break

    server_socket.close()
    root.quit()

def handle_command(command):
    if command.startswith("CREATE"):
        _, name, color, radius_str = command.split()
        radius = int(radius_str)
        Circle(canvas, name, color, radius)

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Server')

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    root.mainloop()
