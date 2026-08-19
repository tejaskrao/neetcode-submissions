class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = [root]
        result = []

        while queue:

            level = [] # store all nodes belonging to the same level
            level_size = len(queue) #find how many nodes are there in this level

            for _ in range(level_size):

                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result