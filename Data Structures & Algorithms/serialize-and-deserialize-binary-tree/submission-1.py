# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # # Encodes a tree to a single string.
    # def serialize(self, root: Optional[TreeNode]) -> str:
    #     queue = deque([root])
    #     string = []
    #     level = 1
    #     while queue:
    #         only_nones = True
    #         for i in range(level):
    #             node = queue.popleft()
    #             if node:
    #                 string.append(node.val)
    #                 queue.append(node.left)
    #                 queue.append(node.right)
    #                 only_nones = False
    #             else:
    #                 string.append(None)
    #                 queue.append(None)
    #                 queue.append(None)
    #         level *= 2
    #         if only_nones:
    #             queue.clear()
    #     string = ",".join(map(str, string))
    #     return string
            

        
    # # Decodes your encoded data to tree.
    # def deserialize(self, data: str) -> Optional[TreeNode]:
    #     values = data.split(",")
    #     nodes = []

    #     for value in values:
    #         if value == 'None':
    #             nodes.append(None)
    #         else:
    #             nodes.append(TreeNode(value))
        
    #     for i, node in enumerate(nodes):
    #         if not node:
    #             continue
    #         node.left = nodes[i*2+1]
    #         node.right = nodes[i*2+2]
        
    #     return nodes[0]

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        queue = deque([root])
        result = []
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")
                
        return ",".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
            
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1
        
        while queue and i < len(values):
            node = queue.popleft()
            
            # Process left child
            if values[i] != "None":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            
            # Process right child
            if i < len(values) and values[i] != "None":
                node.right = TreeNode(int(values[i]))
                queue.append(node.right)
            i += 1
            
        return root

    
