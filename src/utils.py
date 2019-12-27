import socket, logging


def check_internet_connection(host="8.8.8.8", port=53, timeout=1):
    """
    Checks whether the device is connected to the Internet by creating a socket
    connection with a host IP address. By default it makes a connection with
    Google's Public DNS Server on port 53.
    Source: https://stackoverflow.com/a/33117579

    Parameters:
    -----------
    host (str): host IP address, default="8.8.8.8"
    port (int): port number, default=53
    timeout(float, optional) = timeout in seconds, default=1

    Returns:
    --------
    boolean

    """
    logging.debug("Checking internet connection")
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as err:
        print(err)

    return False
