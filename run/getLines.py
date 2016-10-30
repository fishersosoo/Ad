# -*- coding: utf-8 -*-
def blocks(files, size=65536):
    while True:
        b = files.read(size)
        if not b: break
        yield b


def getLines(film_name):
    with open(film_name, "r") as f:
        return sum(bl.count("\n") for bl in blocks(f))

