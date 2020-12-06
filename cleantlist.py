#/usr/bin/env python3
# This is horrible but it works
# ProxyBrokerParse
# Written by Leonidus
# Usage: python3 cleanlist.py outfile.txt
# this is meant for http proxy list ive yet to implement socks5 and https
import sys
prox_list = sys.argv[1]
f = open(prox_list, "r")
proxies = f.readlines()

for proxy in proxies:
    x_proxy = proxy.split(" ")[5] # change this to sort different outputs
    new_proxy = x_proxy.replace(">", "")
    new_list = open("new_list.txt", "a")
    new_list.write(new_proxy)
    new_list.close()
