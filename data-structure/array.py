#!/usr/bin/env python3

class Array:
    def __init__(self):
        self.data = {}
        self.length = 0

    def get(self, index):
        if self.length:
            return self.data[index]

    def append(self, value):
        self.data[self.length] = value
        self.length += 1

    def pop(self):
        if self.length:
            last_item = self.data[self.length - 1]
            del self.data[self.length - 1]
            return last_item
            self.length -= 1


if __name__ == '__main__':
    my_array = Array()
    my_array.append('me')
    my_array.append('you')
    my_array.append('we')
    my_array.append('they')
    print(my_array.data)
    print(my_array.get(2))
