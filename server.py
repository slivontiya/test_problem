import socket
import os
import zipfile
from datetime import datetime, timedelta


def my_time():
    then = datetime.now() - timedelta(days=90)
    year, month, day = then.year, then.month, then.day
    return [year, month, day]


def old_file():
    directory = '/storage'
    root, dirs, files = os.walk(directory)
    for i in dirs:
        if int(i) < my_time()[0]:
            send_file(i)
        else:
            directory = '/storage/' + i
            root, dirs, files = os.walk(directory)
            for j in dirs:
                if int(j) < my_time()[1]:
                    send_file(j)
                else:
                    directory = '/storage/' + i + '/' + j
                    root, dirs, files = os.walk(directory)
                    for k in dirs:
                        if int(k) < my_time()[2]:
                            send_file(k)


def archiving(filename):
    my_directory = filename
    arch = zipfile.ZipFile('zip_file.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(my_directory):
        for tarfile in files:
            if tarfile != '':
                arch.write(root + '\\' + tarfile)
    arch.close()
    return 'zip_file.zip'


def send_file(filename):
    zip_file = archiving(filename)
    s = socket.socket()
    host = socket.gethostname()
    port = 8080
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    print(addr, 'has connected to the network')
    file = open(zip_file, 'rb')
    filedata = file.read(1024)
    conn.send(filedata)
    print('file has been sent successfully')


if __name__ == "__main__":
    old_file()
