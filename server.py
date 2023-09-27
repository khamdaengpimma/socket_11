import socket
import tkinter as tk
import threading
import random
HOST = "127.0.0.1"
PORT = 2050

class Circle:
    def __init__(self, canvas, name, color, radius,):
        self.canvas = canvas
        self.name = name
        self.color = color
        self.radius = radius
        self.x = int(random.randint(self.radius, self.canvas.winfo_width() - self.radius))
        self.y  = int(random.randint(self.radius, self.canvas.winfo_height() - self.radius))
        self.create_circle()

    def create_circle(self):
        x1 = self.x - self.radius
        y1 = self.y - self.radius
        x2 = self.x + self.radius
        y2 = self.y + self.radius
        self.circle = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color)
        self.label = self.canvas.create_text(self.x, self.y, text=self.name)

    def move(self, x=0, y=0):
    #     self.x += x
    #     self.y += y
            print(x,y)

    #     # Limit the circle's movement within the canvas
    #     if self.x < self.radius:
    #         self.x = self.radius
    #     elif self.x + self.radius > self.canvas.winfo_width():
    #         self.x = self.canvas.winfo_width() - self.radius

    #     if self.y < self.radius:
    #         self.y = self.radius
    #     elif self.y + self.radius > self.canvas.winfo_height():
    #         self.y = self.canvas.winfo_height() - self.radius

    #     self.canvas.move(self.circle, x, y)
    #     label_x = self.x
    #     label_y = self.y
    #     self.canvas.coords(self.label, label_x, label_y)


def key(event):
    print("event : ",event)
    move_speed = 20
    if event == 'Up':
        Circle.move(0, -move_speed)
    elif event == 'Down':
        Circle.move(0, move_speed)
    elif event == 'Left':
        Circle.move(-move_speed, 0)
    elif event == 'Right':
        Circle.move(move_speed, 0)
    else:
        pass

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
    else:
        key(command)
        print(command)

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Server')

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    root.mainloop()
