# byteSlayers P2P Chat Application

A peer-to-peer chat application built with Python that enables direct communication between users across a network. Features a simple command-line interface and supports both local testing and network deployment. The application also handles the bonus question effectively.

## Features
- Direct messaging between peers
- Message broadcasting to all connected peers
- Real-time peer discovery and connection management
- Automatic mandatory peer connections
- Thread-safe operations for concurrent message handling
- Non-blocking socket operations with select
- Automatic peer table management

## Prerequisites
- Python 3.12.7
- Basic understanding of networking concepts
- Network connectivity for multi-computer deployment

## Installation
```bash
git clone https://github.com/Hruday2111/byteSlayers.git
cd byteSlayers
```
No additional dependencies required - uses Python's standard library only.

## Usage

### Local Testing
1. Open multiple terminals
2. In each terminal run:
```bash
python P2P.py
```
3. When prompted:
   - Enter your team name
   - Enter a unique port number (e.g., 5001, 5002, 5003)
   - Your local IP will be automatically detected

### Network Deployment

#### Windows Firewall Setup
1. Open Windows Firewall (`wf.msc` or Control Panel)
2. Create Inbound Rule:
   - New Rule → Program
   - Browse to Python executable
   - Allow connection
   - Enable for all networks
3. Repeat for Outbound Rule

#### Running the Application
1. Find your IP:
```bash
ipconfig   # Windows
ifconfig   # Linux/Mac
```

2. Start the application:
```bash
python P2P.py
```

## Menu Options
1. Send Message - Send a direct message to a specific peer
2. Query Active Peers - View list of currently connected peers
3. Connect to Peers - Establish connection with new peers
4. Broadcast Message - Send a message to all connected peers
0. Quit - Exit the application

## Implementation Details
- Uses non-blocking sockets with `select` for efficient I/O
- Automatic peer discovery and connection management
- Threaded client handling for concurrent connections
- Maintains peer table for active connections
- Supports mandatory peer connections (configured in code)
- Automatic peer removal on disconnect

## Troubleshooting

### Connection Refused
- Verify the target IP and port are correct
- Ensure the target application is running
- Check firewall settings
- Verify network connectivity

### Address Already in Use
- Choose a different port number
- Wait a few minutes for the previous connection to timeout
- Check if another application is using the port

## Team Members
- Chebolu Srikanth                 (230001018)
- Hruday Amrit                     (230001051)
- Jothirmai                        (230003032)

## Acknowledgments
Developed for CS-216 Introduction to Blockchain under Dr. Subhra Mazumdar.