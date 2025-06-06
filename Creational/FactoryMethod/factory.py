# Creational/FactoryMethod/factory.py
from abc import ABC, abstractmethod

# "Interfaz" del Producto: define la estructura que deben seguir los productos
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# Productos Concretos: implementaciones reales de la interfaz
class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f'Enviando por Email: "{message}"')

class SmsNotifier(Notifier):
    def send(self, message: str):
        print(f'Enviando por SMS: "{message}"')

class PushNotifier(Notifier):
    def send(self):
        print(f'Enviando por Push: ')

# La Fábrica: su trabajo es crear los objetos correctos
class NotificationFactory:
    @staticmethod
    def create_notifier(channel: str) -> Notifier:
        if channel == "EMAIL":
            return EmailNotifier()
        elif channel == "SMS":
            return SmsNotifier()
        elif channel == "PUSH":
            return PushNotifier()
        raise ValueError(f"Canal desconocido: {channel}")