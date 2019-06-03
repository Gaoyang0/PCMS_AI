# -*- coding:utf-8 -*-
# Author:DaoYang


class MapCell:
    def __init__(self, position):
        self.position = position

        #  0: 无人占 其他: 为用户id
        self.owner = 0
        self.occupy_time = 0
        self.is_taking = False
        self.attacker = 0
        # 进攻的时间
        self.attack_time = 0
        self.attack_type = ""
        # 进攻结束时间
        self.finish_time = 0
        self.last_update_time = 0
        # land gold
        self.cell_type = "land"
        # empty occupied fighting building base
        self.build_state = "empty"
        # build base 是否结束
        self.build_finish = True
        # 建筑base开始时间
        self.build_time = 0

    def update(self, dict):
        self.position.x = dict['position']['x']
        self.position.y = dict['position']['y']
        self.owner = dict['owner']
        self.occupy_time = dict['occupy_time']
        self.is_taking = dict['is_taking']
        self.attacker = dict['attacker']
        self.attack_time = dict['attack_time']
        self.attack_type = dict['attack_type']
        self.finish_time = dict['finish_time']
        self.last_update_time = dict['last_update_time']
        self.cell_type = dict['cell_type']
        self.build_state = dict['build_state']
        self.build_finish = dict['build_finish']
        self.build_time = dict['build_time']

    def info(self):
        return {
            "position": self.position.info(),
            "owner": self.owner,
            "occupy_time": self.occupy_time,
            "is_taking": self.is_taking,
            "attacker": self.attacker,
            "attack_time": self.attack_time,
            "attack_type": self.attack_type,
            'finish_time': self.finish_time,
            'last_update_time': self.last_update_time,
            "cell_type": self.cell_type,
            "build_state": self.build_state,
            'build_finish': self.build_finish,
            'build_time': self.build_time,
        }



