from abc import ABC, abstractmethod

class CWMeta:
    def __new__(cls):
        print("int new")
        return super().__new__(cls)

    def __init__(self):
        print("in init")

obj = CWMeta()
