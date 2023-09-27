import socket
import tkinter as tk

def send_create_command():
    name = entry_name.get()
    color = entry_color.get()
    radius = entry_radius.get()
    request = f"CREATE {name} {color} {radius}"
    client_socket.send(request.encode())

def key(event):
    print(event.keysym)
    _key = event.keysym
    client_socket.send(_key.encode())

root = tk.Tk()
root.title('Client')

frame = tk.Frame(root)
frame.pack()

label_name = tk.Label(frame, text='Ten :')
label_name.grid(row=0, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

label_color = tk.Label(frame, text='Color:')
label_color.grid(row=1, column=0)
entry_color = tk.Entry(frame)
entry_color.grid(row=1, column=1)

label_radius = tk.Label(frame, text='radius:')
label_radius.grid(row=2, column=0)
entry_radius = tk.Entry(frame)
entry_radius.grid(row=2, column=1)

create_button = tk.Button(frame, text='create Circle', command=send_create_command)
create_button.grid(row=3, columnspan=2)
# root.bind('<Up>', key)
# root.bind('<Down>', key)
# root.bind('<Left>', key)
# root.bind('<Right>',key)
root.bind('<KeyPress>', key)

host = "127.0.0.1"
port = 2050

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

root.mainloop()
