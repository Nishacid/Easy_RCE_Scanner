#!/usr/bin/python3
# -*- Coding : utf-8 -*-
# Python Version    : 3.X
# Author            : Nishacid

import socket
import argparse
import yaml
import sys
import time

if __name__ == "__main__":
    
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", dest="ip", help="Targeted IP", required=True)
    args = parser.parse_args()
    
    # Time format
    def time_format(delta_t, units = ["hours","minutes","seconds","miliseconds"]):
        out = ""
        if delta_t // 3600 != 0: # hours
            out = out + str(int(delta_t // 3600)) + " " + units[0]
            delta_t = delta_t % 3600
        if delta_t // 60 != 0: # minutes
            out = out + " " +  str(int(delta_t // 60)) + " " + units[1]
            delta_t = delta_t % 60
        if int(delta_t) != 0: # seconds
            out = out + " " + str(int(delta_t)) + " " + units[2]
            delta_t = delta_t - int(delta_t)
        if delta_t // 0.001 != 0: # miliseconds
            out = out + " " + str(int(delta_t//0.001)) + " " + units[3]
        if len(out) == 0:
            out = "0 "+units[3]
        out = out + "."
        if out.startswith(" "):
            out = out[1:]
        return out
    
    def port_scan(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((IP, port))
            if result == 0:
                print(f"[+] Port {port} open on {IP}")
                print(f"[*] More information about the exploit for {data[number]['name']}")
                print(f"[*] {data[number]['description']}")
                sock.close()
        except socket.error:
            print("Couldn't connect to server")
            sys.exit()
        except socket.gaierror:
            print("Hostname could not be resolved")
            sys.exit()

    # Open Yaml File
    with open("ports.yml", "r") as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as err:
            print(err)
            sys.exit()
    # Infos
    IP = args.ip 
    time_start = time.time()
    
    number = 1
    for value in data.items():
        ports = data[number]["ports"]
        if type(ports) == list:
            for port in ports:
                port_scan(port)
        else:
            port_scan(ports)    
        number += 1
        
    print("Scanning completed in : " + time_format(time.time() - time_start))