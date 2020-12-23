import csv
import os
import time
from selenium import webdriver
import random
import subprocess
import shlex
import signal


def read_file():
    web_sites = list()
    with open('filtered_list') as sites_url:
        for line in sites_url:
            web_sites.append(line)
    return web_sites

def open_site(url):
    dr = webdriver.Chrome()
    dr.get(url)
    dr.close()


try:
    web_sites = read_file()
    site_index = 0
    total_sites = 478
    loop = 0
    while site_index<total_sites:
        #start the flow
        print("start loop: " + str(loop))
        time.sleep(25)
        cmd = shlex.split('sudo openvpn --config /home/irondev25/id25.ovpn')
        #start the vpn service
        vpn_service = subprocess.Popen(cmd)
        #let it initialize
        time.sleep(5)

        #take 4 websites from the list
        for i in range(4):
            if site_index >= total_sites: 
                break
            site = web_sites[site_index]
            site_index += 1
            if(site == ""):
                break
            try:
                open_site(site)
            except Exception as e:
                print(e)
        #sanity wait
        time.sleep(5)
        #kill the vpn service
        os.system('sudo killall -SIGINT openvpn')
        print("end loop: " + str(loop))
        loop += 1
        time.sleep(265)
        #stop the flow
except Exception as e:
    print(e)

        
