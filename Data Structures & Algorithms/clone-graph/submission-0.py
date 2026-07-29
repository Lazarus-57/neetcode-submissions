class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #uses a Hash map to create new identical nodes and a DFS inner function to map out the nodes
        hashmap = {}
        if not node:
            return None
        
        def dfs(curr):
            #is node already in hashmap
            if curr in hashmap:
                return hashmap[curr]

            #if node not in hashmap
            clone = Node(curr.val)
            hashmap[curr] = clone

            #call dfs on the node's neighbours
            for neighbors in curr.neighbors:
                clone.neighbors.append(dfs(neighbors))

            return clone

        return dfs(node)
        