# -*- coding:utf-8 -*-
# Author:DaoYang
import websocket
import threading

try:
    import thread
except ImportError:
    import _thread as thread
import time, json


class NetWork(threading.Thread):
    def __init__(self, url_host, room):
        threading.Thread.__init__(self)
        self.url = url_host + "/ws/colorfight/" + room
        self.ws = None
        self.room = room
        self.res = {}

    def run(self):
        print("Network " + self.room + " started!")
        self.ws = websocket.WebSocketApp(self.url, on_message=self.on_message, on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.run_forever()

    def connect(self):
        self.start()
        time.sleep(0.5)

    def on_message(self, message):
        data = json.loads(message)['message']
        self.res = data['content']
        print('Receive: ', data['response_type'])

    def on_error(self, error):
        print('Error', error)

    def on_close(self, ):
        print("### closed ###")

    def on_open(self, ):
        print("### open ###")

    def send(self, dict, delay=0.1):
        self.ws.send(json.dumps({'message': dict}))
        time.sleep(delay)

    def disconnect(self):
        self.ws.close()


if __name__ == "__main__":
    # websocket.enableTrace(True)
    nw = NetWork('game_channel')
    nw.connect()
    nw.send({'message': {'action': 'register', 'username': '2', 'password': 456}})
    nw.send({'message': {'action': 'register', 'username': '2', 'password': 467}})
    print(nw.res)
    nw.disconnect()
