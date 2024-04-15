import logging
from io import BytesIO

import qrcode
from django.core.files.base import ContentFile
from qrcode.image.svg import SvgPathFillImage
from qrcode.main import QRCode

logger = logging.getLogger()


def make_qr_code(data: str, box_size: int = 10, border: int = 1) -> SvgPathFillImage:
    """
    Generate a QR code, does not save the image.

    Args:
        data (str): The data to be encoded in the QR code.
        box_size (int, optional): The size of each box in the QR code grid.
                                  Defaults to 10.
        border (int, optional): The thickness of the border. Defaults to 1.

    Returns:
        SvgPathFillImage: The generated QR code as an SVG image.
    """
    qr = QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
        image_factory=SvgPathFillImage,
    )
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")


def _in_memory_qr(data: str) -> BytesIO:
    """
    Save file to in-memory bytes buffer, not to disk and return the buffer.

    Args:
        data (str): The data to be encoded in the QR code.

    Returns:
        BytesIO: The in-memory bytes buffer containing the QR code.
    """
    img = make_qr_code(data)
    bytes_io = BytesIO()
    img.save(bytes_io)
    return bytes_io


def make_qr_content_file(data: str, filename: str) -> ContentFile:
    """
    Return content file for use in Django.

    Args:
        data (str): The data to be encoded in the QR code.
        filename (str): The name of the file.

    Returns:
        ContentFile: The content file containing the QR code.
    """
    bytes_io = _in_memory_qr(data)
    return ContentFile(bytes_io.getvalue(), name=f"{filename}")
