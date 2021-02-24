#!/usr/bin/env python3

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class Stack:
	def __init__(self):
		self.top = None
		self.bottom = None
		self.length = 0

	def peek(self):
		return self.top

	def push(self, data):
		new_node = Node(data)
		if self.top:
			new_node.next = self.top
			self.top = new_node
		else:
			new_node.next = self.top
			self.top = new_node
			self.bottom = self.top
		self.length += 1
		return self

	def pop(self):
		if self.top:
			if self.top != self.bottom:
				top_node = self.top
				self.top = self.top.next
				del top_node
			else:
				top_node = self.top
				self.top = self.top.next
				self.bottom = self.top
				del top_node
		self.length -= 1
		return self


my_stack = Stack()
my_stack.push("google.com")
my_stack.push("airbnb.com")
my_stack.push("apple.com")

my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack.top)
print(my_stack.bottom)
print(my_stack.length)
