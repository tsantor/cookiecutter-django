import socket


def get_container_ip():
    """Get the container's IP address"""
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except Exception:  # noqa: BLE001
        return "localhost"
