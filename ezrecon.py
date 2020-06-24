import requests
import re
from urllib.parse import urlparse
from fake_useragent import UserAgent
import socket
import socks
from bs4 import BeautifulSoup as bs4
import hashlib
import os
from urllib.parse import urlparse,urljoin


os.system("clear")
os.system("figlet E2-ReC0N")

url = input("[+]Enter The URL: ")
host = urlparse(url).netloc
ip = socket.gethostbyname(host)

print(f"[*]target IP_addr: {ip}")



def anonymous():

    socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5,'127.0.0.1',9050)
    socket.socket = socks.socksocket

    contest = requests.get("http://checkip.dyndns.com/")
    
    regexip = re.search(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}",contest.text)
    rege = regexip.group()
    #print(rege)
    print("[+]IP_addr is Changed...")
    print(hashlib.md5(rege.encode()).hexdigest()) 
    print("[+]Init Connected Tor")


def mrrobot(url):
    robo = "robots.txt"
    req = requests.get(url+robo)
    if str(req) == '<Response [200]>':
        print("[*]robots.txt is available")
        print(req.text)

        print("-"*60)
    else:
        print("[*]robots.txt is not found")


def request(url):
    
    ua = UserAgent()
    headers = {"User-Agent":ua.random}
    res = requests.get(url,headers = headers)
    soup = bs4(res.text,'lxml')
    print(f"[+]Title: {soup.title.text}")
    array = []
    fixarray = []
    trash = []
    print("[+]Founded:")
    for link in soup.find_all('a'):
        array.append(link.get('href'))
        
        for a in range(0, len(array)):
            regex = re.match(r"^ht.+",str(array[a]))
            if regex == None:
                fixarray.append(urljoin(url,array[a]))

            else:
                fixarray.append(array[a])
     
    setarray = set(fixarray)
    setarray = list(setarray)

    for arr in range(0, len(setarray)):
        if urlparse(setarray[arr]).netloc == urlparse(url).netloc: 
            print(setarray[arr])
    print("[+]Duplicated URL:",len(array)-len(setarray))
    print("[+]Auto Removed.")

mrrobot(url)
anonymous()
request(url)



