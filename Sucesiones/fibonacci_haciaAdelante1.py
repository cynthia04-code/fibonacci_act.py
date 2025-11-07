# -*- coding: utf-8 -*-
"""
Fibonacci hacia delante

Objetivo: Calcular el valor n-ésimo de la suceción de Fibonacci sin saturar la memoria

Tema: Cálculo de una sucesión recursiva hacia adelante para evitar llamadas redundantes
 
 if __name__ == "__main__":
    Sirve para ejecutar un bloque de código solo cuando el script se ejecuta 
    directamente, y no cuando se importa como un módulo en otro archivo.

Versión adaptada del material del Prof. Roberto Méndez Méndez

Software: Python (implementado en GitHub)

Editor:Cynthia

Creado: 06 / 11 / 2025
"""
def fibAbel(n: int) -> int:
    if n == 0: return n
    penultimo: int = 0
    ultimo:    int = 1
    for _ in range(1, n):
        penultimo, ultimo = ultimo, penultimo + ultimo
    return ultimo

if __name__ == "__main__":
    n = int(input("¿De qué posición quieres el valor de Fiboacci?: "))
    print(f"El  {n}-ésimo valor de Fibonacci es: {fibAbel(n)}")
