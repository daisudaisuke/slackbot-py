# -*- coding:utf-8 -*-

from slackbot.bot import respond_to

@respond_to('もうかりまっか')
def hello(message):
    message.reply('ぼちぼちでんな')
