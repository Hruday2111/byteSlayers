import socket
import threading
import time
import select

class PeerChat:
    def __init__(self):
        self.peer_table = []  # List of (IP, port) tuples for connected peers
        self.running = True   # Application running state
        self.team_name = ""
        self.server_port = 0
        self.local_ip = None
        # Mandatory peer connection (assignment requirement)
        self.mandatory_ips = [("10.206.5.228", 6555)]
        self.server_socket = None

    def start_server(self, port):
        """Initialize and run the TCP server to accept incoming connections."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('', port))
        self.server_socket.listen(5)
        self.server_socket.setblocking(False)
        print(f"Server listening on port {port}")
        
        while self.running:
            try:
                # Wait up to 1 second for an incoming connection
                ready_to_read, _, _ = select.select([self.server_socket], [], [], 1)
                if ready_to_read:
                    client, addr = self.server_socket.accept()
                    client.setblocking(False)
                    threading.Thread(target=self.handle_client, args=(client,)).start()
            except Exception as e:
                if self.running:
                    print(f"Error accepting connection: {e}")
                break

    def handle_client(self, client):
        """Handle incoming messages from a connected client."""
        while self.running:
            try:
                # Wait for client data (timeout: 1 second)
                ready_to_read, _, _ = select.select([client], [], [], 1)
                if ready_to_read:
                    data = client.recv(1024).decode()
                    if not data:
                        break

                    parts = data.split(' ', 2)
                    if len(parts) < 3:
                        continue

                    ip_port, team, message = parts
                    ip, port = ip_port.split(':')
                    port = int(port)

                    # Ignore messages from self
                    if ip == self.local_ip and port == self.server_port:
                        continue

                    # Process an "exit" message by removing the peer
                    if message.strip().lower() == "exit":
                        print(f"\n[{time.strftime('%H:%M:%S')}] {ip_port} {team}: {message} (peer disconnected)")
                        if (ip, port) in self.peer_table:
                            self.peer_table.remove((ip, port))
                        break

                    # Add new peer if not already connected
                    if (ip, port) not in self.peer_table:
                        self.peer_table.append((ip, port))

                    print(f"\n[{time.strftime('%H:%M:%S')}] {ip_port} {team}: {message}")
                    print(">> ", end='', flush=True)
            except Exception as e:
                print(f"Error handling client: {e}")
                break
        client.close()

    def send_message(self, ip, port, message):
        """Send a formatted message to a specified peer."""
        try:
            with socket.create_connection((ip, port), timeout=2) as sock:
                formatted = f"{self.local_ip}:{self.server_port} {self.team_name} {message}"
                sock.sendall(formatted.encode())
        except Exception as e:
            print(f"Error sending to {ip}:{port} - {e}")

    def broadcast_message(self, message):
        """Send a message to all connected peers."""
        for ip, port in self.peer_table:
            self.send_message(ip, port, message)

    def connect_to_peer(self, ip, port):
        """Connect to a peer and send a handshake message."""
        try:
            with socket.create_connection((ip, port), timeout=2) as sock:
                handshake_msg = f"{self.local_ip}:{self.server_port} {self.team_name} handshake"
                sock.sendall(handshake_msg.encode())
            if (ip, port) not in self.peer_table:
                self.peer_table.append((ip, port))
            print(f"Successfully connected to {ip}:{port}")
        except Exception as e:
            print(f"Connection failed to {ip}:{port} - {e}")

    def cleanup(self):
        """Terminate the server operation and close the socket."""
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        print("Shutting down...")

    def menu_interface(self):
        """Display the command-line menu and process user input."""
        while self.running:
            print("\n***** Menu *****")
            print("1. Send message")
            print("2. Query active peers")
            print("3. Connect to active peers")
            print("4. Broadcast message")
            print("0. Quit")
            choice = input("Enter choice: ")
            if choice == '1':
                self.send_message_flow()
            elif choice == '2':
                self.query_peers()
            elif choice == '3':
                self.connect_interface()
            elif choice == '4':
                message = input("Enter message to broadcast: ")
                self.broadcast_message(message)
            elif choice == '0':
                self.cleanup()
                break

    def send_message_flow(self):
        """Prompt user for recipient details and send a message."""
        ip = input("Recipient IP: ")
        port = int(input("Recipient port: "))
        message = input("Your message: ")
        self.send_message(ip, port, message)

    def query_peers(self):
        """Print a list of currently connected peers."""
        print("\nActive Peers:")
        if not self.peer_table:
            print("No connected peers")
            return
        for idx, (ip, port) in enumerate(self.peer_table, 1):
            print(f"{idx}. {ip}:{port}")

    def connect_interface(self):
        """Prompt user for peer details and attempt a connection."""
        ip = input("Peer IP: ")
        port = int(input("Peer port: "))
        self.connect_to_peer(ip, port)

    def start(self):
        """Initialize the application, start the server, and run the menu interface."""
        self.team_name = input("Enter your team name: ")
        self.server_port = int(input("Enter your port number: "))
        self.local_ip = socket.gethostbyname(socket.gethostname())
        print(f"Local IP is {self.local_ip}")
        
        # Connect to mandatory peers
        for ip, port in self.mandatory_ips:
            if (ip, port) not in self.peer_table:
                self.connect_to_peer(ip, port)
        
        server_thread = threading.Thread(target=self.start_server, args=(self.server_port,))
        server_thread.daemon = True
        server_thread.start()
        self.menu_interface()

if __name__ == "__main__":
    # Launch the peer-to-peer chat application
    chat = PeerChat()
    chat.start()
