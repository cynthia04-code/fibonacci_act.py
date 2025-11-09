# -*- coding: utf-8 -*-
"""
Fibonacci con función Generator versión 2

Calcula hacia adelante

Tema: yield
La sentencia yield suspende la ejecución de una función y devuelve un valor al invocador, pero conserva suficiente estado para que la 
función pueda reanudarse donde la dejó. Cuando la función se reanuda, continúa la ejecución inmediatamente después de la última ejecución 
de yield. Esto permite que su código genere una serie de valores a lo largo del tiempo, en lugar de calcularlos de una vez y devolverlos
como una lista.
      
if __name__ == "__main__":
    Sirve para ejecutar un bloque de código solo cuando el script se ejecuta directamente, y no cuando se importa 
    como un módulo en otro archivo.

Versión adaptada del material del Prof. Roberto Méndez Méndez

Software: Python (implementado en GitHub)

Repositorio: https://github.com/tuusuario/programa-haskell-funcional

Probar codigo en:https://www.jdoodle.com/python3-programming-online

Editores: 
          
Creado: 06 / 11 / 2025
"""
from typing import Generator

def fibGen(n: int) -> Generator[int, None, None]:
      yield 0
      if n > 0:
          yield 1
      penultimo: int = 0
      ultimo:    int = 1
      for _ in range(1, n):
          penultimo, ultimo = ultimo, penultimo + ultimo
          yield ultimo

if __name__ == "__main__":
    n = int(input("¿Fibonacci hasta la posición?: "))
    for i in fibGen(n):    
        print(i)
