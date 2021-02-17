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

    def insert(self, index, value):
        if 0 <= index < self.length:
            for i in range(self.length, index, -1):
                self.data[i] = self.data[i-1]
            self.length += 1
            self.data[index] = value
        else:
            self.append(value)

    def remove(self, value):
        value_list = list(self.data.values())
        if value in value_list:
            index = value_list.index(value)
            for i in range(index, self.length-1):
                self.data[i] = self.data[i+1]
            del self.data[self.length -1]
            self.length -= 1


if __name__ == '__main__':
    my_array = Array()
    my_array.append('me')
    my_array.append('you')
    my_array.append('we')
    my_array.append('they')
    my_array.insert(2, 'i know')
    print(my_array.data)
    print(my_array.length)
