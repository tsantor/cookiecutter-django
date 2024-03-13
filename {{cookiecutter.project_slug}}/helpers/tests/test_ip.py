from helpers.ip import IPStackAPI
from helpers.ip import get_ip_info
from helpers.ip import is_private_ip
from django.conf import settings

def test_get_ip_info_ipstack():
    if hasattr(settings, "IPSTACK_API_KEY"):
        ip_info = get_ip_info("131.148.1.222", IPStackAPI())
        assert ip_info != {}
    pass

def test_is_private_ip():
    # private ipv4
    assert is_private_ip("192.168.0.1") is True
    assert is_private_ip("10.0.0.1") is True
    assert is_private_ip("172.16.0.1") is True
    assert is_private_ip("127.0.0.1") is True

    # public ipv4
    assert is_private_ip("8.8.8.8") is False
    # assert is_private_ip("2001:db8::") is False
    # assert is_private_ip("fd00::") is True
    # assert is_private_ip("invalid") is False
