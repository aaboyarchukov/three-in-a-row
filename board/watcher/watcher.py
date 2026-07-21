from abc import ABC, abstractmethod
from subscriber import Subscriber

class Watcher(ABC):
    
    @abstractmethod
    def notify(self): ...
    
    @abstractmethod
    def subscribe(): ...
    
    @abstractmethod
    def unsubscribe(): ...


class BoardWatcher(Watcher):
    notifiers : list[Subscriber]

    def notify(self):
        pass

    