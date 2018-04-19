# -*- coding:utf-8 -*-

from slackbot.bot import listen_to
import datetime

@listen_to('何時')
def saytime(message):
    d = datetime.datetime.now()
    message.send(str(d.strftime("%Y年%m月%d日%H時%M分")) +'やで')

@listen_to('素敵やん')
def reaction(message):
    message.react('shallow_pan_of_food')


import urllib.request
import json
import random

@listen_to('アニメ')
def anime(message):
    d = datetime.datetime.today()
    url = 'http://api.moemoe.tokyo/anime/v1/master/'

    winter = [1,2,3]
    spring = [4,5,6]
    summer = [7,8,9]
    autumn = [10,11,12]

    if int(d.month) in winter:
        month = '/1'
    elif int(d.month) in spring:
        month = '/2'
    elif int(d.month) in summer:
        month = '/3'
    else :
        month = '/4'


    url += str(d.year) + month
    print(url)
    response = urllib.request.urlopen(url)
    content = json.loads(response.read().decode('utf-8'))

    rnd = random.randint(0, len(content)-1)
    message.send(content[rnd]['title'] + ':tv:' + 'がおもろいで！知らんけど！' + content[rnd]['public_url'])
