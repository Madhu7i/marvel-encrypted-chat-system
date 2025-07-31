from socket import *
from encryption import encrypt_message  # Import encryption function

# Server configuration
serverName = 'localhost'  # Replace with the server's IP address
serverPort = 11000
key = b'Sixteen byte key'  # Same encryption key as in the server

# Get a unique name
while True:
    # Display predefined and custom name options
    print("Choose your Marvel character:")
    marvel_characters = ["Iron Man", "Thor", "Hulk", "Black Widow"]
    for i, character in enumerate(marvel_characters, 1):
        print(f"{i}. {character}")
    print("5. Enter a custom name")

    # Prompt the user for a name
    choice = int(input("Choose your character (1-5): "))
    if choice == 5:
        user_name = input("Enter your custom name: ")
    else:
        user_name = marvel_characters[choice - 1]

    # Send the name to the server for validation
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    check_message = f"CHECK_NAME:{user_name}"
    encrypted_check = encrypt_message(key, check_message)
    clientSocket.send(encrypted_check.encode('utf-8'))

    # Receive validation response
    response = clientSocket.recv(1024).decode('utf-8')
    clientSocket.close()
    if response == "NAME_ACCEPTED":
        print(f"Name '{user_name}' accepted!")
        break
    else:
        print(f"Name '{user_name}' is already taken. Please choose a different name.")

# Messaging loop
while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    message = input(f"[{user_name}]: ")
    formatted_message = f"{user_name}: {message}"
    encrypted_message = encrypt_message(key, formatted_message)
    clientSocket.send(encrypted_message.encode('utf-8'))

    # Receive acknowledgment
    response = clientSocket.recv(1024)
    print('From Server:', response.decode('utf-8'))
    clientSocket.close()
