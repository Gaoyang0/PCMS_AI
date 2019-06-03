# -*- coding:utf-8 -*-
# Author:DaoYang

from core.colorfight import ColorFight
import time, random
from core.position import Position

url_host = 'ws://127.0.0.1:8000'
user_name = 'Example03'
game_id = '44426'

if __name__ == '__main__':
    game = ColorFight(url_host, game_id, user_name)
    game.connect()
    if game.register():
        while True:
            game.update_info()
            print('--------------------------------------------------', game.me.state)
            if game.me.state == 'free':
                cmd_list = []
                cell_list = []
                # 建base
                if game.me.gold > 80 and game.me.base_source <= 2:
                    for cell in game.me.cells.values():
                        cell_list.append(cell.position)
                    p = random.choice(cell_list)
                    cmd_list.append(game.build(Position(p.x, p.y)))
                # 进攻
                else:
                    for cell in game.me.cells.values():
                        for pos in cell.position.get_surrounding_cardinals():
                            if str(game.map[pos.y][pos.x]['owner']) != str(game.me.uid):
                                cell_list.append(pos)
                    p = random.choice(cell_list)
                    if game.me.gold > 5:
                        cost = 5
                    else:
                        cost = 0
                    cmd_list.append(game.attack(Position(p.x, p.y), cost))
                game.send_cmd(cmd_list)
                print('attack: ', p.x, p.y)
                game.me.state = 'CD'
                print('-------------------------------------------------------')
