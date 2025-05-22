import base64
import logging
from io import BytesIO

import qrcode

logger = logging.getLogger(__name__)


def make_qr_code(data, box_size=10, border=0):
    """Generate a QR code, does not save the image."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")


def make_in_memory_qr(data):
    """Save file to in-memory bytes buffer, not to disk and return the buffer."""
    img = make_qr_code(data)
    bytes_io = BytesIO()
    img.save(bytes_io, format="PNG")
    return bytes_io


def make_qr_code_b64(data):
    """Return a Base64 encoded QR code for use in HTML. NOTE: Base64 encoded
    images are NOT well supported in email clients."""
    bytes_io = make_in_memory_qr(data)
    img_str = base64.b64encode(bytes_io.getvalue()).decode()
    return f"data:image/png;base64, {img_str}"
