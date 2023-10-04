import socket
import pickle

def main():
    host = "localhost"  # Change to the server's IP address
    port = 9999

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    try:
        while True:
            
            
            # Serialize and send the delta values
            data = pickle.dumps((dx, dy))
            client.send(data)
    except KeyboardInterrupt:
        print("Closing the client.")
        client.close()

if __name__ == "__main__":
    main()
