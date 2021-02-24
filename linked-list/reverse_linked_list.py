#!/usr/bin/env python3

def reverse_linked_list(head):
    rev_list = None
    current_node = head
    while  current_node:
        next_node = current_node.next
        current_node.next = rev_list
        rev_list = current_node
        current_node  = next_node
    return rev_list
