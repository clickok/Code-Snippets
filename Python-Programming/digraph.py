"""
A relatively generic implementation of a directed graph in Python
"""

class GraphNode:
    """
    A node in the graph,
    """
    def __init__(self, **kwargs):
        self.__dict__['children'] = set()
        self.__dict__['parents'] = set()
        self.values = dict()
        self.set_values(**kwargs)
        
    def __setattr__(self, name, value):
        """Access control for the attributes `children` and `parents`."""
        if name in ('children', 'parents'):
            raise AttributeError('Immutable attribute:', name,)
        super().__setattr__(name, value)
        
    def __delattr__(self, name):
        """Access control for the attributes `children` and `parents`."""
        if name not in ('children', 'parents'):
            del self.__dict__[name]
        else:
            raise AttributeError('Immutable attribute:', name)

    def set_values(self, **kwargs):
        self.values.update(kwargs)
        
    def __repr__(self):
        parents_str = ','.join([repr(x) for x in self.parents])
        children_str = ','.join([repr(x) for x in self.children])

        return "(p: %s, c: %s)" % (parents_str, children_str)


class DirectedGraph:
    def __init__(self):
        self.clear()
        
    def clear(self):
        self.node_map = dict()
        
    def __contains__(self, node):
        return node_key in self.node_map

    def __getitem__(self, key):
        return self.node_map[key]
    
    def __iter__(self):
        return iter(self.node_map.keys())
    
    def __len__(self):
        return len(self.node_map)
    
    def __repr__(self):
        return repr(self.node_map)
    
    def add_edge(self, parent, child):
        """Add an edge from parent --> child."""
        # Assertions go here
        self.get_children(parent).add(child)
        self.get_parents(child).add(parent)
        
    def add_edges(self, edges):
        """Add multiple edges, as an iterable of the form (parent, child)."""
        for edge in edges:
            parent, child = edge
            self.add_edge(parent, child)
    
    def add_node(self, node_key, attrs=None):
        """Add a GraphNode, optionally specifying its initial attributes."""
        if attrs is None:
            attrs = dict()
        node = GraphNode(**attrs)
        self.node_map.setdefault(node_key, node)

    def connect(self, node1, node2):
        """Add edges to connect two nodes."""
        self.add_edge(node1, node2)
        self.add_edge(node2, node1)
        
    def get_node(self, node_key):
        """Get the node corresponding to `node_key`."""
        return self[node_key]
        
    def get_children(self, node_key):
        """Get the child nodes of a given node."""
        return self.get_node_set(node_key, relation='children')
    
    def get_parents(self, node_key):
        """Get the parent nodes of a given node."""
        return self.get_node_set(node_key, relation='parents')
    
    def get_node_set(self, node_key, relation):
        """Get an attribute of a node, e.g., its parents or children."""
        node = self[node_key]
        return getattr(node, relation)
    
    def get_orphans(self):
        """Return all orphan nodes, i.e., those without parents."""
        return [k for k in self.node_map if not self.has_parents(k)]
    
    def has_children(self, node_key):
        """True if the node has one child node or more."""
        return len(self.get_children(node_key)) > 0
    
    def has_parents(self, node_key):
        """True if the node has one parent node or more."""
        return len(self.get_parents(node_key)) > 0
    
    def has_edge(self, parent, child):
        """True if there is an edge from parent --> child."""
        assert(self.has_node(child))
        assert(self.has_node(parent))
        return child in self.get_children(parent)
        
    def has_node(self, node_key):
        """True if the node is present in the graph."""
        return node_key in self.node_map
    
    def is_empty(self):
        """True if the graph has no vertices, false otherwise."""
        return len(self.node_map) == 0
    
    def is_isolated(self, node_key):
        """True if a node has no incoming/outgoing edges."""
        return not (self.has_children(node_key) and self.has_parents(node_key))

    def remove_node(self, node_key):
        """Remove a node from the graph."""
        # Remove record of node from parents/children
        for p in self.get_parents(node_key):
            self.get_children(p).remove(node_key)
            
        for c in self.get_children(node_key):
            self.get_parents(c).remove(node_key)
            
        if node_key in self.node_map:
            self.node_map.pop(node_key)

    def is_cyclic(self):
        """DFS with checking for cycles."""
        flag    = False
        nodes   = set(iter(self.node_map.keys()))
        visited = set() # fully explored
        marked  = set() # marked as having been seen

        def expand(node):
            """
            Recursive DFS, operates by marking nodes temporarily if they've
            been seen but not all of their children have been visited, and
            returning False if such a mark is encountered.
            """
            nonlocal visited, marked, flag

            if node in marked:
                flag = True
            elif node in visited:
                pass
            else:
                marked.add(node)
                for child in self.get_children(node):
                    expand(child)
                marked.remove(node)
                visited.add(node)

        
        while nodes != visited:
            expand(set.difference(nodes, visited).pop())
            if flag:
                return True 

        return False

    def is_connected(self, node):
        """DFS to check that all nodes are reachable from some node"""
        visited = set()
        stack   = [node]

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            else:
                stack.extend([c for c in self.get_children(node)])
                visited.add(node)

        if visited != set(self):
            return False
        else:
            return True


class SparseDirectedGraph(DirectedGraph):
    """
    Same as the DirectedGraph, but with a nodes stored in a `defaultdict` 
    instead of the normal Python `dict`.
    """
    from collections import defaultdict
    def clear(self):
        self.node_map = defaultdict(GraphNode)