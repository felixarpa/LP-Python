#!/usr/bin/python3

class KeyTree(object):
    def __init__(slef, value = 'root', type = str, children = None):
        self.type = type
        self.value = value
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.value

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)