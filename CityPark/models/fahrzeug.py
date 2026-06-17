from abc import ABC, abstractmethod


class Fahrzeug(ABC):

    def __init__(self, kennzeichen):
        self.__kennzeichen = kennzeichen


    def get_kennzeichen(self):
        return self.__kennzeichen


    @abstractmethod
    def get_faktor(self):
        pass


    @abstractmethod
    def get_typ(self):
        pass