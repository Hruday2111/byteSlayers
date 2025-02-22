# byteSlayers P2P Chat Application

A peer-to-peer chat application built with Python enabling direct communication between users across a network. Supports local testing and network deployment with mandatory message forwarding capabilities.

## Features
- Direct messaging between peers
- Message broadcasting to all connected peers
- Real-time peer discovery
- Mandatory message forwarding
- Thread-safe concurrent operations
- Command-line interface with emoji feedback

## Prerequisites
- Python 3.12.7
- Network connectivity for multi-computer deployment

## Installation
```bash
git clone https://github.com/Hruday2111/byteSlayers.git
cd byteSlayers
```

## Usage

### Local Testing
1. Open multiple terminals
2. In each terminal run:
```bash
python P2P.py
```
3. Use `127.0.0.1` as IP and different ports (e.g., 5001, 5002, 5003)

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
1. Send Message - Direct message to peer
2. Query Active Peers - View connected peers
3. Connect to Peers - Add new connections
4. Broadcast Message - Send to all peers
5. Disconnect from Peer - Remove connection
0. Quit - Exit application

## Troubleshooting

### Connection Refused
- Verify IP and port
- Check if target is running
- Review firewall settings

### Address Already in Use
- Try different port
- Wait for timeout
- Check port availability

## Team Members
- Hruday Amrit (230001051)
- Chebolu Durga Shanmukha Srikanth (230001018)
- Jothirmai (230003032)

## Acknowledgments
Developed for CS-216 Introduction to Blockchain under Dr. Subhra Mazumdar.