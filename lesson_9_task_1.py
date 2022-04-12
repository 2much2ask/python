import time


class TrafficLight:

    def running(self):
        _color_times = {'red': 3,
                        'yellow': 2,
                        'green': 1
                        }

        for key, value in _color_times.items():
            print(f'now the light is {key}, please wait {value} seconds')
            time.sleep(value)


a = TrafficLight()
TrafficLight.running(a)
