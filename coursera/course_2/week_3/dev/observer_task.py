from abc import ABC, abstractmethod


class Engine:
    pass


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, achievement):
        for subscriber in self.__subscribers:
            subscriber.update(achievement)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, achievement):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, achievement):
        self.achievements.add(achievement["title"])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = list()

    def update(self, achievement):
        if achievement not in self.achievements:
            self.achievements.append(achievement)


if __name__ == "__main__":
    short_notification_printer = ShortNotificationPrinter()
    full_notification_printer = FullNotificationPrinter()

    engine = ObservableEngine()
    engine.subscribe(short_notification_printer)
    engine.subscribe(full_notification_printer)

    achievement1= {"title": "FirstLevel", "text": "You reached 1 level"}
    achievement2= {"title": "ZombiesKiller", "text": "You killed 20 zombies"}
    engine.notify(achievement1)
    engine.notify(achievement2)
    engine.notify(achievement2)
    engine.notify(achievement1)

    print("short_notification_printer: ", short_notification_printer.achievements)
    print("full_notification_printer: ", *full_notification_printer.achievements, sep='\n')