class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        if not n:
            return 0
        
        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        
        res = 0
        
        visit = set()
        
        
        def dfs(i):

            visit.add(i)
            for nei in adj[i]:
                if nei not in visit:
                    dfs(nei)

            
        for i in range(n):
            if i not in visit:
                
                dfs(i)
                res += 1

        return res