""" File: tree_funcs_long.py
    Author: Otabek Abduraimov
    Purpose: This file has a few functions
    that do different operations on binary trees.
    It uses:
    -No helper functions
    -No default arguments
    -Recursion and Loops
    Course #: CS 120, Fall 2021
"""

from tree_node import *


def bst_search_loop(root, val):
    """
    :param root: root of a BST
    :param val: value to search
    :return: node which contains the value or None
    This function returns the node if the
    value exists in the tree. If not, it
    returns None
    It uses:
    -No recursion
    -Loop
    """
    if root is None:
        return None
    cur = root
    while cur is not None:
        if cur.val == val:
            return cur
        elif val < cur.val:
            cur = cur.left
        elif val > cur.val:
            cur = cur.right


def tree_search(root, val):
    """
    :param root: root of a binary tree
    :param val: value to search
    :return: node which contains the value
    This functions searches for the value
    using recursion. It returns the node, which
    contains the value or None
    """
    if root is None:
        return None
    if root.val == val:
        return root
    if tree_search(root.left, val) is not None:
        return tree_search(root.left, val)
    if tree_search(root.right, val) is not None:
        return tree_search(root.right, val)
    return None



def bst_insert_loop(root, val):
    """
    :param root: root of a BST, which is not empty
    :param val: value to insert, which is not in the tree
    :return:
    This function inserts a numeric value into a BST.
    -No recursion
    -Loop

    """
    cur = root
    new_node = TreeNode(val)
    while cur is not None:
        if val < cur.val and cur.left is not None:
            cur = cur.left
        elif val > cur.val and cur.right is not None:
            cur = cur.right
        else:
            break
    if val < cur.val:
        cur.left = new_node
    elif val > cur.val:
        cur.right = new_node
    return root


def pre_order_traversal_print(root):
    """
    :param root: root of a binary tree
    :return: None
    This one prints out the values in the
    tree in the pre-order style (root, left, then right)
    """
    if root is None:
        print(end="")
    else:
        print(root.val)
        pre_order_traversal_print(root.left)
        pre_order_traversal_print(root.right)


def in_order_traversal_print(root):
    """
    :param root: root of a binary tree
    :return: None
    This one prints out the values in the
    tree in the in-order style (left, root, then right)
    """
    if root is None:
        print(end="")
    else:
        in_order_traversal_print(root.left)
        print(root.val)
        in_order_traversal_print(root.right)


def post_order_traversal_print(root):
    """
    :param root: root of a binary tree
    :return: None
    This one prints out the values in the
    tree in the post-order style (left, right, then root)
    """
    if root is None:
        print(end="")
    else:
        post_order_traversal_print(root.left)
        post_order_traversal_print(root.right)
        print(root.val)


def in_order_vals(root):
    """
    :param root: root of a binary tree: No BST
    :return: array of values of the tree nodes in oder.
    This function traverse through the tree and puts all
    the values into an array using recursion
    """
    if root is None:
        return []
    else:
        return in_order_vals(root.left) + [root.val] + in_order_vals(root.right)


def bst_max(root):
    """
    :param root: root of a BST, which is not empty
    :return largest_val: the largest val in the tree
    This one finds the largest value in the BST
    using a loop and returns it.
    """
    cur = root
    while cur is not None and cur.right is not None:
        cur = cur.right
    largest_val = cur.val
    return largest_val


def tree_max(root):
    """
    :param root: root of a tree, which is not empty
    :return largest_val: the largest val in the tree
    This one finds the largest value in the tree
    using recursion.
    """
    if root is None:
        return 0
    else:
        return max(root.val, tree_max(root.left), tree_max(root.right))
