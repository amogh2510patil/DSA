def lca(self,root, n1, n2):
        # Code here
        flag=[False]
        lca=[None]
        def solve(node):
            l=False 
            r=False
            if not flag[0] and node.left:
                l=solve(node.left)
            if not flag[0] and (node.data==n1 or node.data==n2):
                if l:
                    flag[0]=True
                    lca[0]=node
                    return True
                else:
                    l=True
            if not flag[0] and node.right:
                r=solve(node.right)
            if l and r:
                lca[0]=node
                flag[0]=True
                return True
            else:
                
                return l or r
        
        solve(root)
        return lca[0] if flag[0] else -1