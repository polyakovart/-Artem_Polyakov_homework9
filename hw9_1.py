import time


class TrafficLight:
    __color = ('red', 'yellow', 'green')
    def running(self):
        time_red = 4
        time_yellow = 2
        time_green = 3
        print(f'{TrafficLight.__color[0]} {time_red} сек')
        time.sleep(time_red)
        print(f'{TrafficLight.__color[1]} {time_yellow} сек')
        time.sleep(time_yellow)
        print(f'{TrafficLight.__color[2]} {time_green} сек')
        time.sleep(time_green) 


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()