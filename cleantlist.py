#/usr/bin/env python3
# This is horrible but it works
# ProxyBrokerParse
# Written by Leonidus
# Usage: python3 cleanlist.py outfile.txt
import sys
prox_list = sys.argv[1]
f = open(prox_list, "r")
proxies = f.readlines()

for proxy in proxies:
    x_proxy = proxy.split(" ")[5]
    new_proxy = x_proxy.replace(">", "")
    new_list = open("new_list.txt", "a")
    new_list.write(new_proxy)
    new_list.close()
