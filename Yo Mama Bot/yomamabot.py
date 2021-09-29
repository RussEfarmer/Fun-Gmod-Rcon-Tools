import time
from rcon import Client
import random

#Sends a single command
def sendcommand(command):
    #Change this to what you put in your startup options
    port = 27015
    password = "change this"
    with Client("127.0.0.1", port, passwd=password) as client:
        response = client.run(command)
        print(response)

#Runs the clock with a cool graphic
def rcontimer(t, command):
    while t: 
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        if not t:
            sendcommand(command)

#Automatic yo mama jokes
def yo_mama(file):
    fh = open(file, "r")
    lines = 0
    jokes = []
    for i in fh.readlines():
        lines += 1
        jokes.append(i)
    return jokes[random.randint(1, lines)]

#To call specific peoples mama fat
def whos_mama(who, file):
    joke_split = yo_mama(file).split(" ")
    joke_split[0] = who
    return " ".join(joke_split)

while True:
    #Top function does specific persons mama, bottom is normal yo mama
    #rcontimer(100, "say " + whos_mama("dong\'s", "mama.txt"))
    rcontimer(120, "say " + yo_mama("mama.txt"))