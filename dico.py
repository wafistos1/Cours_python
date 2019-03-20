#! /usr/bin/env python3
# conding: utf-8


"""
    Cours de Jason de la formation video
"""
echiquier = {}# Creation d'un dictionnaire
echiquier['a', 1] = "tour blanche"
echiquier['b', 1] = "cavalier blanc"
echiquier['c', 1] = "fou blanc"
echiquier['d', 1] = "reine blanche"


# Premiere ligne
echiquier['a', 2] = "pion blanc"
echiquier['b', 2] = "pion blanc"


print(echiquier)

del echiquier['c', 1]
echiquier.pop('b', 1)


print(echiquier)

if __name__ == "__main__":
    print("Salut")
