#!/usr/bin/env python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def prepend(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = self.head
        return self

    def append(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = self.tail
        return self

    def insert(self, index, value):
        new_node = Node(value)
        if index == 0:
            self.prepend(value)
        else:
            leader = self._travers_to_right(index)
            new_node.next = leader.next
            leader.next = new_node
        return self

    def remove(self, index):
        if index == 0:
            unwanted_node = self.head
            self.head = self.head.next
            del unwanted_node
        else:
            leader = self._travers_to_right(index-1)
            unwanted_node = leader.next
            leader.next = unwanted_node.next
            del unwanted_node
        return self

    def _travers_to_right(self, index):
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node.next
            counter += 1
        return current_node


sll = LinkedList()
