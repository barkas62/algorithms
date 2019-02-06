class Trie:
    class Node:
        def __init__(self, endIdx = -1 ):
            self.end_idx = endIdx # in leaf: idx of pattern ended here
            self.children = {}    # list of ougoing edges {c : child_node}

        def is_leaf(self):
            return not self.children

    def __init__(self, patterns: 'List[str]'):
        if not patterns:
            self.root = None
            return

        self.root = Trie.Node()

        for idx, pattern in enumerate(patterns):
            node = self.root
            for c in pattern:
                if c in node.children:
                    node = node.children[c]
                else:
                    new_node = Trie.Node()
                    node.children[c] = new_node
                    node = new_node
            node.end_idx = idx

    def match(self, Target: 'str', i):
        if not self.root or self.root.is_leaf():
            return []
        match_idx = []
        node = self.root

        while i < len(Target):
            c = Target[i]
            if c in node.children:
                node = node.children[c]
                if node.end_idx != -1:
                    match_idx.append(node.end_idx)
                i += 1
            else:
                break

        return match_idx

def find_patterns(Target, Patterns):
    pref_trie = Trie(Patterns)
    match_idx = []
    for i in range(len(Target)):
        match = pref_trie.match(Target, i)
        if match:
            match_idx.append( (i, match) )
    return match_idx

Target = "abcdabce"
Patterns = ["a", "ab", "ad", "abc", "cda", "ce", "e"]

res = find_patterns(Target, Patterns)

#tr = Trie(Patterns)
#res = tr.match(Target, 0)

pass


