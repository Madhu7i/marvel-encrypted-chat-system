from socket import *
from encryption import encrypt_message  # Import encryption function

# Server configuration
serverName = 'localhost'  # Replace with your server's IP
serverPort = 12000
key = b'Sixteen byte key'  # Same encryption key as in the server

# Predefined Marvel Characters
marvel_characters = ["Iron Man", "Spider-Man", "Thor", "Hulk", "Black Widow"]
chat_rooms = ["Stark Tower", "Wakanda Labs", "SHIELD Command"]

def get_unique_name():
    """Function to ensure the client selects a unique name."""
    while True:
        # Display character options
        print("Choose your Marvel character:")
        for i, character in enumerate(marvel_characters, 1):
            print(f"{i}. {character}")
        print("6. Enter a custom name")

        # Get user choice
        choice = int(input("Choose your character (1-6): "))
        if choice == 6:
            user_name = input("Enter your custom name: ")
        else:
            user_name = marvel_characters[choice - 1]

        # Check name availability with the server
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        check_message = f"CHECK_NAME:{user_name}"
        encrypted_check = encrypt_message(key, check_message)
        clientSocket.sendto(encrypted_check.encode('utf-8'), (serverName, serverPort))

        # Receive response from the server
        response, _ = clientSocket.recvfrom(2048)
        response = response.decode('utf-8')
        if response == "NAME_ACCEPTED":
            print(f"Name '{user_name}' accepted!")
            return user_name
        else:
            print(f"Name '{user_name}' is already taken. Please choose a different name.")

def select_chat_room():
    """Function to select a chat room."""
    print("Available Chat Rooms:")
    for i, room in enumerate(chat_rooms, 1):
        print(f"{i}. {room}")
    return chat_rooms[int(input("Select your chat room (1-3): ")) - 1]

def main():
    """Main function to handle the chat."""
    user_name = get_unique_name()
    chat_room = select_chat_room()

    clientSocket = socket(AF_INET, SOCK_DGRAM)
    print(f"You joined the chat room: {chat_room}")

    while True:
        message = input(f"[{user_name} in {chat_room}]: ")
        if message.lower() == "switch":
            print("Switching character and chat room...")
            main()  # Restart the process
            break

        # Encrypt and send the message
        formatted_message = f"{chat_room}|[{user_name}]: {message}"
        encrypted_message = encrypt_message(key, formatted_message)
        clientSocket.sendto(encrypted_message.encode('utf-8'), (serverName, serverPort))

# Start the client
main()
