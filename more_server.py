from tkinter import *
import socket
import threading

class Ball:
    def __init__(self, canvas, name, color, **kw):
        self.canvas = canvas
        self.radius = kw.get('radius', 50)
        self.pos_x = kw.get('pos_x', 0)
        self.pos_y = kw.get('pos_y', 0)
        self.color = kw.get('color', color)
        self.name = name
        self.create()

    def calculate_ball_pos(self):
        x1 = self.pos_x
        x2 = self.pos_x + self.radius
        y1 = self.pos_y
        y2 = self.pos_y + self.radius
        return x1, y1, x2, y2

    def create(self):
        coords = self.calculate_ball_pos()
        self.ball = self.canvas.create_oval(coords[0], coords[1], coords[2], coords[3])
        self.canvas.itemconfig(self.ball, fill=self.color)

        label_x = (coords[0] + coords[2]) / 2
        label_y = (coords[1] + coords[3]) / 2
        self.label = self.canvas.create_text(label_x, label_y, text=self.name)
    

    def move(self, x=0, y=0):
        self.pos_x += x
        self.pos_y += y

        if self.pos_x < 0:
            self.pos_x = 0
        elif self.pos_x + self.radius > self.canvas.winfo_width():
            self.pos_x = self.canvas.winfo_width() - self.radius

        if self.pos_y < 0:
            self.pos_y = 0
        elif self.pos_y + self.radius > self.canvas.winfo_height():
            self.pos_y = self.canvas.winfo_height() - self.radius

        coords = self.calculate_ball_pos()
        self.canvas.coords(self.ball, coords[0], coords[1], coords[2], coords[3])
        label_x = (coords[0] + coords[2]) / 2
        label_y = (coords[1] + coords[3]) / 2
def key(event, ball):
    move_speed = 20
    if event == 'Up':
        ball.move(0, -move_speed)
    elif event == 'Down':
        ball.move(0, move_speed)
    elif event == 'Left':
        ball.move(-move_speed, 0)
    elif event == 'Right':
        ball.move(move_speed, 0)
    else:
        pass

def client_handler(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Received data from client: {data}")
        key(data, ball1)  # Call the key function for the ball1

# Create a list to hold all the client threads
client_threads = []

# Start the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))
server_socket.listen(5)  # Allow multiple clients to queue up

print(f"Server is listening on {host}:{port}...")

# Create the Tkinter window and canvas
root = Tk()
root.title('Ball_server')
mainCanvas = Canvas(root, width=500, height=500)
mainCanvas.grid()

while True:
    # Accept client connections
    client_socket, client_addr = server_socket.accept()
    print(f"Accepted connection from {client_addr}")
    name = client_socket.recv(1024).decode('utf-8')

    # Create a ball for each client and start a thread for the client handler
    ball1 = Ball(mainCanvas, name, 'green', pos_x=225, pos_y=100)
    client_thread = threading.Thread(target=client_handler, args=(client_socket,))
    client_threads.append(client_thread)
    client_thread.start()

# Start the Tkinter main loop
root.mainloop()

# Close the client sockets and wait for client threads to finish
for thread in client_threads:
    thread.join()
