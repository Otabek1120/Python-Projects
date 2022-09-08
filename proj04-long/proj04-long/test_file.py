# x = input()
# print(x)
# print(type(x))
# if x == "":
#     print("hfdfkfdhf")

# x = set("abdhhifdk")
# print(x)
# x = {(1,2), (3,4), (5,6)}
# print(x)

# x = open("maze_of_obstacles.txt", "r")
# for line in x:
#     print(line)

# y = "efjh"
# print(int(y))
"""
+-----------+
|           |
|           |
|           |
|        X+ |
|         . |
|       *.. |
|           |
|           |
|           |
|           |
|           |
+-----------+

"""

# x = 1
# y = 2
# z = []
# print(z.append((x, y)))
# print(z)


class Linked_List:
    def __init__(self, val):
        self.val = val
        self.next = None

    def insert(self, new_node):
        if

    def __str__(self):
        cur = self
        vals = []
        while cur is not None:
            vals.append(cur.val)
        return "->".join(vals)


vals = [10, 20, 30, 40, 50]
head = Linked_List(vals[0])
cur = head
for val in vals[1:]:
    new_node = Linked_List(val)
    cur.next = new_node
    cur = cur.next

print(Linked_List.__str__(head))



