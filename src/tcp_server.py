from socket import *
from encryption import decrypt_message  # Import decryption function
import threading

# Server Configuration
serverIP = 'localhost'  # Replace with the server's actual IP address
serverPort = 11000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(5)  # Allow up to 5 simultaneous connections
print(f'The server is ready to receive on {serverIP}:{serverPort}')

key = b'Sixteen byte key'  # Ensure this key matches the client's encryption key
used_names = set()  # Store unique names of connected clients


# Function to handle each client connection
def handle_client(connectionSocket, addr):
    try:
        # Receive the encrypted message
        encrypted_message = connectionSocket.recv(1024).decode('utf-8')
        decrypted_message = decrypt_message(key, encrypted_message)

        # Ensure the first message is the name
        if decrypted_message.startswith("CHECK_NAME:"):
            name = decrypted_message.split(":", 1)[1].strip()
            if name in used_names:
                # Notify the client the name is taken
                connectionSocket.send(b"NAME_TAKEN")
            else:
                # Add the name to the used_names set
                used_names.add(name)
                connectionSocket.send(b"NAME_ACCEPTED")
            return

        # Process regular messages
        character_name, message = decrypted_message.split(':', 1)
        print(f"[{character_name.strip()}]: {message.strip()}")

        # Acknowledge the message
        connectionSocket.send(b"Message received")
    except Exception as e:
        print(f"Error handling message: {e}")
    finally:
        connectionSocket.close()


# Main server loop
while True:
    connectionSocket, addr = serverSocket.accept()
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
    client_thread.start()
