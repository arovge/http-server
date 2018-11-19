"""
Python Webserver
 - 11/19/2018
 - Austin Rovge

This is a simple web server written in python.
"""

import socket


def main():
    """
    The main method is called first and starts the server on port 8080.
    """

    start_http_server(8080)


def start_http_server(port):
    """
    This method setups the http server
    :param port: the port to start the server on
    """

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    listen_addr = '', port
    server_socket.bind(listen_addr)
    server_socket.listen()

    while True:
        conn, addr = server_socket.accept()
        print(conn)


if __name__ == '__main__':
    main()
