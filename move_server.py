import socket
import tkinter as tk
import threading
import random
import time

HOST = "127.0.0.1"
PORT = 2050

class Circle:
    def __init__(self, canvas, name, color, radius):
        self.canvas = canvas
        self.name = name
        self.color = color
        self.radius = radius
        self.create_circle()
        self.dx = 0  # Initialize speed to 0
        self.dy = 0
        self.move_interval = 100  # Time interval for moving the circle

    def create_circle(self):
        x = random.randint(self.radius, self.canvas.winfo_width() - self.radius)
        y = random.randint(self.radius, self.canvas.winfo_height() - self.radius)
        self.circle = self.canvas.create_oval(
            x - self.radius, y - self.radius,
            x + self.radius, y + self.radius,
            fill=self.color
        )
        self.label = self.canvas.create_text(x, y, text=self.name)

    def move(self):
        self.canvas.move(self.circle, self.dx, self.dy)
        self.canvas.move(self.label, self.dx, self.dy)
        self.check_boundary()
        self.canvas.after(self.move_interval, self.move)  # Schedule the next move

    def check_boundary(self):
        # Check if the circle hits the canvas boundary
        x1, y1, x2, y2 = self.canvas.coords(self.circle)
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        if x1 < 0 or x2 > canvas_width:
            self.dx = 0  # Stop horizontal movement
        if y1 < 0 or y2 > canvas_height:
            self.dy = 0  # Stop vertical movement

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print("Server is waiting for a client...")
    client, addr = server_socket.accept()
    print("Client connected from", addr)

    circle = None

    while True:
        try:
            data = client.recv(1024).decode()
            if not data:
                break
            circle = handle_command(data, circle)
            print(data)
        except Exception as e:
            print(e)
            break

    server_socket.close()
    root.quit()

def handle_command(command, circle):
    if command.startswith("CREATE"):
        _, name = command.split()#, color, radius_str
        radius = 30
        circle = Circle(canvas, name, "gold", radius)
        circle.move()
    elif circle is not None and command.startswith("MOVE"):
        _, x_str, y_str = command.split()
        x = int(x_str)
        y = int(y_str)
        move_circle(circle, x, y)
    
    return circle  # Return the updated circle

def move_circle(circle, x, y):
    if circle is not None:
        circle.dx = x  # Update the x-speed
        circle.dy = y  # Update the y-speed

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Server')

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    # Create a border around the canvas
    border_width = 1
    canvas.create_rectangle(
        border_width, border_width,
        canvas.winfo_width() - border_width,
        canvas.winfo_height() - border_width,
        outline="black", width=border_width
    )

    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    root.mainloop()
