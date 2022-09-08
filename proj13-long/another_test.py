
### WOTD = match

# Activity 1

"""
1. if tree is None, ret_val --> (0, None)
2. No we just need to return (depth, val)
3.
4. yes, we need to check both childs of the tree
5. if letter not found, return (depth, None) depth is the bigger one
6. if found only once, return (depth, None)
7. if both children find the node, then keep both nodes and compare the depths
    and return the shallower one
8.
"""


def tree_height(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    if root.left is not None and root.right is None:
        return 1 + tree_height(root.left)
    if root.left is None and root.right is not None:
        return 1 + tree_height(root.right)
    else:
        return tree_height(root.left) + tree_height(root.right)


def _shallow_match(tree, letter, depth=0, matches=None):
    """

    :param tree: a binary tree
    :param letter: the first letter of the node.val
    :param matches: [(depth1, val1), (depth2, val2)]
    :return:
    """

    if matches is None:
        matches = []

    if tree is None:
        return

    if tree.val[0] == letter:
        matches.append((depth, tree.val))

    if tree.left is not None:
        depth = tree_height(tree.left)
        _shallow_match(tree.left, letter, depth, matches)
    if tree.right is not None:
        depth = tree_height(tree.right)
        _shallow_match(tree.right, letter, depth, matches)

    if matches == []:
        return depth, None
    return min(matches)


### ica_Dec_1 WOTD ==  Queue

# Activity 1
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_BFS(root, queue=None):
    if root is None:
        return
    if queue is None:
        queue = []
    queue.append(root)
    while queue is not None:
        print(f"This node: {queue[0].val}")
        queue.pop(0)
        if root.left is not None:
            queue.append(root.left)
        if root.right is not None:
            queue.append(root.right)

        for node in queue:
            print(node.val)

        if len(queue) > 0:
            root = queue[0]
        else:
            queue = None


def shallow_word(root, letter):


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)

root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

root.right.left = TreeNode(13)
root.right.right = TreeNode(20)
print_BFS(root)






