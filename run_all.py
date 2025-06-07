# Importamos las funciones de prueba de cada patrón
from Creational.FactoryMethod.main import test_factory_method

def main():
    """Función principal que ejecuta todas las pruebas."""
    print("========================================")
    print("== EJECUTANDO TODAS LAS PRUEBAS DE PATRONES ==")
    print("========================================\n")

    # Llama a cada función de prueba
    test_factory_method()
    # ... Llama a las demás aquí

    print("========================================")
    print("==       FIN DE LA EJECUCIÓN        ==")
    print("========================================")

if __name__ == "__main__":
    main()