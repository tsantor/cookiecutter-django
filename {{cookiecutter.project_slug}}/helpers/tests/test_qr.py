from django.core.files.base import ContentFile

from helpers.qr import _in_memory_qr
from helpers.qr import make_qr_code
from helpers.qr import make_qr_content_file


def test_make_qr_code():
    data = "Test QR Code"
    qr_image = make_qr_code(data)

    assert qr_image is not None


def test_in_memory_qr():
    data = "Test QR Code"
    bytes_io = _in_memory_qr(data)

    assert bytes_io.getvalue() != b""


def test_make_qr_content_file():
    data = "Test QR Code"
    filename = "test_qr.png"
    content_file = make_qr_content_file(data, filename)

    assert isinstance(content_file, ContentFile)
    assert content_file.name == filename
    assert content_file.read() != b""
