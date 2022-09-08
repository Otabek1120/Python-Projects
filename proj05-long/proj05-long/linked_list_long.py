""" File: linked_list_ling.py
    Author: Otabek Abduraimov
    Purpose: This program consists of 6 different
             functions all dealing with linked lists:
             1. is_sorted()
             2. list_sum()
             3. list_sum()
             4. partition_list()
             5. list_length()
             6. accordion_4()
             7. pair()
    Course #: CS 120, Fall 2021
"""

from list_node import *


def is_sorted(head):
    """
    :param head: the head of a linked list
    :return: True if sorted, False if not
    This function takes the head of
    a linked list and checks whether
    the vals of its nodes are in the
    ascending order
    """
    ret_val = None
    if head is None:
        ret_val = True
    elif head.next is None:
        ret_val = True
    else:
        cur = head
        while cur.next is not None:
            if cur.val > cur.next.val:
                ret_val = False
                break
            else:
                ret_val = True
            cur = cur.next
    return ret_val


def list_sum(head):
    """
    :param head: the head of a linked list
    :return ret_val: the sum of the vals of the nodes
    This function takes the head of
    linked list and calculates the sum
    of the vals of the nodes.
    """
    ret_val = 0
    if head is None:
        ret_val = 0
    else:
        cur = head
        while cur is not None:
            ret_val += cur.val
            cur = cur.next

    return ret_val


def partition_list(head):
    """
    :param head: head of a linked list
    :return list_1: the linkd list with the vals
                    at the even indexes
            list_2: the one with the vals
                    at the odd indexes
    This one also takes the head
    of a linked list. What it does is
    to divide the list into two different
    lists.
    The first one has the vals at
    even indexes (0,2,4,6...)
    The other has the vals at
    odd indexes (1,3,5,7....)
    """
    if head is None:
        return None
    elif head.next is None:
        list_1 = head
        list_2 = None
        return list_1, list_2
    else:
        list_1 = head
        list_2 = head.next
        cur_1 = list_1
        cur_2 = list_2
        while cur_1 is not None and cur_2 is not None:
            if cur_1.next is not None and cur_1.next.next is not None:
                cur_1.next = cur_1.next.next
                cur_1 = cur_1.next
            else:
                cur_1.next = None
                cur_1 = cur_1.next
            if cur_2.next is not None and cur_2.next.next is not None:
                cur_2.next = cur_2.next.next
                cur_2 = cur_2.next
            else:
                cur_2.next = None
                cur_2 = cur_2.next
        return list_1, list_2


def list_length(head):
    """
    :param head: head of a linked list
    :return: length: the len of the linked list
    What this one does is to find
    the length of a linked list
    """
    length = 0
    cur = head
    while cur is not None:
        length += 1
        cur = cur.next
    return length


def accordion_4(head, start_pos):
    """
    :param head: head of a linked list
    :param start_pos: the index of the first node
                        to keep
    :return: ret_val_head: the head of the changed list
    This one removes three out of four
    nodes in the list and it starts the head
    of the list at the start position
    given by the user
    """
    list_len = list_length(head)
    if list_len < start_pos:
        return None
    else:
        cur = head
        while start_pos > 0:
            cur = cur.next
            start_pos -= 1
        ret_val_head = cur
        if list_len <= 4:
            return ret_val_head
        else:
            cur2 = ret_val_head
            while cur2 is not None:
                if cur2.next is not None:
                    if cur2.next.next is not None:
                        if cur2.next.next.next is not None:
                            if cur2.next.next.next.next is not None:
                                cur2.next = cur2.next.next.next.next
                            else:
                                cur2.next = None
                        else:
                            cur2.next = None
                    else:
                        cur2.next = None
                else:
                    cur2.next = None
                cur2 = cur2.next
            return ret_val_head


def pair(list1, list2):
    """
    :param list1: a linked list
    :param list2: another linked list
    :return: newLinkedList: a linked list with the nodes
                            whose vals are a tuple of one
                            value from the list1 and
                            one from list2
    This one makes a new list with nodes whose vals
    are a tuple of two values, one from the list one
    and the other from list two.
    If the lists have different lengths, it will stop
    at the last node of the shorter list.

    """
    if list1 is None or list2 is None:
        return None
    else:
        cur1 = list1
        cur2 = list2
        newLinkedList = ListNode((cur1.val, cur2.val))
        cur1 = cur1.next
        cur2 = cur2.next
        tail = newLinkedList
        while cur1 is not None and cur2 is not None:

            tail.next = ListNode((cur1.val, cur2.val))
            tail = tail.next
            cur1 = cur1.next
            cur2 = cur2.next

        return newLinkedList

