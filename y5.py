import socket

def main():
    host = '127.0.0.1'
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        message = input("Enter your message (type 'exit' to quit): ")
        client.send(message.encode())

        if message.lower() == 'exit':
            break

    client.close()

if __name__ == "__main__":
    main()
