# -*- coding:utf-8 -*-
# Author:DaoYang

from snake_ai.astar import Array2D, Point, AStar


class SnakeDecision(object):
    def __init__(self, width, height):
        self.HEIGHT = height
        self.WIDTH = width
        self.food = {}
        self.snake = []
        self.current_direction = 0

    def set_map(self, new_food, new_snake, current_direction):
        self.food = new_food
        self.snake = new_snake
        self.current_direction = current_direction

    def get_one_step(self, ):
        '''
        上 38
        下 40
        左 37
        右 39
        '''
        # 创建一个10*10的地图
        map2d = Array2D(self.HEIGHT, self.WIDTH)
        # 设置障碍
        for i in range(1, len(self.snake)):
            map2d[self.snake[i]['left']][self.snake[i]['top']] = 1

        # 显示地图当前样子
        # map2d.showArray2D()
        # 创建AStar对象,并设置起点为蛇头,终点为食物
        aStar = AStar(map2d, Point(self.snake[0]['left'], self.snake[0]['top']),
                      Point(self.food['left'], self.food['top']))
        # 开始寻路
        pathList = aStar.start()
        '''
        # 遍历路径点,在map2d上以'-'显示
        if pathList:
            for point in pathList:
                map2d[point.x][point.y] = '-'
                # print(point)
            print("----------------------")
            # 再次显示地图
            map2d.showArray2D()
        '''
        # 当无路径时不改变方向
        if pathList:
            # print(aStar.startPoint)
            # print(pathList[0])
            if aStar.startPoint.x == pathList[0].x and aStar.startPoint.y < pathList[0].y:
                return 40
            if aStar.startPoint.x == pathList[0].x and aStar.startPoint.y > pathList[0].y:
                return 38
            if aStar.startPoint.y == pathList[0].y and aStar.startPoint.x < pathList[0].x:
                return 39
            if aStar.startPoint.y == pathList[0].y and aStar.startPoint.x > pathList[0].x:
                return 37
        else:
            return self.current_direction



s = SnakeDecision(10, 10)
s.set_map({'left': 3, 'top': 3}, [{'left': 2, 'top': 0}, {'left': 3, 'top': 0}, {'left': 4, 'top': 0}], 38)
print(s.get_one_step())

