from socket import *
from encryption import decrypt_message  # Import decryption function
from collections import defaultdict
import threading

# Server configuration
server_name = 'localhost'  # Replace this with your server's IP
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((server_name, serverPort))
print(f"Marvel-Themed Chat Server is ready to receive messages on {server_name}:{serverPort}...")

# Track unique names
used_names = set()

# Chat room data
chat_rooms = defaultdict(set)
key = b'Sixteen byte key'  # Same encryption key as the client

# Global variable to keep track of the selected room
selected_room = None

def display_messages():
    """Function to display messages from the selected chat room."""
    global selected_room
    while True:
        encrypted_message, clientAddress = serverSocket.recvfrom(2048)
        encrypted_message = encrypted_message.decode('utf-8')

        try:
            decrypted_message = decrypt_message(key, encrypted_message)
            if decrypted_message.startswith("CHECK_NAME:"):
                # Name verification logic
                user_name = decrypted_message.split(":", 1)[1].strip()
                if user_name in used_names:
                    response = "NAME_TAKEN"
                else:
                    used_names.add(user_name)
                    response = "NAME_ACCEPTED"
                serverSocket.sendto(response.encode('utf-8'), clientAddress)
            else:
                # Handle regular messages
                room_name, client_message = decrypted_message.split('|', 1)
                chat_rooms[room_name].add(clientAddress)

                # Display messages only if they are from the selected room
                if room_name == selected_room:
                    print(f"[{room_name}] {client_message.strip()}")

                # Broadcast the message to all clients in the same room
                for client in chat_rooms[room_name]:
                    if client != clientAddress:
                        serverSocket.sendto(encrypted_message.encode('utf-8'), client)
        except Exception as e:
            print(f"Error processing message: {e}")

def select_chat_room():
    """Function to select the chat room to monitor."""
    global selected_room
    available_rooms = ["Stark Tower", "Wakanda Labs", "SHIELD Command"]

    while True:
        print("\nAvailable Chat Rooms:")
        for i, room in enumerate(available_rooms, 1):
            print(f"{i}. {room}")
        try:
            choice = int(input("Select the chat room to monitor (1-3): "))
            if 1 <= choice <= len(available_rooms):
                selected_room = available_rooms[choice - 1]
                print(f"Now monitoring messages in: {selected_room}")
                break
            else:
                print("Invalid choice. Please select a valid room.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def monitor_chat_rooms():
    """Main function to manage chat room monitoring."""
    while True:
        select_chat_room()
        print("Type 'switch' to change the chat room.")
        while True:
            command = input("Command: ").strip().lower()
            if command == "switch":
                break

# Start the chat room management and message display
room_management_thread = threading.Thread(target=monitor_chat_rooms)
room_management_thread.daemon = True
room_management_thread.start()

display_messages()  # Run the message display in the main thread
