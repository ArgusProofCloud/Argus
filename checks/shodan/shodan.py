#!/usr/bin/python3
from urllib import response
import requests
import socket
import sys
key="4VdRQ9pNJvTsJNw4dF2VMQz3VczqbV0a"

def main(domain:str):
    try:
        host_name = domain
        host_ip = socket.gethostbyname(host_name)
        #print("Hostname : ",host_name)
        #print("IP : ",host_ip)
        response = requests.get("https://api.shodan.io/shodan/host/"+host_ip+"?key="+key)
        print(response.json())
    except:
        print("Unable to resolve Hostname to IP")



if __name__ == "__main__":
  main(sys.argv[1])