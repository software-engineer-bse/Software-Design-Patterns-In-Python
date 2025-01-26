class Shop:
    def __init__(self):
        self._observers = []
        self._if_shop_open = True

    def add_observer(self, observer):
        self._observers.append(observer)

    def set_if_shop_open(self, if_shop_open):
        self._if_shop_open = if_shop_open
        self.notify_observers()

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._if_shop_open)


class Observer:
    def update(self, if_shop_open):
        pass

class Phone_Screen(Observer):
    def update(self, if_shop_open):
        if if_shop_open:
            print("Shop is open.")
        else:
            print("Shop is not open")

shop = Shop()
phone_screen = Phone_Screen()
shop.add_observer(phone_screen)
shop.set_if_shop_open(True)
shop.set_if_shop_open(False)