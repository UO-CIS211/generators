"""
A simple demonstration of the usefulness of 
generators where it would be more difficult to 
create a Java-style iterator.  We construct a 
directed graph and provide it with a depth-first 
traversal generator, which can be used in iteration. 
"""

class digraph:
    """Directed graph represented as a mapping from nodes to lists 
    of adjacent nodes.
    """
    
    def __init__(self):
        self.edgelists = { }

    def edge(self, from_node, to_node):
        """Create an edge from from_node to to_node"""
        if from_node not in self.edgelists:
            self.edgelists[from_node] = [ ]
        if to_node not in self.edgelists:
            self.edgelists[to_node] = [ ]
        if to_node not in self.edgelists[from_node]:
            self.edgelists[from_node].append(to_node)

    def u_edge(self, from_node, to_node):
        """Undirected edge represented as a pair of directed edges"""
        self.edge(from_node, to_node)
        self.edge(to_node, from_node)

    def nodes_depth_first(self,root):
        """Iterate nodes in depth-first order starting at root"""
        assert root in self.edgelists, "Must designate a root node in the graph"
        yield from self._nodes_dfs(root, set())

    def _nodes_dfs(self, root, visited):
        """Depth-first traversal of graph"""
        if root in visited:
            return
        visited.add(root)
        yield root
        for adjacent in self.edgelists[root]:
            yield from self._nodes_dfs(adjacent,visited)
        return



# Some connections in Oregon and Washington, to Vancouver BC
g = digraph()
g.u_edge("Portland", "Eugene")
g.u_edge("Eugene", "Bend")
g.u_edge("Eugene", "Medford")
g.u_edge("Portland", "Seattle")
g.u_edge("Medford", "Klamath Falls")
g.u_edge("Bend", "Redmond")
g.u_edge("Seattle", "Vancouver")
g.u_edge("Vancouver", "Seattle")
g.u_edge("Seattle", "Yakima")
g.u_edge("Portland", "Pasco")
g.u_edge("Pasco", "Yakima")

print("Depth first from Eugene")
for city in g.nodes_depth_first("Eugene"):
    print(city)

print()
    
print("Depth first from Vancouver")
for city in g.nodes_depth_first("Vancouver"):
    print(city)

        
