"""
Python Webserver
 - 11/19/2018
 - Austin Rovge

This is a simple web server written in python.
"""

import socket
from os.path import isfile, join
from os import stat


def main():
    """
    The main method is called first and starts the server on port 8080.
    """

    start_http_server(8080)


def start_http_server(port):
    """
    This method setups the http server.
    :param port: the port to start the server on
    """

    # create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind to the local address on the specified port
    listen_addr = '', port
    server_socket.bind(listen_addr)

    # listen for an 10 requests. refuse any after that
    server_socket.listen(10)

    while True:
        conn, addr = server_socket.accept()
        handle_request(conn)


def handle_request(server_socket):
    request_line, request_headers = read_http_request(server_socket)
    http_request, resource, protocol_version = request_line

    if http_request == 'GET':
        handle_get_request(server_socket, request_line)
    else:
        print(f'{http_request} requests are not supported')


def read_http_request(server_socket):
    """
    This method reads in the entire HTTP request.
    :param server_socket: the socket to read bytes from
    :return: a tuple of the request line (as a tuple of HTTP request, resource, and protocol version)
             and the request headers, in ASCII
    """

    # all HTTP requests ends with a \r\n\r\n (CR LF CR LF)
    http_request = b''
    while b'\r\n\r\n' not in http_request:
        http_request += next_byte(server_socket)

    request_line, request_headers = http_request.decode('ASCII').split('\r\n', 1)

    # tuple of HTTP request, resource, and protocol version
    request_line = request_line.split(' ', 3)

    return request_line, request_headers


def handle_get_request(server_socket, request_line):
    """
    This method handles all HTTP GET requests.
    :param server_socket: the server socket to receive data from
    :param request_line: the HTTP request line as a tuple (containing HTTP request, resource, and protocol version)
    """

    http_request, resource, protocol_version = request_line

    if resource == '/':
        resource = 'index.html'
    else:
        resource = resource[1:]

    file = join('resources', resource)

    file_size = get_file_size(file)
    http_response = get_status_line(file_size)

    http_response += b'Content-length: ' + file_size + b'\r\n'
    http_response += b'\r\n'
    server_socket.sendall(http_response)


def get_status_line(file_size):
    """
    This method returns the status line for the HTTP response based on the file size.
    :param file_size: the size of the requested file
    :return: the status line as a bytes object
    """

    status_line = b'HTTP/1.1 '

    if file_size != b'0':
        status_line += b' 200 OK\r\n'
    else:
        status_line += b' 404 Not Found\r\n'

    return status_line


def get_file_size(resource):
    """
    This method gets the size of the resource.
    :param resource: resource to get size from
    :return: the file size as an integer
    """

    file_size = b'0'
    if isfile(resource):
        file_size = stat(resource).st_size.encode('ASCII')
    return file_size


def next_byte(server_socket):
    """
    This method reads in one byte.
    :param server_socket: the socket to read one byte from
    :return: a byte object of the single byte read in
    """

    return server_socket.recv(1)


if __name__ == '__main__':
    main()
