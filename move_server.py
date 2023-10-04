import tkinter as tk
import socket
import threading
import pickle

class Circle:
    def __init__(self, canvas, x, y, radius=20, color="blue"):
        self.canvas = canvas
        self.circle = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)

    def move(self, dx, dy):
        self.canvas.move(self.circle, dx, dy)

def handle_client(client_socket):
    global circles
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            # Deserialize the received data
            dx, dy = pickle.loads(data)
            for circle in circles:
                circle.move(dx, dy)
        except Exception as e:
            print(f"Error: {e}")
            break
    client_socket.close()

def accept_connections():
    while True:
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

# Create the main window
root = tk.Tk()
root.title("Move Circles")

# Create a canvas widget
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# Create a list to store circle objects
circles = []

# Bind the canvas to create circles on mouse click
def create_circle(event):
    x, y = event.x, event.y
    circle = Circle(canvas, x, y)
    circles.append(circle)

canvas.bind("<Button-1>", create_circle)

# Set up the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen(5)

print("Server listening on port 9999")

# Accept incoming client connections in a separate thread
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()

# Run the Tkinter event loop
root.mainloop()
