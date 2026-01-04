<div align="center"> 
    
![ICR SCARS](screenshots/scars.png)

# Bitch-X Terminal Chat

</div>


---

## Features

- Terminal-based anonymous chat
- Multi-client support (50+ users)
- No message logging or storage
- Real-time message broadcasting
- Pink/White hacker-style interface
- Session data cleared on exit
- Pure Python (no dependencies)

---

## Quick Start

### Installation

**Windows:**
```cmd
mkdir bitchx-chat
cd bitchx-chat
mkdir handlers utils ui
type nul > handlers\__init__.py
type nul > utils\__init__.py
type nul > ui\__init__.py
```

**Linux/Mac:**
```bash
mkdir -p bitchx-chat/{handlers,utils,ui}
cd bitchx-chat
touch handlers/__init__.py utils/__init__.py ui/__init__.py
```

Copy all Python files to their respective directories.

### Usage

**Start Server:**
```bash
python server.py
```

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
4. Share the ngrok URL with friends

---

## Troubleshooting

**"Address already in use"**
- Change port in `config.py`
- Or kill the process using that port

**"Connection refused"**
- Check server is running
- Verify IP address and port
- Check firewall settings

**"No module named 'handlers'"**
- Create `__init__.py` files in all directories

**Colors not showing (Windows)**
- Use Windows Terminal
- Or install: `pip install colorama`

---

## Project Structure

```
bitchx-chat/
├── server.py
├── client.py
├── config.py
├── handlers/
│   ├── __init__.py
│   ├── client_handler.py
│   ├── message_handler.py
│   └── receive_handler.py
├── utils/
│   ├── __init__.py
│   └── colors.py
└── ui/
    ├── __init__.py
    ├── banner.py
    └── input_handler.py
```

---

## Requirements

- Python 3.6+
- No external dependencies (standard library only)

---

## Security Notes

- Messages are not encrypted
- No user authentication
- No message persistence
- Use VPN or ngrok for internet connections
- Not recommended for sensitive information

---

## License

Free to use and modify.

---

**Stay Anonymous. Stay Connected.**
