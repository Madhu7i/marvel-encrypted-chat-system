# Marvel Encrypted Chat System
A multi-client chat application with AES encryption supporting both TCP and UDP protocols. Features Marvel character selection, multiple chat rooms, and concurrent user handling.

A secure, multi-client chat application featuring AES encryption with both TCP and UDP protocol implementations. Users can select Marvel characters and communicate across different themed chat rooms with real-time message broadcasting.

## 🚀 Features

- **Dual Protocol Support**: Both TCP and UDP implementations
- **AES-256 Encryption**: Secure message transmission with symmetric key cryptography
- **Multi-Client Architecture**: Concurrent handling of unlimited simultaneous users
- **Character Selection**: Choose from predefined Marvel characters or create custom names
- **Multiple Chat Rooms**: Three themed rooms (Stark Tower, Wakanda Labs, SHIELD Command)
- **Real-time Broadcasting**: Messages instantly delivered to all room participants
- **Name Validation**: Prevents duplicate usernames across the system
- **Thread-safe Operations**: Concurrent client handling with Python threading

## 🛠️ Technology Stack

- **Language**: Python 3.x
- **Encryption**: AES (Advanced Encryption Standard) with EAX mode
- **Networking**: Socket programming (TCP/UDP)
- **Concurrency**: Python threading
- **Encoding**: Base64 for secure data transmission

## 📋 Prerequisites

- Python 3.7 or higher
- pip package manager

## ⚡ Quick Start

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/marvel-encrypted-chat-system.git
   cd marvel-encrypted-chat-system
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Update IP Configuration:**
   - Open `tcp_server.py` and `udp_server.py`
   - Replace `'192.168.1.169'` with your server's IP address
   - Update the same IP in `tcp_client.py` and `udp_client.py`

### Running the Application

#### TCP Version
1. **Start the server:**
   ```bash
   python src/tcp_server.py
   ```

2. **Run clients (in separate terminals):**
   ```bash
   python src/tcp_client.py
   ```

#### UDP Version
1. **Start the server:**
   ```bash
   python src/udp_server.py
   ```

2. **Run clients (in separate terminals):**
   ```bash
   python src/udp_client.py
   ```

## 🎮 How to Use

### TCP Client
1. Select a Marvel character or enter a custom name
2. Start chatting - each message creates a new connection
3. Messages are displayed on the server console

### UDP Client
1. Choose your Marvel character
2. Select a chat room (Stark Tower, Wakanda Labs, or SHIELD Command)
3. Start chatting in real-time
4. Type "switch" to change character and room

### Server Management
- **TCP Server**: Automatically handles all incoming connections
- **UDP Server**: Select which chat room to monitor from the console

## 🔧 Configuration

### Security Settings
- **Encryption Key**: Modify the 16-byte key in all files (keep it consistent)
- **Port Configuration**: Default ports are 11000 (TCP) and 12000 (UDP)

### Network Settings
```python
# Update these variables in all files
serverIP = 'YOUR_SERVER_IP'        # Server IP address
serverPort = YOUR_PORT             # Port number
key = b'Your 16-byte key'          # Encryption key (must be 16 bytes)
```

## 📊 Architecture Overview

### TCP Implementation
- **Connection-oriented**: Reliable message delivery
- **Threading**: Each client handled in separate thread
- **Use Case**: Guaranteed message delivery scenarios

### UDP Implementation
- **Connectionless**: Fast, lightweight communication
- **Broadcasting**: Real-time message distribution
- **Use Case**: Real-time chat with multiple participants

### Security Layer
```
Client Message → AES Encryption → Base64 Encoding → Network Transmission
Server Receives → Base64 Decoding → AES Decryption → Message Processing
```

## 🔍 Code Structure

```
src/
├── encryption.py      # AES encryption/decryption functions
├── tcp_client.py      # TCP client implementation
├── tcp_server.py      # TCP server with threading
├── udp_client.py      # UDP client with room selection
└── udp_server.py      # UDP server with broadcasting
```

## 🚦 Testing

1. **Single Machine Testing**: Run server and multiple clients on localhost
2. **Network Testing**: Deploy server on one machine, clients on others
3. **Concurrent Testing**: Launch multiple clients simultaneously
4. **Security Testing**: Monitor encrypted traffic with network tools

## 🔐 Security Features

- **AES-256 Encryption**: Industry-standard symmetric encryption
- **Nonce Usage**: Prevents replay attacks
- **Key Management**: Shared secret key for client-server communication
- **Input Validation**: Username uniqueness and message formatting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Madhukar Anumula**
- LinkedIn: [Madhukar Anumula](https://www.linkedin.com/in/madhukar-anumula-996371248)
- Email: anumulamadhu22@gmail.com

## 🙏 Acknowledgments

- Marvel Characters used for demonstration purposes
- Crypto library for encryption implementation
- Python community for excellent documentation

---

⭐ **Star this repository if you found it helpful!**
