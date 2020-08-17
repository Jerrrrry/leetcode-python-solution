class Solution:
    def maxPathSum(self,root:TreeNode)->int:
        def max_gain(node):
            nonlocal max_sum
            ## max_sum would be used and assigned , need declare this 
            if not node:
                return 0
            
            left=max(max_gain(node.left),0)
            right=max(max_gain(node.right),0)


            allpath=node.val+left+right

            max_sum=max(max_sum,allpath)

            return node.val+max(left,right)

        max_sum=float('-inf')

        max_gain(root)

        return max_sum