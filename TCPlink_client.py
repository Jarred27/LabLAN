import socket
import os

TCP_IP = '118.138.64.240'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = b'Hello, World!'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print('sending message')
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)


def list_text_files():
    """

    :return: a list of txt files in the current directory path
    """
    list_of_textfiles = []
    for file in os.listdir("/mydir"):
        if file.endswith(".txt"):
            list_of_textfiles.append(os.path.join("/mydir", file))
    return list_of_textfiles


def send_file(file_to_be_sent):
    for line in file_to_be_sent:



"""
text file operations:
    read txt file from local storage, send chunks over TCP
    verify a file has completely sent or not
        sendfile("filename") returns 0 for success, 1 for failure


Visa operations
    resource management
        list resources
        check devices available
        WhoAmI function
    sending commands
        read
        write
        query
        exception handling
    keep TCP connection alive
        make connection request
        send ping requests at intervals
                
"""
