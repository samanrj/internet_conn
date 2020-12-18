import pytest
import socket

# @pytest.mark.enable_socket
# def test_explicitly_enable_socket_with_mark():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         assert s.connect(('1.1.1.1', 80))

def inc(x):
    return x + 1
def test_answer():
    assert inc(3) == 4
