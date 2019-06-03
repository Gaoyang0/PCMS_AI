# -*- coding:utf-8 -*-
# Author:DaoYang

from .constants import INITIAL_GOLD
from .map_cell import MapCell
from .position import Position


class User:
    def __init__(self, uid, username, ):
        self.uid = uid
        self.username = username
        self.gold = INITIAL_GOLD
        self.gold_source = 0
        self.base_source = 0
        self.state = "dead"
        self.cells = {}
        self.score = 0

    def load_info(self, user_info):
        self.gold = user_info['gold']
        self.gold_source = user_info['gold_source']
        self.state = user_info['state']
        self.score = user_info['score']
        self.base_source = user_info['base_source']

        # 更新cells
        c = {}
        for key in user_info['cells'].keys():
            if key in self.cells:
                self.cells[key].update(user_info['cells'][key])
                c[key] = self.cells[key]
            else:
                pos = Position(user_info['cells'][key]['position']['x'], user_info['cells'][key]['position']['y'])
                cell = MapCell(pos)
                cell.update(user_info['cells'][key])
                c[pos.__str__()] = cell
        self.cells = c

    def info(self):
        return {
            "uid": self.uid,
            "username": self.username,
            "gold": self.gold,
            "state": self.state,
            "gold_source": self.gold_source,
            "cells": {cell.position.__str__(): cell.info() for cell in self.cells.values()},
            "score": self.score,
            "base_source": self.base_source,
        }
