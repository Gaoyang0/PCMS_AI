# -*- coding:utf-8 -*-
# Author:DaoYang

import time
import queue

from .user import User
from .position import Position
from .network import NetWork
import json


class ColorFight:
    def __init__(self, url_host, game_id, user_name):
        self.game_id = game_id
        self.url_host = url_host

        self.game_state = ''
        self.width = 0
        self.height = 0
        self.current_time = 0

        self.uid = 0
        self.user_name = user_name

        self.me = None

        self.error = {}

        self.map = []
        self.nw_info = None
        self.nw_action = None

    def connect(self, ):
        self.nw_info = NetWork(self.url_host, 'game_channel/' + self.game_id + '/' + self.user_name + '/')
        self.nw_action = NetWork(self.url_host, 'action_channel/' + self.game_id + '/' + self.user_name + '/')
        self.nw_info.connect()
        self.nw_action.connect()

    def load_info(self, info):
        if info['state'] == 'success':
            self.game_state = info['game']['game_state']
            self.width = info['game']['width']
            self.height = info['game']['height']
            self.current_time = info['game']['time']

            self.me.load_info(info['user'])
            self.map = info['map']

    def update_info(self):
        msg = {'action': 'get_info', 'content': {'game_id': self.game_id, 'uid': self.uid}}
        try:
            self.nw_info.send(msg, 0.4)
            self.load_info(self.nw_info.res)
            return True
        except:
            return False

    def register(self, ):
        msg = {'action': 'register', 'content': {'user_name': self.user_name, 'game_id': self.game_id, }}
        try:
            self.nw_action.send(msg)
            self.uid = self.nw_action.res['uid']
            self.me = User(self.uid, self.user_name)
            return True
        except:
            return False

    def attack(self, position, cost):
        return {'action': 'attack', 'content': {'uid': self.uid, 'game_id': self.game_id, 'x': position.x, 'y': position.y, 'cost': cost, }}

    def build(self, position):
        return {'action': 'build', 'content': {'uid': self.uid, 'game_id': self.game_id, 'x': position.x, 'y': position.y, }}

    def send_cmd(self, cmd_list):
        for cmd in cmd_list:
            try:
                self.nw_action.send(cmd)
                print(self.nw_action.res)
            except:
                print('cmd: ', cmd, 'except!')

