""" File: linked_list_recursion_part2.py
    Author: Otabek Abduraimov
    Purpose: This file has three functions that
    do different operations on linked list using recursion.
    It uses:
    -No loops
    -No helper functions
    -No default arguments
    -Recursion
    Course #: CS 120, Fall 2021
"""

from list_node import *


def array_to_list_recursive(data):
    """
    :param data: an array of some values
    :return head: head of a linked list
    This function uses recursion to create a
    linked list from an array
    """
    if len(data) == 0:
        return None
    else:
        head = ListNode(data[0])
        head.next = array_to_list_recursive(data[1:])
        return head


def accordion_recursive(head):
    """
    :param head: head of a linked list
    :return head: head of modified linked list whose
                    every other node has been removed
    This function uses recursion to remove every other node
    in a linked list. It starts with the head of the linked list,
    if the head and head.next are not None. If not it returns None
    """
    if head is None:
        return None
    elif head.next is None:
        return None
    else:
        head = head.next
        if head.next is not None and \
                head.next.next is not None:
            head.next = accordion_recursive(head.next)
        else:
            head.next = None
        return head


def pair_recursive(head1, head2):
    """

    :param head1: head of linked list 1
    :param head2: head of linked list 2
    :return: head: head of a new linked list
    This functions takes the values of each linked list and
    creates a new linked list of tuples, consisting of one value
    from the first list and one value from the other.
    If any of the lists is None, it returns None.
    It's length is equal to the length of shorter linked list
    It uses recursion to solve the problem.
    """
    if head1 is None or head2 is None:
        return None
    else:
        # here neither head1 nor head2 is None
        head = ListNode((head1.val, head2.val))
        head.next = pair_recursive(head1.next, head2.next)
    return head
