"""
You can auto-discover and run all tests with this command:

    py.test

Documentation: https://docs.pytest.org/en/latest/
"""

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4


# def test_telnet_is_null_when_host_unreachable(self):
#     hostname = 'unreachable'
#
#     response = network_utils.telnet(hostname)
#
#     self.assertDictEqual(response, {'unreachable': None})
#
# def test_telnet_give_time_when_reachable(self):
#     hostname = '127.0.0.1'
#
#     response = network_utils.telnet(hostname, port=22)
#
#     self.assertGreater(response[hostname], 0)


# def test_capital_case():
#     assert capital_case('semaphore') == 'Semaphore'
#
# def test_raises_exception_on_non_string_arguments():
#     with pytest.raises(TypeError):
#         capital_case(9)

# import mock
# import socket
#
# class testSample(object):
#
#     def __init__(self):
#         self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.tcp_socket.connect('0.0.0.0', '6767')
#
# with mock.patch('socket.socket'):
#     c = testSample()
#     c.tcp_socket.connect.assert_called_with('0.0.0.0', '6767')
