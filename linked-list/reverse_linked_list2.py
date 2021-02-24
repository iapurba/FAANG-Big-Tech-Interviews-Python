#!/usr/bin/env python3

def reverse_between(head, left, right):
    current_node = head
    leader = head
    counter = 1

    while counter < left:
        leader = current_node
        current_node = current_node.next
        counter += 1

    tail = current_node
    new_list = current_node

    while counter >= left and counter <= right:
        next_node = current_node.next
        current_node.next = new_list
        new_list = current_node
        current_node = next_node
        counter += 1

    if left > 1:
        leader.next = new_list
        tail.next = current_node
        return head
    else:
        tail.next = current_node
        return new_list
