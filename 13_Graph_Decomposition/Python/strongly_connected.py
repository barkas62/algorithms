class Node:
    def __init__(self, id):
        self.id = id
        self.adj_nodes = []
        self.inv_nodes = []
        self.visited = False

    def add_edge(self, node):
        self.adj_nodes.append(node)
        node.inv_nodes.append(self)


class Graph:
    def __init__(self, n_nodes):
        self.nodes = [Node(i) for i in range(n_nodes)]

    def add_edge(self, i, j):
        assert 0 <= i < len(self.nodes) and 0 <= i < len(self.nodes)
        self.nodes[i].add_edge(self.nodes[j])

    def visit(self, node, node_stack):
        node.visited = True
        for next_node in node.adj_nodes:
            if not next_node.visited:
                self.visit(next_node, node_stack)
        node_stack.append(node)

    def dfs(self, node_stack):
        for node in self.nodes:
            node.visited = False

        for node in self.nodes:
            if not node.visited:
                self.visit(node, node_stack)


    def visit_inv(self, node, cur_cc):
        node.visited = True
        cur_cc.append(node.id)
        for next_node in node.inv_nodes:
            if not next_node.visited:
                self.visit_inv(next_node, cur_cc)


    def strongly_connected(self):
        node_stack = []
        self.dfs(node_stack)

        for node in self.nodes:
            node.visited = False
        all_cc = []
        while node_stack:
            node = node_stack.pop()
            if not node.visited:
                cur_cc = []
                self.visit_inv(node, cur_cc)
                all_cc.append(cur_cc)
        return all_cc


G = Graph(5)

G.add_edge(0, 3)
G.add_edge(3, 4)
G.add_edge(4, 3)
G.add_edge(0, 2)
G.add_edge(2, 1)
G.add_edge(1, 0)

strongly_connected_comps = G.strongly_connected()

pass