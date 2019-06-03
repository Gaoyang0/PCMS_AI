# -*- coding:utf-8 -*-
# Author:DaoYang


from flask import Flask, request, Response
import json
from snake_ai import snakeAI, sankeAI_astar

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'snake AI 已开启!'


# 延时检测
@app.route('/test_delayed/')
def test_delayed():
    return Response(json.dumps({'status': 'OK'}), mimetype='application/json')


@app.route('/snake-ai/', methods=['POST'])
def snake_ai():
    data = request.json
    if data['type'] and data['type'] == 'ai_decision':
        # 地图长宽
        width = data['message']['map_size']['width']
        height = data['message']['map_size']['height']
        # 食物
        food = data['message']['food']
        # 蛇身
        snake = data['message']['body']
        # 当前方向
        current_direction = data['message']['direction']
        # print(type(int(current_direction)))


        # 更优算法
        # 创建sankeAI类
        snake_ai = snakeAI.SnakeDecision(width, height)
        # 重置地图信息
        # food = {'left': 1, 'top': 1}
        # snake = [{'left': 3, 'top': 0}, {'left': 2, 'top': 0}]
        snake_ai.set_map(food, snake, current_direction)
        # 获取决策结果
        direction = snake_ai.get_one_step()

        '''

        # Astar算法
        # 创建sankeAI类
        snake_Astar = sankeAI_astar.SnakeDecision(width, height)
        # 重置地图信息
        # food = {'left': 1, 'top': 1}
        # snake = [{'left': 3, 'top': 0}, {'left': 2, 'top': 0}]
        snake_Astar.set_map(food, snake, current_direction)
        # 获取决策结果
        direction = snake_Astar.get_one_step()
'''

        # 返回决策结果
        rt = {
            'type': 'ai_control',
            'message': {
                'direction': direction,
            },
        }
        return Response(json.dumps(rt), mimetype='application/json')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
