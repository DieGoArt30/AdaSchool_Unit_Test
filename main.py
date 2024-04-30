"""import unittest


def sum(a, b):
    return a + b


class SumTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)  # Corregido el valor esperado


if __name__ == '__main__':
    unittest.main()

"""

import datetime

class Greeter:
    def greet(self, name):
        # Eliminar espacios en blanco al principio y al final del nombre
        name = name.strip()
        
        # Convertir la primera letra del nombre en mayúscula
        name = name.capitalize()
        
        # Obtener la hora actual
        current_time = datetime.datetime.now().time()
        
        # Devolver el saludo apropiado según la hora actual
        if datetime.time(6, 0) <= current_time <= datetime.time(12, 0):
            greeting = "Buenos días"
        elif datetime.time(18, 0) <= current_time <= datetime.time(22, 0):
            greeting = "Buenas tardes"
        else:
            greeting = "Buenas noches"
        
        # Registrar en la consola
        print(f"Saludo: {greeting} {name}")
        
        # Devolver el saludo
        return f"{greeting} {name}"

# Prueba
greeter = Greeter()
print(greeter.greet(" john "))  # Debería imprimir: "Buenos días John"
print(greeter.greet("Alice"))   # Debería imprimir: "Buenas tardes Alice"
print(greeter.greet("Bob"))     # Debería imprimir: "Buenas noches Bob"
