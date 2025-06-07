# Creational/FactoryMethod/main.py
from .factory import NotificationFactory

def test_factory_method():
    print("--- Prueba del Patrón Factory Method ---")
    try:
        # El cliente pide los objetos a la fábrica sin saber cómo se crean
        email_notifier = NotificationFactory.create_notifier("EMAIL")
        email_notifier.send("¡Tu pedido ha sido enviado!")

        sms_notifier = NotificationFactory.create_notifier("SMS")
        sms_notifier.send("Tu código de verificación es 12345.")
        
        push_notifier = NotificationFactory.create_notifier("PUSH")
        push_notifier.send("Tienes una nueva notificacion en tu app.")
    except ValueError as e:
        print(e)
    print("---------------------------------------\n")

# Esto permite ejecutar este archivo de forma independiente
if __name__ == "__main__":
    test_factory_method()