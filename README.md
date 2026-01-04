<div align="center"> 
    
![ICR SCARS](screenshots/scars.png)

# ICR Chat Scars

</div>


---

## Features

- terminal-based anonymous chat
- multi-client support (50+ users)
- no message logging or storage
- real-time message broadcasting
- session data cleared on exit
- pure python (no dependencies)

---
## Screenshots

![Chat](screenshots/client.png)


---
## Quick Start

### Installation

```
cd ICR-Chat-Scars
```

```
pip install -r requirements.txt
```

Copy all Python files to their respective directories.

### Usage

**Start Server:**
```bash
python server.py
```
---
""new terminal""
**Start Client:**
```bash
python client.py
# Enter server IP (127.0.0.1 for localhost)
# Enter port (default: 50000)
# Enter username
```

---

## Configuration

Edit `config.py`:

```python
SERVER_CONFIG = {
    'host': '0.0.0.0',
    'port': 50000,
    'max_clients': 50
}

CLIENT_CONFIG = {
    'default_host': '127.0.0.1',
    'default_port': 50000,
    'max_message_length': 500
}
```

---

## Commands

| Command | Description |
|---------|-------------|
| `/help` | Show commands |
| `/quit` | Disconnect |
| `/exit` | Disconnect |
| `/q` | Quick disconnect |

---

## Network Setup

### Local Network (Same WiFi)

1. Find your IP:
   - Windows: `ipconfig`
   - Linux/Mac: `ifconfig` or `ip addr show`

2. Start server on your computer
3. Clients connect using your IP address

### Internet (Using ngrok)

1. Download ngrok: https://ngrok.com/download
2. Start server: `python server.py`
3. Start ngrok: `ngrok tcp 50000`
4. Share the ngrok URL and Port with friends

---

## Troubleshooting

**"Address already in use"**
- Change port in `config.py`
- Or kill the process using that port

**"Connection refused"**
- Check server is running
- Verify IP address and port


**Colors not showing (Windows)**
- Use Windows Terminal
- Or install: `pip install colorama`

---

## Project Structure

```
IRC-Chat-Scars/
├── server.py
├── client.py
├── config.py
├── handlers/
│   ├── client_handler.py
│   ├── message_handler.py
│   └── receive_handler.py
│   
├── utils/
│   ├── colors.py
│   
└── ui/
    ├── banner.py
    └── input_handler.py
```

---

## Requirements

- Python 3.9+
- No external dependencies (standard library only)

---

## Security Notes

- Messages are not encrypted
- No user authentication
- No message persistence
- Not recommended for sensitive information

---

## License

Unauthorized sharing is not allowed.

---
while {
developed by : leoniofficials; 
- just a drop star ✮
}
