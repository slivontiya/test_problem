import socket


def run():
    s = socket.socket()
    host = socket.gethostname()
    port = 8080
    s.connect((host, port))
    print('connected')
    file_data = s.recv(1024)
    filename = 'zip_file.zip'
    file = open(filename, 'wb')
    file.write(file_data)
    file.close()
    print('finished')
