import graphviz


class Node:
    def __init__(self, keys: int=None, leaf: bool=True) -> None:
        if keys is None:
            keys = []
        self.keys = keys
        self.children = []
        self.leaf = leaf

    def __str__(self):
        values = ', '.join(map(lambda key: str(key), self.keys))
        return f"Node: {values}"

    def __repr__(self):
        return ', '.join(map(lambda key: str(key), self.keys))

    def __lt__(self, other: int):
        if self.keys[0] < other:
            return True
        return False

    def __gt__(self, other: int):
        if self.keys[0] > other:
            return True
        return False


class Tree:
    def __init__(self, n: int):
        # n - number of keys in node
        self.n = n
        self.root = Node([], False)

    def __str__(self):
        return str(self.root)

    def insert(self, val: int) -> None:
        pass

    def insert_non_full(self, value: int):
        i = 0
        try:
            while i < self.n and value >= self.root.keys[i]:
                i += 1
            tmp = self.root.keys[:i] + [value] + self.root.keys[i:]
            self.root.keys = tmp.copy()

        except IndexError:
            self.root.keys.append(value)

    def search(self, key):
        return self.search_rec(self.root, key)

    def search_rec(self, node: Node, key: int):
        i = 1
        while i < self.n and key > node.keys[i]:
            i += 1
        if i <= self.n and key in node.keys:
            return (node, i)
        if node.leaf:
            return None
        return self.search_rec(node.keys[i], key)




def test_search():
    node, pos = t.search(7)
    print(f"7 in {node} on pos {pos}")


t = Tree(4)
t.root.keys = [Node([0, 1]), 2, Node([3]), 4, Node([5, 6, 7])]

print(t)